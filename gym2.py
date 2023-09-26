# gym_2

import time
import pyautogui


# Function to press and hold a key, then release it
def press_key(key, delay=1):
    pyautogui.keyDown(key)  # hold duration
    pyautogui.keyUp(key)
    time.sleep(delay)  # delay between each key press


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
    # for _ in range(5):
    #     press_key('s')
    # turn('d')
    # for _ in range(15):
    #     press_key('d')
    # turn('w')
    # for _ in range(4):
    #     press_key('w')
    # turn('d')
    # for _ in range(4):
    #     press_key('d')
    # turn('w', 5)
    # for _ in range(6):
    #     press_key('w')
    # press_key('f', 2)
    # press_key('f', 2)
    # press_key('f', 2)
    # press_key('f', 7)
    # press_key('f', 2)
    # press_key('f', 3)
    # press_key('f')
    # turn('s')
    # for _ in range(6):
    #     press_key('s')
    # time.sleep(5)  # outside of poke center
    # press_key('x')
    # press_key('f')
    # for _ in range(4):
    #     press_key('d')
    # press_key('s')
    # press_key('s')
    # for _ in range(10):
    #     press_key('f')
    # time.sleep(3)
    # press_key('s')
    # press_key('f', 2)
    # press_key('f')
    # press_key('f')
    # press_key('f')
    # press_key('f')
    # press_key('f', 6)
    # for _ in range(3):
    #     press_key('r', 2)  # learnt rock smash
    turn('a')
    for _ in range(4):
        press_key('a')
    turn('s')
    for _ in range(4):
        press_key('s')
    turn('a')
    for _ in range(17):
        press_key('a')
    turn('w')
    turn('a')
    for _ in range(11):
        press_key('a')
    turn('w')
    for _ in range(11):
        press_key('w')
    turn('a')
    for _ in range(5):
        press_key('a')
    time.sleep(4)
    for _ in range(10):
        press_key('f', 2)
    time.sleep(4)
    for _ in range(4):
        press_key('a')  # enter cave
    time.sleep(4)
    grass_cycle_left()
    grass_cycle_left()
    for _ in range(3):
        grass_cycle_up()
    for _ in range(3):
        grass_cycle_left()
    for _ in range(5):
        grass_cycle_down()
    for _ in range(6):
        grass_cycle_left()
    for _ in range(3):
        grass_cycle_down()
    for _ in range(3):
        grass_cycle_left()
    for _ in range(5):
        grass_cycle_up()
    for _ in range(13):
        grass_cycle_left()
    press_key('a', 4)
    for _ in range(6):
        press_key('a')
    time.sleep(4)
    press_key('f', 14)
    press_key('s')
    press_key('w')
    press_key('f')
    press_key('s')
    press_key('f, 24')
    turn('s')
    for _ in range(3):
        press_key('s')
    turn('a')
    turn('s')
    press_key('s', 2)
    turn('a')
    for _ in range(11):
        press_key('a')
    grass_cycle_left()
    grass_cycle_left()
    grass_cycle_left()
    press_key('a')
    turn('s')
    press_key('s')
    turn('a')
    press_key('a')
    press_key('a')
    grass_cycle_left()
    grass_cycle_left()
    for _ in range(30):
        press_key('a')
    time.sleep(3)


# Execute the main function
if __name__ == "__main__":
    main()
