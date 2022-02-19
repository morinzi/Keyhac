import sys
import os
import datetime
import subprocess

import pyauto
from keyhac import *

# 別途，レジストリ編集により，capslockをctrlに変更。


def configure(keymap):
    print("body mode.")
    keymap.replaceKey("RShift", "Delete")
    keymap_global = keymap.defineWindowKeymap()
    keymap_global["O-(29)"] = lambda: keymap.wnd.setImeStatus(0)
    keymap_global["O-(28)"] = lambda: keymap.wnd.setImeStatus(1)

    keymap.defineModifier(29, "User0") # 無変換
    keymap.defineModifier(28, "User1") # 変換
    keymap.defineModifier(194, "User3") # 未割当の仮想キー

    keymap_global["User3-Plus"] = "Left"
    keymap_global["User3-Colon"] = "Right"
    keymap_global["User3-Atmark"] = "Up"
    keymap_global["User3-Slash"] = "Down"

    keymap_global["User3-1"] = "F1"
    keymap_global["User3-2"] = "F2"
    keymap_global["User3-3"] = "F3"
    keymap_global["User3-4"] = "F4"
    keymap_global["User3-5"] = "F5"
    keymap_global["User3-6"] = "F6"
    keymap_global["User3-7"] = "F7"
    keymap_global["User3-8"] = "F8"
    keymap_global["User3-9"] = "F9"
    keymap_global["User3-0"] = "F10"
    keymap_global["User3-Minus"] = "F11"
    keymap_global["User3-Caret"] = "F12"

    keymap_global["User3-K"] = "Home"
    keymap_global["User3-Comma"] = "End"
    # keymap_global["User3-L"] = "PageUp"
    # keymap_global["User3-Period"] = "PageDown"

    keymap_global["LCtrl-User3-Plus"] = "LCtrl-Left"
    keymap_global["LCtrl-User3-Colon"] = "LCtrl-Right"
    keymap_global["LCtrl-LShift-User3-Plus"] = "LCtrl-LShift-Left"
    keymap_global["LCtrl-LShift-User3-Colon"] = "LCtrl-LShift-Right"
    keymap_global["LShift-User3-Plus"] = "LShift-Left"
    keymap_global["LShift-User3-Colon"] = "LShift-Right"

    keymap_global["LShift-Esc"] = keymap.defineMultiStrokeKeymap("LShift-Esc")
    pathToAppData = os.environ.get('AppData')
    print(pathToAppData)
    keymap_global["LShift-Esc"]["Enter"] = lambda: subprocess.Popen([pathToAppData + "/Keyhac/run_hhkb.bat"])

    # shared
    keymap_global["LAlt-Plus"] = "LCtrl-Left"
    keymap_global["LAlt-Colon"] = "LCtrl-Right"
    keymap_global["LAlt-LShift-Plus"] = "LCtrl-LShift-Left"
    keymap_global["LAlt-LShift-Colon"] = "LCtrl-LShift-Right"
    keymap_global["LAlt-LShift-Enter"] = \
        lambda: [keymap.command_InputKey("LCtrl-Left")(), keymap.command_InputKey("LCtrl-LShift-Right")()]
    