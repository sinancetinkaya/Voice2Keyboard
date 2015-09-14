#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from cx_Freeze import setup, Executable

include_files = [r'H:\users\sinan\workspace\v2k\config.ini', 
                 r"H:\Program Files\Python27\Lib\site-packages\speech_recognition"
                 ]
setup(
      name = "Voice2Keyboard",
      version = "1.01",
      description = "Converting Speech to Keyboard inputs",
      author = "Sinan Cetinkaya",
      executables = [Executable(script="v2k.py",
                                base="Console",
                                icon="keyboard_key_speaker.ico")
                     ],
      options = {"build_exe": {#'excludes':excludes,
                               "build_exe": "v2k",
                               'include_files':include_files,
                               }
                 }
    )