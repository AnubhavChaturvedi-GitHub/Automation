import random

import pyautogui as ui
from Head.Mouth import speak
from Data.dlg_data.dlg import *

closedlg_random = random.choice(closedlg)
def close():
    speak(closedlg_random)
    ui.hotkey("alt","f4")