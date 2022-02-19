import sys
import os
import datetime
import subprocess

import pyauto
from keyhac import *

# 別途，レジストリ編集により，capslockをctrlに変更。

def fKeyMode(keymap, keymap_global, isFKeyMode):
    for i in range(13):
        keyNum = i + 1
        if isFKeyMode: 
            keymap_global[str(keyNum)] = "F" + str(keyNum)
        else:
            keymap_global[str(keyNum)] = str(keyNum)
    keymap.updateKeymap()

def configure(keymap):
    print("hhkb mode.")
    keymap_global = keymap.defineWindowKeymap()
    keymap.replaceKey(194, "Ctrl")

    isFKeyMode = bool(False)
    def handleFKeyMode():
        global isFKeyMode
        fKeyMode(keymap, keymap_global, not isFKeyMode)
        isFKeyMode = not isFKeyMode

    keymap_global["LShift-Esc"] = keymap.defineMultiStrokeKeymap("LShift-Esc")
    keymap_global["LShift-Esc"]["Back"] = lambda: handleFKeyMode()
    pathToAppData = os.environ.get('AppData')
    print(pathToAppData)
    keymap_global["LShift-Esc"]["Enter"] = lambda: subprocess.Popen([pathToAppData + "/Keyhac/run_body.bat"])

    # shared
    keymap_global["LAlt-Plus"] = "LCtrl-Left"
    keymap_global["LAlt-Colon"] = "LCtrl-Right"
    keymap_global["LAlt-LShift-Plus"] = "LCtrl-LShift-Left"
    keymap_global["LAlt-LShift-Colon"] = "LCtrl-LShift-Right"
    keymap_global["LAlt-LShift-Enter"] = \
        lambda: [keymap.command_InputKey("LCtrl-Left")(), keymap.command_InputKey("LCtrl-LShift-Right")()]

    