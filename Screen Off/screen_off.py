import ctypes
import time

def screen_off(delay):
        timer = delay
        while timer > 0:
            print(f'Countdown: {timer}...')
            time.sleep(1)
            timer -= 1
        return ctypes.windll.user32.SendMessageW(65535, 274, 61808, 2)

screen_off(5)