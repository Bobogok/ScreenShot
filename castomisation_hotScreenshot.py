# !python3
# castomisation_hotScreenshot.py - Приложение для кастомизации hotScreenshot.py

import pyautogui
import keyboard
import datetime
import time
import os


class Castomisation:
    def castomisation_take_screenshot_by_keys(self):
        print('Вы хотие изменить значения горячих клавишь. Продолжить? Y/N')
        answer = str(input()).lower()
        accept_keys = ['y', 'н', 'да']

        if answer in accept_keys:
            print('Нажмите на первую клавишу комбинации')
            key_first = keyboard.read_key()
            print('Вы нажали: ' + key_first)
            time.sleep(1)

            print('Нажмите на вторую клавишу комбинации')
            key_second = keyboard.read_key()
            print('Вы нажали: ' + key_second)

            print('Вы изменили комбинацию клавишь на: %s+%s' % (key_first, key_second))
            time.sleep(1)
        else:
            print('Отмена изменений...')

Castomisation().castomisation_take_screenshot_by_keys()

# ТОDO сделать кастомизацию для take_screenshot_by_keys()
# TODO сделать кастомизацию для path_to_save()