#! python3
# hotScreenshot.py - программа, позволяющая делать моментальный скрин и сохранять его на рабочем столе

import pyautogui
import keyboard 
import time
import os 

# path to save on Desktop
path = '~\\Desktop'
fullPath = os.path.expanduser(path)
os.chdir(fullPath)

# take a screenShot combination of keys ctrl+`
count = 0
while True:
    time.sleep(0.05)
    try:
        if keyboard.is_pressed('ctrl+`'):
            im = pyautogui.screenshot()
            im.save('screenshot ' + str(count) + '.png')
            count += 1
            continue
    except KeyboardInterrupt:
        break

    

















