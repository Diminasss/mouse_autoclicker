import pyautogui
import time
import keyboard
import threading
import os


class AutoClicker:
    def __init__(self):
        self.stop_auto_clicker = False
        self.step_time = None

    def auto_clicker(self):
        while not self.stop_auto_clicker:
            x, y = pyautogui.position()
            pyautogui.click(x, y)
            time.sleep(self.step_time)

    def keyboard_handler(self):
        print("\nПрограмма остановлена пользователем.")
        self.stop_auto_clicker = True
        time.sleep(2)
        os._exit(0)

    def start(self):
        try:
            self.step_time = float(input("Введите время между кликами в секундах (можно целые и дробные, например, 0.1) и нажмите Enter для запуска кликера: "))
        except ValueError:
            raise Exception("В качестве времени между кликами можно использовать только целые и дробные числа")
        threading.Thread(target=self.auto_clicker).start()
        print("Автокликер запущен. Нажмите Ctrl+B, чтобы остановить.")

        keyboard.add_hotkey('ctrl+b', self.keyboard_handler)
        keyboard.wait()


if __name__ == "__main__":
    clicker = AutoClicker()
    clicker.start()
