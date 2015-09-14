#!/usr/bin/env python
# -*- coding: utf-8 -*-
#! python2
'''
Created on 12 Ağu 2015

@author: Sinan Cetinkaya sinancetinkaya****@gmail.com
'''

import sys, os 
from globalhotkeys import GlobalHotKeys
import speech_recognition as sr
from pykeyboard import PyKeyboard
import ConfigParser
import logging
from io import open

if getattr(sys, 'frozen', False):
    APP_DIR = os.path.dirname(sys.executable)
else:
    APP_DIR = os.path.dirname(os.path.realpath(__file__))
if not APP_DIR:
    sys.exit("APP_DIR cannot be empty")

CONFIG_FILE = APP_DIR + '\\config.ini'

ch = logging.StreamHandler(stream=sys.stdout)
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
LOG = logging.getLogger()
LOG.addHandler(ch)
LOG.setLevel(logging.DEBUG)

config = ConfigParser.RawConfigParser()
config.optionxform = str

if os.path.isfile(CONFIG_FILE):
    if os.access(CONFIG_FILE, os.R_OK):
        with open(CONFIG_FILE,'r', encoding="utf-8-sig") as fp:
            config.readfp(fp)
    else:
        sys.exit("Config file access error")
else:
    sys.exit("No Config file found in %s" % APP_DIR)

LANG = config.get('parameters', 'lang')
HOTKEY_LISTEN = int(config.get('parameters', 'hotkey_listen'), 16)
HOTKEY_QUIT = int(config.get('parameters', 'hotkey_quit'), 16)
API_KEY = config.get('parameters', 'api_key')

try:
    if not API_KEY:
        r = sr.Recognizer(language = LANG.encode('ascii','ignore')) 
    else:
        r = sr.Recognizer(language = LANG.encode('ascii','ignore'), 
                          key = API_KEY)
except:
    LOG.error("", exc_info=True)
    sys.exit()

try:
    k = PyKeyboard()
except:
    LOG.error("", exc_info=True)
    sys.exit()


def main():
    
    print ("Voice2Keyboard BETA. Written by Sinan Cetinkaya")
    print ("Check the config.ini for settings")
    print ("Translated to %s by %s" % (LANG, config.get(LANG, 'translator')))
    print (config.get(LANG, 'Registering_hotkeys'))
    GlobalHotKeys.register(HOTKEY_LISTEN, GlobalHotKeys.MOD_CONTROL | GlobalHotKeys.MOD_ALT, listen)
    GlobalHotKeys.register(HOTKEY_QUIT, GlobalHotKeys.MOD_CONTROL | GlobalHotKeys.MOD_ALT, quit)
    print (config.get(LANG, 'Ready'))
    GlobalHotKeys.listen()

def quit():
    
    print (config.get(LANG, 'Unregistering_hotkeys'))
    GlobalHotKeys.register(HOTKEY_LISTEN, GlobalHotKeys.MOD_CONTROL | GlobalHotKeys.MOD_ALT, None)
    GlobalHotKeys.register(HOTKEY_QUIT, GlobalHotKeys.MOD_CONTROL | GlobalHotKeys.MOD_ALT, None)
    sys.exit(config.get(LANG, 'Bye'))

def listen():
    
    print (config.get(LANG, 'Listening'))
    text = ''
    with sr.Microphone() as source:                # use the default microphone as the audio source
        audio = r.listen(source)                   # listen for the first phrase and extract it into audio data
    print (config.get(LANG, 'Processing'))
    try:
        text = r.recognize(audio)    # recognize speech using Google Speech Recognition
        LOG.info(text)
        k.type_string(text)
        return True
    except IndexError:                                  # the API key didn't work
        LOG.info(config.get(LANG, "No_internet_connection"))
    except KeyError:                                    # the API key didn't work
        LOG.info(config.get(LANG, "Invalid_API_key_or_quota_maxed_out"))
    except LookupError:                                 # speech is unintelligible
        LOG.info(config.get(LANG, "Could_not_understand_audio"))
    else:
        LOG.info(config.get(LANG, "Unknown_error"), exc_info=True)
    return False
    
if __name__ == '__main__':
        main()

