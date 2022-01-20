# -*- coding: utf-8 -*-
# !/usr/bin/env python3
# =============================================================================
# Created By  : Sinan Cetinkaya <sinancetinkaya35@gmail.com>
# =============================================================================
import os
import signal
import time
from logging.handlers import TimedRotatingFileHandler
from pathlib import Path
import logging
import speech_recognition
from pywinauto import keyboard
from pywinauto.win32_hooks import Hook, KeyboardEvent

APP_DIRECTORY = os.path.dirname(os.path.realpath(__file__))
LOGS_DIRECTORY = os.path.join(APP_DIRECTORY, 'logs')

if not os.path.exists(LOGS_DIRECTORY):
    os.makedirs(LOGS_DIRECTORY)

log_file_handler = TimedRotatingFileHandler(
    os.path.join(LOGS_DIRECTORY, f"{Path(__file__).stem}.log"),
    when="midnight",
    encoding='utf-8',
    backupCount=10
)

# noinspection PyArgumentList
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s.%(msecs)03d [%(levelname)-5.5s] %(name)s.%(funcName)s(),%(lineno)d: %(message)s',
    datefmt="%Y%m%d_%H%M%S",
    handlers=[logging.StreamHandler(), log_file_handler]
)
logging.Formatter.converter = time.localtime
log = logging.getLogger(__name__)


class Voice2Keyboard:
    def __init__(self):
        self.hook = Hook()
        self.hook.handler = self.on_event
        self.HOTKEY = {'Lwin', 'Z'}
        self.LANGUAGE = "tr-TR"
        self.recognizer = speech_recognition.Recognizer()
        self.lock = False
        self.list_devices()

    def list_devices(self):
        for index, name in enumerate(speech_recognition.Microphone.list_microphone_names()):
            log.info(f"device_index[{index}]='{name}'")

        log.info("if microphone doesn't work, try to set DEVICE_INDEX to one the devices above")
        self.DEVICE_INDEX = None

    def on_event(self, event):
        if not isinstance(event, KeyboardEvent) or event.event_type != 'key down' or self.lock:
            return False

        if set(event.pressed_key) != self.HOTKEY:
            # log.info(event.__dict__)
            return False

        self.lock = True

        log.info("listening...")
        with speech_recognition.Microphone(device_index=self.DEVICE_INDEX) as source:
            audio = self.recognizer.listen(source)

        log.info("converting audio to text...")
        try:
            text = self.recognizer.recognize_google(
                audio_data=audio,
                # This uses Google Speech Engine's public API key.
                # If you exceed the quota, you need your own API key from https://console.developers.google.com/
                key="AIzaSyBOti4mM-6x9WDnZIjIeyEU21OpBXqWBgw",
                language=self.LANGUAGE
            )
            log.info(f"typing '{text}'")
            keyboard.send_keys(text, with_spaces=True)
        except:
            log.exception("")
        finally:
            keyboard.send_keys("{VK_LWIN up}{Z up}")
            self.lock = False

    def listen(self):
        log.info(f"registering {self.HOTKEY} hotkey")
        self.hook.hook(keyboard=True, mouse=False)

    def exit(self):
        log.info(f"unregistering hotkey")
        self.hook.unhook_keyboard()


if __name__ == '__main__':
    v2k = Voice2Keyboard()

    for signame in ['SIGINT', 'SIGTERM']:
        signal.signal(getattr(signal, signame), lambda signum, frame: v2k.exit())

    log.info("use Ctrl + C to stop the script")
    v2k.listen()


