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


# start of Gym 1 Script
def main():
    time.sleep(2)
    # press_key('f', 3)
    # press_key('f', 5)
    # press_key('x')
    # press_key('s')
    # press_key('s')
    # press_key('s')
    # press_key('f', 1)
    # press_key('d')
    # press_key('s')
    # press_key('s')
    # press_key('s')
    # press_key('s')
    # press_key('s')
    # press_key('s')
    # press_key('f', 1)
    # press_key('f', 2)
    # press_key('s')
    # press_key('f')
    # press_key('w', 3)
    # press_key('f', 2)
    # press_key('f')
    # press_key('f')
    # press_key('f')
    # press_key('f', 4)
    # press_key('f')
    # press_key('f', 2)
    # press_key('f', 2)
    # press_key('f', 2)
    # press_key('f', 3)
    # press_key('d')
    # press_key('d')
    # turn('w')
    # turn('d')
    # press_key('d')
    # press_key('d', 7)
    # press_key('f', 2)
    # press_key('f', 2)
    # press_key('f', 4)
    # for _ in range(7):
    #     press_key('s')
    # turn('a')
    # press_key('a')
    # press_key('a')
    # press_key('a')
    # press_key('f')
    # press_key('f')
    # press_key('f', 2)
    # press_key('f')
    # turn('s', 4)  # Exit House
    # turn('a')
    # for _ in range(6):
    #     press_key('a')
    # turn('w')
    # for _ in range(9):
    #     press_key('w')
    # turn('a')
    # press_key('a')
    # press_key('a')
    # press_key('a', 2)
    # press_key('f', 3)
    # press_key('f')
    # press_key('f', 2)
    # press_key('f', 4)
    # press_key('f', 6)
    # press_key('w')
    # press_key('w', 4)
    # turn('a')
    # press_key('a')
    # press_key('a')
    # press_key('a')
    # press_key('a')
    # for _ in range(9):
    #     press_key('w')
    # turn('d', 2)
    # press_key('f', 2)
    # press_key('f', 3)
    # press_key('f', 2)
    # press_key('f', 3)
    # press_key('w')
    # turn('a', 4)
    # for _ in range(8):
    #     press_key('s')
    # turn('d')
    # press_key('d')
    # press_key('d')
    # press_key('d')
    # turn('s', 4)
    # turn('d')
    # for _ in range(4):
    #     press_key('d')
    # for _ in range(21):
    #     press_key('w')
    # for _ in range(88):
    #     press_key('f', 2)
    # press_key('a')
    # press_key('a')
    # press_key('f', 2)
    # press_key('f', 2)
    # press_key('f', 2)
    # press_key('f')
    # press_key('d')
    # press_key('f')  # hover over "yes" for choosing chimchar
    # press_key('f', 4)  # selects chimchar
    # press_key('f', 2)
    # press_key('f')
    # press_key('f', 2)
    # press_key('f')
    # press_key('f', 2)
    # press_key('f', 2)
    # press_key('f')
    # press_key('f', 5)
    # press_key('f')
    # press_key('f', 4)
    # press_key('f')
    # press_key('f', 5)
    # press_key('f', 2)
    # press_key('f')
    # press_key('f')
    # press_key('f')
    # press_key('f')
    # press_key('f', 13)
    # press_key('f')
    # press_key('f')
    # press_key('f')
    # press_key('d')
    # press_key('f')
    # press_key('f', 10)
    # press_key('f')
    # press_key('f')
    # press_key('a')
    # press_key('f')
    # press_key('f', 10)
    # press_key('f')
    # press_key('f')
    # press_key('f', 10)
    # press_key('f')
    # press_key('f')
    # press_key('f', 10)
    # press_key('f')
    # press_key('f')
    # press_key('f', 10)
    # press_key('f')
    # press_key('f')
    # press_key('f', 10)
    # press_key('f')
    # press_key('f')
    # press_key('f', 10)
    # press_key('f')
    # press_key('f')
    # press_key('f', 10)
    # press_key('f')
    # press_key('f')
    # press_key('f', 10)  # knocks piplup out
    # press_key('f')
    # press_key('f')
    # press_key('f', 10)
    # press_key('f', 5)
    # press_key('f', 2)
    # press_key('f', 2)
    # press_key('f', 5)
    # press_key('f')
    # press_key('f')
    # press_key('f')
    # press_key('f', 13)
    # press_key('f')
    # for _ in range(19):
    #     press_key('f', 2)
    # press_key('a', 2)
    # press_key('a', 2)
    # press_key('a', 2)
    # press_key('f', 2)
    # press_key('a', 2)
    # press_key('a', 2)
    # press_key('a', 2)
    # press_key('f', 2)
    # press_key('a', 2)
    # press_key('a', 2)
    # press_key('a', 2)
    # press_key('f', 2)
    # press_key('a', 2)
    # press_key('a', 2)
    # press_key('a', 2)
    # press_key('f', 2)
    # press_key('a', 2)
    # press_key('a', 2)
    # press_key('a', 2)
    # press_key('f', 2)
    # turn('s')
    # press_key('s')
    # turn('d')
    # turn('s', 4)  # exit house after rival battle
    # turn('a')
    # press_key('a')
    # press_key('a')
    # turn('w')
    # for _ in range(28):
    #     press_key('w')
    # for _ in range(9):
    #     press_key('f', 2)
    # press_key('w')
    # press_key('w')
    # turn('a')
    # for _ in range(30):
    #     press_key('a')
    # turn('w')
    # for _ in range(8):
    #     press_key('w')
    # turn('a')
    # turn('w')
    # press_key('w', 2)
    # for _ in range(34):
    #     press_key('f', 2)
    # press_key('s')
    # press_key('s', 4)
    # for _ in range(10):
    #     press_key('s')
    # turn('d')
    # for _ in range(33):
    #     press_key('d')
    # turn('w')
    # turn('d')  # start first grass_cycle
    # for _ in range(11):
    #     grass_cycle_right()
    # for _ in range(20):
    #     press_key('d')
    # turn('s')
    # turn('w')
    # for _ in range(7):
    #     grass_cycle_up()
    # for _ in range(4):
    #     grass_cycle_right()
    # turn('w')
    # press_key('w')
    # press_key('w')
    # turn('d')
    # for _ in range(11):
    #     press_key('d')
    # turn('s')
    # press_key('s')
    # press_key('s')
    # turn('d')
    # for _ in range(4):
    #     press_key('d')
    # press_key('d', 4)
    # for _ in range(14):
    #     press_key('f', 2)
    # time.sleep(10)
    # for _ in range(7):
    #     press_key('f', 2)
    # press_key('s')
    # for _ in range(48):
    #     press_key('f', 2)
    # time.sleep(4)
    # for _ in range(10):
    #     press_key('s')  # outside of lab
    # time.sleep(4)
    # for _ in range(18):
    #     press_key('f', 2)
    # for _ in range(4):
    #     press_key('f')
    # for _ in range(26):
    #     press_key('f')  # save 6, outside of poke mart
    # time.sleep(3)
    # turn('w')
    # press_key('w', 4)
    # for _ in range(4):
    #     press_key('w')
    # press_key('f', 2)
    # press_key('f', 2)
    # press_key('s', 2)
    # press_key('f', 2)
    # for _ in range(3):
    #     press_key('s')
    # press_key('f', 2)
    # press_key('f')
    # press_key('f')
    # press_key('f')
    # press_key('s')
    # press_key('s')
    # press_key('s')
    # press_key('f', 2)
    # press_key('s')
    # press_key('s')
    # press_key('f')
    # press_key('f')
    # time.sleep(3)
    # turn('s')
    # for _ in range(4):
    #     press_key('s')
    # time.sleep(3)
    # press_key('s')
    # turn('a')
    # for _ in range(34):
    #     press_key('a')
    # turn('s')
    # for _ in range(6):
    #     press_key('s')
    # turn('a')
    # for _ in range(23):
    #     press_key('a')
    # turn('w')
    # press_key('w')
    # turn('a')
    # for _ in range(14):
    #     press_key('a')
    # turn('s')
    # for _ in range(34):
    #     press_key('s')
    # turn('d')
    # press_key('d')
    # press_key('d')
    # turn('w', 4)  # enter home
    # press_key('w')
    # press_key('w')
    # press_key('d')
    # for _ in range(42):
    #     press_key('f', 2)
    # press_key('s')
    # press_key('s')
    # press_key('s', 4)  # outside of moms house
    # turn('a')
    # press_key('a')
    # press_key('a')
    # turn('w')
    # for _ in range(33):
    #     press_key('w')
    # turn('d')
    # press_key('d')
    # for _ in range(11):
    #     grass_cycle_right()
    # for _ in range(20):
    #     press_key('d')
    # turn('s')
    # turn('w')
    # for _ in range(7):
    #     grass_cycle_up()
    # for _ in range(4):
    #     grass_cycle_right()
    # turn('w')
    # press_key('w')
    # press_key('w')
    # turn('d')
    # for _ in range(11):
    #     press_key('d')
    # turn('s')
    # press_key('s')
    # press_key('s')
    # turn('d')
    # for _ in range(24):
    #     press_key('d')
    # turn('w')
    # for _ in range(18):
    #     press_key('w')
    # turn('a')
    # for _ in range(3):
    #     press_key('a')
    # for _ in range(5):
    #     press_key('f', 2)
    # time.sleep(60)
    # for _ in range(18):
    #     press_key('f', 2)  # dawn tutorial ends
    # time.sleep(5)
    # for _ in range(5):
    #     grass_cycle_left()
    # for _ in range(5):
    #     press_key('a')
    # for _ in range(4):
    #     grass_cycle_left()
    # for _ in range(9):
    #     grass_cycle_up()
    # for _ in range(5):
    #     press_key('w')
    # turn('d')
    # press_key('d', 5)  # first trainer
    # press_key('f', 16)
    # press_key('f')
    # press_key('f')
    # press_key('f', 16)  # scratch
    # press_key('f')
    # press_key('f', 16)  # scratch
    # press_key('a')
    # press_key('f', 2)
    # press_key('f', 2)
    # press_key('f', 2)
    # press_key('f', 2)  # possible potion #1
    # press_key('f')
    # press_key('s')
    # press_key('s')
    # press_key('d')
    # press_key('f')
    # press_key('w')
    # press_key('f')
    # press_key('f', 8)
    # press_key('w')
    # press_key('f')
    # press_key('f', 14)
    # press_key('a')
    # press_key('f', 2)
    # press_key('f', 2)
    # press_key('f', 2)
    # press_key('f', 2)  # possible potion #2
    # press_key('f')
    # press_key('s')
    # press_key('s')
    # press_key('d')
    # press_key('f')
    # press_key('w')
    # press_key('f')
    # press_key('f', 8)
    # press_key('w')
    # press_key('f')
    # press_key('f', 14)
    # press_key('a')
    # press_key('f', 2)
    # press_key('f', 2)
    # press_key('f', 2)
    # press_key('f', 2)  # possible potion #3
    # press_key('f')
    # press_key('s')
    # press_key('s')
    # press_key('d')
    # press_key('f')
    # press_key('w')
    # press_key('f')
    # press_key('f', 8)
    # press_key('w')
    # press_key('f')
    # press_key('f', 14)
    # press_key('a')
    # press_key('f', 2)
    # press_key('f', 2)
    # press_key('f', 2)
    # press_key('f', 2)  # possible potion #4
    # press_key('f')
    # press_key('s')
    # press_key('s')
    # press_key('d')
    # press_key('f')
    # press_key('w')
    # press_key('f')
    # press_key('f', 8)
    # press_key('w')
    # press_key('f')
    # press_key('f', 14)
    # press_key('a')
    # press_key('f', 2)
    # press_key('f', 2)
    # press_key('f', 2)
    # press_key('f', 2)  # possible potion #5
    # press_key('f')
    # press_key('s')
    # press_key('s')
    # press_key('d')
    # press_key('f')
    # press_key('w')
    # press_key('f')
    # press_key('f', 8)
    # press_key('w')
    # press_key('f')
    # press_key('f', 14)
    # press_key('a')
    # press_key('f', 2)
    # press_key('f', 2)
    # press_key('f', 2)
    # press_key('f', 2)  # possible potion #6
    # press_key('f')
    # press_key('s')
    # press_key('s')
    # press_key('d')
    # press_key('f')
    # press_key('w')
    # press_key('f')
    # press_key('f', 8)
    # press_key('w')
    # press_key('f')
    # press_key('f', 14)
    # press_key('a')
    # press_key('f', 2)
    # press_key('f', 2)
    # press_key('f', 2)
    # press_key('f', 2)  # possible potion #7
    # press_key('f')
    # press_key('s')
    # press_key('s')
    # press_key('d')
    # press_key('f')
    # press_key('w')
    # press_key('f')
    # press_key('f', 8)
    # press_key('w')
    # press_key('f')
    # press_key('f', 14)
    # press_key('f', 2)
    # press_key('f', 2)
    # press_key('f', 2)
    # for _ in range(13):
    #     press_key('d')
    # press_key('w')
    # turn('d')
    # press_key('d')
    # press_key('d')
    # turn('w')
    # press_key('w')
    # press_key('f')
    # for _ in range(13):
    #     press_key('d')
    # press_key('w')
    # turn('d')
    # press_key('d')
    # press_key('d')
    # turn('w')
    # press_key('w')
    # press_key('f')
    # for _ in range(13):
    #     press_key('d')
    # press_key('w')
    # turn('d')
    # press_key('d')
    # press_key('d')
    # turn('w')
    # press_key('w')  # tree corner after first trainer
    # turn('s')
    # for _ in range(8):
    #     press_key('s')
    # turn('a')
    # press_key('a')
    # press_key('a')
    # press_key('a')
    # turn('s')
    # press_key('s')
    # turn('d')
    # for _ in range(6):
    #     grass_cycle_right()
    # for _ in range(4):
    #     press_key('d')
    # turn('s')
    # turn('d')
    # press_key('d')
    # turn('s')
    # for _ in range(16):
    #     press_key('s')
    # turn('a')
    # for _ in range(6):
    #     press_key('a')
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
    # time.sleep(5)
    # turn('d')
    # for _ in range(6):
    #     press_key('d')
    # turn('w')
    # for _ in range(16):
    #     press_key('w')
    # turn('a')
    # for _ in range(3):
    #     press_key('a')
    # for _ in range(6):
    #     grass_cycle_left()
    # for _ in range(6):
    #     press_key('a')
    # for _ in range(4):
    #     grass_cycle_left()
    # for _ in range(9):
    #     grass_cycle_up()
    # for _ in range(6):
    #     press_key('w')
    # turn('d')
    # for _ in range(11):
    #     press_key('d')
    # turn('s')
    # for _ in range(4):
    #     press_key('s')
    # turn('d')
    # for _ in range(3):
    #     press_key('d')
    # press_key('d', 4)  # second trainer route 202
    # press_key('f', 2)
    # press_key('f', 15)
    # press_key('f')
    # press_key('f')
    # press_key('f', 12)
    # press_key('f')
    # press_key('f', 12)
    # press_key('f')
    # press_key('f', 12)
    # press_key('a')
    # press_key('a')
    # press_key('f', 2)
    # press_key('f', 2)
    # press_key('f', 2)
    # press_key('f', 2)
    # press_key('f', 14)
    # press_key('w')
    # press_key('f')
    # press_key('f', 12)
    # press_key('f')
    # press_key('f', 12)
    # press_key('f')
    # press_key('f', 20)
    # for _ in range(5):
    #     press_key('f', 2)
    # turn('s')
    # press_key('f')
    # turn('s')
    # for _ in range(11):
    #     press_key('s')  # almost in tree corner but not quite
    # turn('d')
    # press_key('d')
    # press_key('d')
    # turn('s')
    # for _ in range(11):
    #     press_key('s')
    # turn('a')
    # for _ in range(6):
    #     press_key('a')
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
    # time.sleep(5)
    # turn('d')
    # for _ in range(6):
    #     press_key('d')
    # turn('w')
    # for _ in range(16):
    #     press_key('w')
    # turn('a')
    # for _ in range(3):
    #     press_key('a')
    # for _ in range(6):
    #     grass_cycle_left()
    # for _ in range(6):
    #     press_key('a')
    # for _ in range(4):
    #     grass_cycle_left()
    # for _ in range(9):
    #     grass_cycle_up()
    # for _ in range(6):
    #     press_key('w')
    # turn('d')
    # for _ in range(11):
    #     press_key('d')
    # turn('s')
    # for _ in range(4):
    #     press_key('s')
    # turn('d')
    # for _ in range(5):
    #     press_key('d')
    # turn('w')
    # for _ in range(7):
    #     grass_cycle_up()
    # for _ in range(6):
    #     grass_cycle_right()
    # grass_cycle_up()
    # grass_cycle_up()
    # for _ in range(7):
    #     press_key('w')
    # for _ in range(3):
    #     press_key('d')  # top right tree corner
    # turn('s')
    # turn('a')
    # press_key('a')
    # press_key('a')  # third trainer route 202
    # press_key('a', 5)
    # press_key('f', 16)
    # press_key('f')
    # press_key('s')
    # press_key('f', 16)
    # press_key('f')
    # press_key('f', 20)
    # press_key('f', 2)
    # press_key('f', 2)
    # press_key('f', 2)
    # press_key('f', 2)
    # press_key('f', 2)
    # press_key('f', 2)
    # turn('d')
    # press_key('d')
    # press_key('d')
    # press_key('d')
    # turn('w')  # top right tree corner
    # turn('s')
    # turn('a')
    # for _ in range(4):
    #     press_key('a')
    # for _ in range(5):
    #     grass_cycle_left()
    # for _ in range(10):
    #     press_key('a')
    # turn('s')
    # turn('a')
    # for _ in range(5):
    #     grass_cycle_left()
    # time.sleep(3)
    # press_key('f', 2)
    # press_key('f', 2)
    # press_key('f', 2)
    # for _ in range(5):
    #     grass_cycle_right()
    # turn('w')
    # press_key('w')
    # press_key('w')
    # turn('d')
    # for _ in range(6):
    #     press_key('d')
    # turn('a')
    # turn('w')
    # for _ in range(7):
    #     press_key('w')
    # time.sleep(6)  # Dawn walks up @ Jubilife
    # for _ in range(55):
    #     press_key('f', 2)
    # turn('a')
    # for _ in range(3):
    #     press_key('a')
    # turn('s')
    # press_key('s')
    # turn('a')
    # for _ in range(3):
    #     press_key('a')
    # turn('w', 4)
    # for _ in range(6):
    #     press_key('w')
    # turn('a')
    # for _ in range(3):
    #     press_key('a')
    # turn('w')
    # turn('a')
    # for _ in range(3):
    #     press_key('f', 2)
    # turn('d')
    # turn('s')
    # turn('d')
    # press_key('d')
    # press_key('d')
    # turn('w')
    # for _ in range(23):
    #     press_key('f', 2)
    # for _ in range(8):
    #     press_key('s')
    # turn('d')
    # turn('s', 4)  # leaving trainer school
    turn('d')
    for _ in range(5):
        press_key('d')
    turn('w', 5)
    for _ in range(8):
        press_key('f', 2)
    turn('d')
    turn('w')
    for _ in range(7):
        press_key('w')
    turn('d')
    for _ in range(4):
        press_key('d')
    turn('s')
    turn('d')
    for _ in range(20):
        press_key('d', 2)
    for _ in range(9):
        press_key('f', 2)


# Execute the main function
if __name__ == "__main__":
    main()
