# gym_2

import tim
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
    for _ in range(5):
        press_key('s')
    turn('d')
    for _ in range(15):
        press_key('d')
    turn('w')
    for _ in range(4):
        press_key('w')
    turn('d')
    for _ in range(4):
        press_key('d')
    turn('w', 5)
    for _ in range(6):
        press_key('w')
    press_key('f', 2)
    press_key('f', 2)
    press_key('f', 2)
    press_key('f', 7)
    press_key('f', 2)
    press_key('f', 3)
    press_key('f')
    turn('s')
    for _ in range(6):
        press_key('s')
    time.sleep(5)  # outside of poke center
    press_key('x')
    press_key('f')
    for _ in range(4):
        press_key('d')
    press_key('s')
    press_key('s')
    for _ in range(10):
        press_key('f')
    time.sleep(3)
    press_key('s')
    press_key('f', 2)
    press_key('f')
    press_key('f')
    press_key('f')
    press_key('f')
    press_key('f', 6)
    for _ in range(3):
        press_key('r', 2)  # learnt rock smash
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
    for _ in range(6):
        press_key('f', 2)
    for _ in range(12):
        press_key('a')
    turn('w')
    for _ in range(12):
        press_key('w')
    turn('a')
    turn('w')
    press_key('w', 2)
    press_key('f')
    for _ in range(27):
        press_key('f', 2)
    time.sleep(16)  # enter double battle against team galactic
    press_key('s')
    press_key('w')
    press_key('f')
    press_key('s')
    press_key('f')
    press_key('f', 30)
    press_key('f')
    press_key('f')
    press_key('d')
    press_key('f', 34)
    for _ in range(40):
        press_key('f', 2)
    turn('w')
    for _ in range(14):
        press_key('w')
    turn('a')
    press_key('a')
    press_key('w')
    press_key('f', 2)
    press_key('f', 14)
    press_key('s')
    press_key('w')
    press_key('f')
    press_key('s')
    press_key('f', 24)  # defeated the lass
    turn('d')
    turn('w')
    press_key('w')
    press_key('w')
    turn('a')
    for _ in range(4):
        press_key('a')
    turn('w')
    press_key('a', 4)
    press_key('f')
    press_key('f', 14)
    press_key('s')
    press_key('w')
    press_key('f')
    press_key('d')
    press_key('f', 24)  # defeated youngster tyler
    turn('d')
    press_key('d')
    press_key('d')
    turn('s')
    turn('w')
    for _ in range(4):
        grass_cycle_up()
    press_key('w', 5)
    press_key('f')
    press_key('f', 15)
    press_key('s')
    press_key('w')
    press_key('f')
    press_key('s')
    press_key('f', 25)  # defeated lass samantha
    for _ in range(3):
        grass_cycle_right()
    for _ in range(9):
        grass_cycle_up()
    press_key('w')
    turn('a')
    press_key('a')
    turn('w')
    press_key('w')  # save before cavern
    press_key('w', 4)
    for _ in range(6):
        grass_cycle_up()
    for _ in range(3):
        grass_cycle_right()
    press_key('f', 2)
    press_key('f')
    grass_cycle_right()
    press_key('f', 2)
    press_key('f')
    press_key('f', 4)
    for _ in range(6):
        grass_cycle_right()
    turn('s', 5)
    turn('a')
    for _ in range(7):
        press_key('a')
    turn('w')
    for _ in range(6):
        press_key('w')
    turn('d')
    for _ in range(3):
        press_key('d')
    press_key('f', 2)
    press_key('f', 15)
    press_key('s')
    press_key('w')
    press_key('f')
    press_key('s')
    press_key('f, 16')
    press_key('f')
    press_key('f', 25)  # defeat aroma lady taylor
    turn('s')
    turn('d')
    for _ in range(2):
        press_key('d')
    turn('w')
    for _ in range(6):
        grass_cycle_up()
    press_key('w')
    press_key('d')
    press_key('w', 3)
    press_key('f', 14)
    press_key('w')
    press_key('f')
    press_key('s')
    press_key('f', 24)
    press_key('f')
    press_key('f', 32)
    turn('a')
    for _ in range(9):
        press_key('a')
    turn('w')
    for _ in range(3):
        press_key('w')
    for _ in range(4):
        grass_cycle_up()
    for _ in range(10):
        press_key('w')
    turn('d')
    for _ in range(5):
        press_key('d')
    turn('w', 5)
    for _ in range(6):
        press_key('w')
    for _ in range(3):
        press_key('f', 2)
    press_key('f', 7)
    press_key('f', 2)
    press_key('f', 3)
    press_key('f')
    turn('s')
    for _ in range(6):
        press_key('s')
    time.sleep(5)  # outside of poke center
    turn('d')
    for _ in range(12):
        press_key('d')
    turn('w')
    for _ in range(5):
        press_key('w')
    turn('d')
    for _ in range(20):
        press_key('d')  # looking at girl
    for _ in range(5):
        press_key('f', 2)
    turn('a')
    for _ in range(29):
        press_key('a')
    turn('w')
    turn('a')
    for _ in range(5):
        press_key('a')
    turn('w')
    for _ in range(17):
        press_key('w')
    turn('a')
    for _ in range(10):
        press_key('a')
    turn('w', 4)
    for _ in range(6):
        press_key('w')
    for _ in range(8):
        press_key('f', 2)
    time.sleep(14)
    press_key('w')
    press_key('f')
    press_key('s')
    press_key('f', 18)
    press_key('r')
    press_key('r', 10)
    for _ in range(3):
        press_key('f', 2)
    time.sleep(14)
    press_key('w')
    press_key('f')
    press_key('s')
    press_key('f', 20)
    time.sleep(14)
    press_key('w')
    press_key('f')
    press_key('s')
    press_key('f', 20)
    for _ in range(41):
        press_key('f', 2)
    turn('s')
    for _ in range(6):
        press_key('s')
    time.sleep(4)
    turn('d')
    for _ in range(23):
        press_key('d')
    turn('s')
    for _ in range(16):
        press_key('s')
    turn('d')
    for _ in range(26):
        press_key('d')
    turn('s')
    turn('d')
    for _ in range(8):
        press_key('d')
    turn('s')
    press_key('s')
    turn('d')
    for _ in range(18):
        press_key('d')
    turn('w')
    for _ in range(5):
        press_key('w')
    turn('d')
    press_key('w')  # in front of windmill guard
    for _ in range(5):
        press_key('f', 2)
    time.sleep(14)
    press_key('w')
    press_key('f')
    press_key('s')
    press_key('f', 26)
    for _ in range(7):
        press_key('f', 2)
    press_key('w')
    for _ in range(4):
        press_key('f', 2)
    press_key('w', 6)
    for _ in range(5):
        press_key('f', 2)
    for _ in range(10):
        press_key('a')
    turn('w')
    for _ in range(7):
        press_key('w')
    time.sleep(6)
    press_key('f', 14)
    press_key('w')
    press_key('f')
    press_key('f', 22)
    turn('w')
    turn('d')
    for _ in range(5):
        press_key('d')
    turn('s')
    turn('d')
    for _ in range(7):
        press_key('d')
    turn('w')
    turn('d')
    press_key('d')
    press_key('d', 3)
    for _ in range(9):
        press_key('f', 2)
    time.sleep(14)
    press_key('w')
    press_key('f')
    press_key('s')
    press_key('f', 22)
    press_key('f')
    press_key('w')
    press_key('d')
    press_key('f', 8)
    press_key('f')
    press_key('f', 25)
    for _ in range(26):
        press_key('f', 2)
    turn('a')  # post mars
    for _ in range(5):
        press_key('a')
    turn('s')
    turn('a')
    for _ in range(7):
        press_key('a')
    turn('w')
    turn('a')
    press_key('a')
    turn('s')
    for _ in range(8):
        press_key('s')
    turn('d')
    for _ in range(8):
        press_key('d')
    turn('s', 7)
    for _ in range(14):
        press_key('f', 2)
    for _ in range(3):
        press_key('s')
    turn('a')
    turn('s')
    press_key('s')
    press_key('s')
    turn('a')
    for _ in range(24):
        press_key('a')
    turn('w')
    for _ in range(8):
        press_key('w')
    turn('a')
    press_key('a')
    press_key('a')
    turn('w')
    press_key('w')
    for _ in range(9):
        grass_cycle_up()
    for _ in range(9):
        grass_cycle_left()
    turn('w')
    for _ in range(3):
        press_key('w')
    turn('d')
    press_key('d')
    press_key('d')
    turn('w')
    press_key('d')
    press_key('f', 3)
    press_key('f', 14)
    press_key('w')
    press_key('f')
    press_key('d')
    press_key('f', 22)
    press_key('f')
    press_key('f', 22)
    press_key('f')
    press_key('f', 25)  # defeat hiker
    turn('w')
    for _ in range(4):
        press_key('w')
    turn('a')
    turn('w')
    for _ in range(3):
        press_key('w')
    time.sleep(10)
    press_key('f', 14)
    press_key('w')
    press_key('f')
    press_key('s')
    press_key('f', 25)
    turn('w')
    for _ in range(12):
        press_key('w')
    turn('a')
    turn('w')
    for _ in range(3):
        press_key('w')
    grass_cycle_up()
    grass_cycle_up()
    grass_cycle_right()
    grass_cycle_right()
    for _ in range(6):
        grass_cycle_up()
    press_key('w', 8)
    press_key('f', 14)
    press_key('w')
    press_key('f')
    press_key('s')
    press_key('f, 25')
    turn('w')
    turn('a')
    turn('w')
    for _ in range(20):
        press_key('w')  # eterna forest
    time.sleep(5)
    press_key('w', 5)
    for _ in range(10):
        press_key('f', 2)
    turn('d')
    press_key('d')
    turn('w')
    press_key('w')
    press_key('w')
    turn('a')
    turn('d')
    for _ in range(4):
        grass_cycle_right()
    for _ in range(8):
        grass_cycle_up()
    turn('d')
    for _ in range(3):
        press_key('d')
    turn('w')
    for _ in range(7):
        press_key('w')
    time.sleep(5)
    press_key('f', 4)
    press_key('f', 16)
    press_key('w')
    press_key('f')
    press_key('s')
    press_key('f')
    press_key('f', 20)
    press_key('r')
    press_key('r', 12)
    press_key('f')
    press_key('f')
    press_key('d')
    press_key('f', 25)
    press_key('f')
    press_key('f')
    press_key('f', 25)
    press_key('f')
    press_key('f')
    press_key('f', 35)  # won first double battle
    turn('w')
    turn('d')
    turn('w')
    for _ in range(7):
        press_key('w')
    turn('d')
    for _ in range(10):
        press_key('d')
    turn('s')
    for _ in range(8):
        press_key('s')
    time.sleep(3)
    for _ in range(6):
        press_key('f', 2)
    press_key('f', 16)
    press_key('w')
    press_key('f')
    press_key('s')
    press_key('f')
    press_key('f', 25)
    press_key('f')
    press_key('f')
    press_key('d')
    press_key('f', 25)
    turn('s')
    for _ in range(5):
        press_key('s')
    for _ in range(5):
        grass_cycle_down()
    for _ in range(15):
        grass_cycle_right()
    for _ in range(9):
        grass_cycle_up()
    for _ in range(5):
        press_key('w')
    turn('d')
    turn('w')
    press_key('w')
    turn('d')
    for _ in range(14):
        press_key('d')
    for _ in range(3):
        grass_cycle_right()
    for _ in range(10):
        grass_cycle_up()
    for _ in range(8):
        press_key('w')
    turn('a')
    for _ in range(5):
        press_key('a')
    grass_cycle_left()
    for _ in range(7):
        grass_cycle_up()
    press_key('w')
    press_key('w')
    press_key('w')
    turn('d')
    for _ in range(4):
        press_key('d')
    time.sleep(5)
    for _ in range(10):
        press_key('f', 2)
    for _ in range(5):
        press_key('d')
    time.sleep(5)  # route 205
    press_key('d')
    turn('s')
    for _ in range(4):
        press_key('s')
    turn('d')
    for _ in range(12):
        press_key('d')
    turn('s')
    press_key('s')
    press_key('s')
    turn('d')
    for _ in range(29):
        press_key('d')
    turn('s')
    for _ in range(26):
        press_key('s')
    turn('d')
    turn('s')
    for _ in range(3):
        press_key('s')
    turn('d')
    for _ in range(7):
        press_key('d')
    turn('w')
    for _ in range(8):
        press_key('f', 2)
    press_key('w')
    press_key('w', 5)  # enter gym_2
    for _ in range(5):
        press_key('w')
    turn('d')
    press_key('d')
    press_key('f', 2)
    press_key('f', 16)
    press_key('w')
    press_key('f')
    press_key('s')
    press_key('f', 25)
    press_key('f')
    press_key('f', 25)
    press_key('f', 2)
    press_key('f', 2)
    time.sleep(20)
    turn('a')
    press_key('a')
    turn('w')
    for _ in range(7):
        press_key('w')
    turn('d')
    for _ in range(8):
        press_key('d')
    turn('s')
    press_key('s')
    press_key('s')
    press_key('f', 2)
    press_key('f', 2)
    press_key('f', 14)
    press_key('w')
    press_key('f')
    press_key('s')
    press_key('f', 25)
    press_key('f')
    press_key('f', 25)
    press_key('f')
    press_key('f', 25)
    for _ in range(3):
        press_key('f', 2)
    time.sleep(10)
    press_key('f', 2)
    press_key('f', 2)
    turn('w')
    press_key('w')
    press_key('w')
    turn('a')
    for _ in range(16):
        press_key('a')
    turn('w')
    for _ in range(4):
        press_key('w')
    press_key('f', 2)
    press_key('f', 16)
    press_key('w')
    press_key('f')
    press_key('s')
    press_key('f', 25)
    press_key('r')
    press_key('r', 12)
    press_key('f', 2)
    press_key('f', 20)
    press_key('f', 2)
    press_key('f', 2)
    turn('s')
    for _ in range(4):
        press_key('s')
    turn('d')
    for _ in range(8):
        press_key('d')
    turn('w')
    for _ in range(7):
        press_key('w')
    for _ in range(6):
        press_key('f', 2)
    time.sleep(15)
    press_key('w')
    press_key('f')
    press_key('s')
    for _ in range(3):
        press_key('f')
        press_key('f', 25)
    for _ in range(15):
        press_key('f', 2)
    time.sleep(8)
    turn('s')
    for _ in range(22):
        press_key('s')
    time.sleep(5)  # gym_2 completed


# Execute the main function
if __name__ == "__main__":
    main()
