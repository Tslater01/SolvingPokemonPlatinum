# gym_3  
import t
import pyautogui


# Function to press and hold a key, then release it
def press_key(key, delay=1):
    pyautogui.keyDown(key)  # hold duration
    pyautogui.keyUp(key)
    time.sleep(delay)  # delay between each keyDown keyUp press


def turn(key, delay=1):
    pyautogui.keyDown(key)
    time.sleep(0.25)
    pyautogui.keyUp(key)
    time.sleep(delay)  # delay between each turn


def grass_cycle_right():
    time.sleep(1)
    press_key('d', 17)
    press_key('x')
    press_key('a')
    press_key('d')
    press_key('x')
    press_key('f', 7)


def grass_cycle_left():
    time.sleep(1)
    press_key('a', 17)
    press_key('x')
    press_key('a')
    press_key('d')
    press_key('x')
    press_key('f', 7)


def grass_cycle_up():
    time.sleep(1)
    press_key('w', 17)
    press_key('x')
    press_key('a')
    press_key('d')
    press_key('x')
    press_key('f', 7)


def grass_cycle_down():
    time.sleep(1)
    press_key('s', 17)
    press_key('x')
    press_key('a')
    press_key('d')
    press_key('x')
    press_key('f', 7)


def main():
    time.sleep(2)
    turn (a)
