#! python3
# hotScreenshot.py - программа, позволяющая делать моментальный скрин и сохранять его в удобном для пользователя месте

import castomisation_hotScreenshot #Мой набор персональных кастомизаций
import pyautogui
import keyboard
import datetime
import time
import os


class Screenshot:
    def __init__(self):
        pass

    def path_to_save(self, path='Desktop', path_folder='ScreenShots'):
        '''
        :paran path: - указывает где должна находиться папка со скриншотами
        :param path_folder: - название папки со скриншотами

        Функция предназначена для получения пути сохранения файла
        '''
        fullPath = os.path.expanduser('~\\' + path + '\\' + path_folder)
        os.makedirs(fullPath, exist_ok=True)
        return str(fullPath)

    def take_screenshot_by_keys(self, first_key='ctrl', second_key='`'):
        '''
        :param first_key: первая кнопка для комбинации
        :param second_key: вторая кнопка для комбинации

        Функция для установки комбинации клавиш
        '''
        try:
            while True:
                time.sleep(.05) #приостанавливает цикл для экономии циклов процессора
                if keyboard.is_pressed(first_key + '+' + second_key):
                    self.save_screenshot()
                    print('Сделан скриншот: ' + str(self.name_screenshot()))
                    time.sleep(1) # Выжидает 1 секнду для успешного сохранения скриншота
                    continue
        except KeyboardInterrupt:
            return print('Все скриншоты сохранены по этому пути: ' + self.path_to_save())

    def save_screenshot(self):
        '''
        Функция для сохранения в указанном пути
        '''
        my_screen = pyautogui.screenshot()
        my_screen.save(self.name_screenshot())
        # return os.path.basename(save_shot)

    def name_screenshot(self, name='Screenshot', time_now=''):
        time_now = time.time()
        # print(self.path_to_save() + '\\' + name + str(round(time_now)) + '.png')
        return self.path_to_save() + '\\' + name + str(round(time_now)) + '.png'

Screenshot().take_screenshot_by_keys()
