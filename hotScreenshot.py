#! python3
# hotScreenshot.py - программа, позволяющая делать моментальный скрин и сохранять его на рабочем столе

import pyautogui, os, keyboard, time

nameDir = 'C:\\Users\\i7-2\\Desktop'
 
os.chdir(nameDir)

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

    

















