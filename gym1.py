import time
import pyautogui


# Function to press and hold a key, then release it
def press_key(key, delay=1):
    pyautogui.keyDown(key)  # hold duration
    pyautogui.keyUp(key)
    time.sleep(delay)  # delay between each key press


def grass_cycle_right():
    press_key('d', 13)
    press_key('x')
    press_key('a')
    press_key('d')
    press_key('x')
    press_key('f', 7)


def grass_cycle_left():
    press_key('a', 13)
    press_key('x')
    press_key('a')
    press_key('d')
    press_key('x')
    press_key('f', 7)


def grass_cycle_up():
    press_key('w', 13)
    press_key('x')
    press_key('a')
    press_key('d')
    press_key('x')
    press_key('f', 7)


def grass_cycle_down():
    press_key('s', 13)
    press_key('x')
    press_key('a')
    press_key('d')
    press_key('x')
    press_key('f', 7)


# start of Gym 1 Script
def main():
    time.sleep(2)
    press_key('f', 3)
    press_key('f', 5)
    press_key('x')
    press_key('s')
    press_key('s')
    press_key('s')
    press_key('f', 1)
    press_key('d')
    press_key('s')
    press_key('s')
    press_key('s')
    press_key('s')
    press_key('s')
    press_key('s')
    press_key('f', 1)
    press_key('f', 2)
    press_key('s')
    press_key('f')
    press_key('w', 3)
    press_key('f', 2)
    press_key('f', 1)
    press_key('f', 1)
    press_key('f', 1)
    press_key('f', 4)
    press_key('f', 1)
    press_key('f', 2)
    press_key('f', 2)
    press_key('f', 2)
    press_key('f', 3)
    press_key('d')
    press_key('d')
    press_key('w')
    press_key('w')
    press_key('d')
    press_key('d')
    press_key('d')
    press_key('d', 7)
    press_key('f', 2)
    press_key('f', 2)
    press_key('f', 4)
    press_key('s')
    press_key('s')
    press_key('s')
    press_key('s')
    press_key('s')
    press_key('s')
    press_key('s')
    press_key('a')
    press_key('a')
    press_key('a')
    press_key('a')
    press_key('a', 1)
    press_key('f', 1)
    press_key('f', 1)
    press_key('f', 2)
    press_key('f', 1)
    press_key('s')
    press_key('s', 3)  # Exit House
    press_key('a')
    press_key('a')
    press_key('a')
    press_key('a')
    press_key('a')
    press_key('a')
    press_key('a')
    press_key('a')
    press_key('w')
    press_key('w')
    press_key('w')
    press_key('w')
    press_key('w')
    press_key('w')
    press_key('w')
    press_key('w')
    press_key('w')
    press_key('w')
    press_key('w')
    press_key('a')
    press_key('a')
    press_key('a')
    press_key('a')
    press_key('a', 1)
    press_key('f', 3)
    press_key('f', 1)
    press_key('f', 2)
    press_key('f', 4)
    press_key('f', 2)
    press_key('w')
    press_key('w', 2)
    press_key('a')
    press_key('a')
    press_key('a')
    press_key('a')
    press_key('a')
    press_key('a')
    press_key('w')
    press_key('w')
    press_key('w')
    press_key('w')
    press_key('w')
    press_key('w')
    press_key('w')
    press_key('w')
    press_key('d')
    press_key('d', 2)
    press_key('f', 2)
    press_key('f', 3)
    press_key('f', 2)
    press_key('f', 3)
    press_key('w')
    press_key('a')
    press_key('a', 4)
    press_key('s')
    press_key('s')
    press_key('s')
    press_key('s')
    press_key('s')
    press_key('s')
    press_key('s')
    press_key('s')
    press_key('d')
    press_key('d')
    press_key('d')
    press_key('d')
    press_key('d')
    press_key('s')
    press_key('s', 3)
    press_key('d')
    press_key('d')
    press_key('d')
    press_key('d')
    press_key('d')
    press_key('d')
    press_key('w')
    press_key('w')
    press_key('w')
    press_key('w')
    press_key('w')
    press_key('w')
    press_key('w')
    press_key('w')
    press_key('w')
    press_key('w')
    press_key('w')
    press_key('w')
    press_key('w')
    press_key('w')
    press_key('w')
    press_key('w')
    press_key('w')
    press_key('w')
    press_key('w')
    press_key('w', 1)
    press_key('f', 3)
    press_key('f', 1)
    press_key('f', 3)
    press_key('f', 2)
    press_key('f', 1)
    press_key('f', 1)
    press_key('f', 1)
    press_key('f', 2)
    press_key('f', 2)
    press_key('f', 1)
    press_key('f', 2)
    press_key('f', 1)
    press_key('f', 1)
    press_key('f', 2)
    press_key('f', 1)
    press_key('f', 2)
    press_key('f', 2)
    press_key('f', 1)
    press_key('f', 1)
    press_key('f', 4)
    press_key('f', 2)
    press_key('f', 1)
    press_key('f', 1)
    press_key('f', 1)
    press_key('f', 1)
    press_key('f', 2)
    press_key('f', 2)
    press_key('f', 2)
    press_key('f', 2)
    press_key('f', 1)
    press_key('f', 2)
    press_key('f', 2)
    press_key('f', 1)
    press_key('f', 3)
    press_key('f', 1)
    press_key('f', 2)
    press_key('f', 1)
    press_key('f', 1)
    press_key('f', 1)
    press_key('f', 1)
    press_key('f', 2)
    press_key('f', 1)
    press_key('f', 2)
    press_key('f', 2)
    press_key('f', 2)
    press_key('f', 2)
    press_key('f', 2)
    press_key('f', 2)
    press_key('f', 1)
    press_key('f', 1)
    press_key('f', 1)
    press_key('f', 1)
    press_key('f', 2)
    press_key('f', 1)
    press_key('f', 2)
    press_key('f', 2)
    press_key('f', 2)
    press_key('f', 2)
    press_key('f', 2)
    press_key('f', 2)
    press_key('f', 2)
    press_key('f', 2)
    press_key('f', 2)
    press_key('f', 2)
    press_key('f', 2)
    press_key('f', 2)
    press_key('f', 2)
    press_key('f', 2)
    press_key('f', 2)
    press_key('f', 2)
    press_key('f', 2)
    press_key('f', 2)
    press_key('f', 2)
    press_key('f', 2)
    press_key('f', 2)
    press_key('f', 2)
    press_key('f', 2)
    press_key('f', 2)
    press_key('f', 2)
    press_key('f', 2)
    press_key('f', 2)
    press_key('f', 2)
    press_key('f', 2)
    press_key('f', 2)
    press_key('a')
    press_key('a')
    press_key('f', 2)
    press_key('f', 2)
    press_key('f', 2)
    press_key('f')
    press_key('d')
    press_key('f')  # hover over "yes" for choosing chimchar
    press_key('f', 4)  # selects chimchar
    press_key('f', 2)
    press_key('f')
    press_key('f', 2)
    press_key('f')
    press_key('f', 2)
    press_key('f', 2)
    press_key('f')
    press_key('f', 5)
    press_key('f')
    press_key('f', 4)
    press_key('f')
    press_key('f', 5)
    press_key('f', 2)
    press_key('f')
    press_key('f')
    press_key('f')
    press_key('f')
    press_key('f', 13)
    press_key('f')
    press_key('f')
    press_key('f')
    press_key('d')
    press_key('f')
    press_key('f', 10)
    press_key('f')
    press_key('f')
    press_key('a')
    press_key('f')
    press_key('f', 10)
    press_key('f')
    press_key('f')
    press_key('f', 10)
    press_key('f')
    press_key('f')
    press_key('f', 10)
    press_key('f')
    press_key('f')
    press_key('f', 10)
    press_key('f')
    press_key('f')
    press_key('f', 10)
    press_key('f')
    press_key('f')
    press_key('f', 10)
    press_key('f')
    press_key('f')
    press_key('f', 10)
    press_key('f')
    press_key('f')
    press_key('f', 10)  # knocks piplup out
    press_key('f')
    press_key('f')
    press_key('f', 10)
    press_key('f', 5)
    press_key('f', 2)
    press_key('f', 2)
    press_key('f', 5)
    press_key('f')
    press_key('f')
    press_key('f')
    press_key('f', 13)
    press_key('f')
    press_key('f', 2)
    press_key('f', 2)
    press_key('f', 2)
    press_key('f', 2)
    press_key('f', 2)
    press_key('f', 2)
    press_key('f', 2)
    press_key('f', 4)
    press_key('f', 2)
    press_key('f', 2)
    press_key('f', 2)
    press_key('f', 2)
    press_key('f', 2)
    press_key('f', 2)
    press_key('f', 2)
    press_key('f', 2)
    press_key('f', 2)
    press_key('f', 2)
    press_key('a', 2)
    press_key('a', 2)
    press_key('a', 2)
    press_key('f', 2)
    press_key('a', 2)
    press_key('a', 2)
    press_key('a', 2)
    press_key('f', 2)
    press_key('a', 2)
    press_key('a', 2)
    press_key('a', 2)
    press_key('f', 2)
    press_key('a', 2)
    press_key('a', 2)
    press_key('a', 2)
    press_key('f', 2)
    press_key('a', 2)
    press_key('a', 2)
    press_key('a', 2)
    press_key('f', 2)
    press_key('s')
    press_key('s')
    press_key('s')
    press_key('d')
    press_key('d')
    press_key('s')
    press_key('s', 3)  # exit house after rival battle
    press_key('a')
    press_key('a')
    press_key('a')
    press_key('a')
    press_key('w')
    press_key('w')
    press_key('w')
    press_key('w')
    press_key('w')
    press_key('w')
    press_key('w')
    press_key('w')
    press_key('w')
    press_key('w')
    press_key('w')
    press_key('w')
    press_key('w')
    press_key('w')
    press_key('w')
    press_key('w')
    press_key('w')
    press_key('w')
    press_key('w')
    press_key('w')
    press_key('w')
    press_key('w')
    press_key('w')
    press_key('w')
    press_key('w')
    press_key('w')
    press_key('w')
    press_key('w')
    press_key('w')
    press_key('w')
    press_key('f')
    press_key('f')
    press_key('f')
    press_key('f')
    press_key('f')
    press_key('f')
    press_key('f')
    press_key('f')
    press_key('w')
    press_key('w')
    press_key('a')
    press_key('a')
    press_key('a')
    press_key('a')
    press_key('a')
    press_key('a')
    press_key('a')
    press_key('a')
    press_key('a')
    press_key('a')
    press_key('a')
    press_key('a')
    press_key('a')
    press_key('a')
    press_key('a')
    press_key('a')
    press_key('a')
    press_key('a')
    press_key('a')
    press_key('a')
    press_key('a')
    press_key('a')
    press_key('a')
    press_key('a')
    press_key('a')
    press_key('a')
    press_key('a')
    press_key('a')
    press_key('a')
    press_key('a')
    press_key('a')
    press_key('a')
    press_key('w')
    press_key('w')
    press_key('w')
    press_key('w')
    press_key('w')
    press_key('w')
    press_key('w')
    press_key('w')
    press_key('w')
    press_key('w')
    press_key('a')
    press_key('a')
    press_key('w')
    press_key('w')
    press_key('w')
    press_key('f')
    press_key('f')
    press_key('f')
    press_key('f')
    press_key('f')
    press_key('f')
    press_key('f')
    press_key('f')
    press_key('f')
    press_key('f')
    press_key('f')
    press_key('f')
    press_key('f')
    press_key('f')
    press_key('f')
    press_key('f')
    press_key('f')
    press_key('f')
    press_key('f')
    press_key('f')
    press_key('f')
    press_key('f')
    press_key('f')
    press_key('f')
    press_key('f')
    press_key('f')
    press_key('f')
    press_key('f')
    press_key('f')
    press_key('f')
    press_key('f')
    press_key('f')
    press_key('f')
    press_key('s')
    press_key('s')
    press_key('s')
    press_key('s')
    press_key('s')
    press_key('s')
    press_key('s')
    press_key('s')
    press_key('s')
    press_key('s')
    press_key('s')
    for _ in range(36):
        press_key('d')
    press_key('w')
    press_key('w')
    press_key('d')  # start first grass_cycle (SAVE 5)
    for _ in range(11):
        grass_cycle_right()
    for _ in range(19):
        press_key('d')
    press_key('d', 2)
    press_key('w', 2)
    for _ in range(7):
        grass_cycle_up()
    for _ in range(4):
        grass_cycle_right()
    for _ in range(15):
        press_key('d')
    press_key('f')
    press_key('f')
    press_key('f')
    press_key('f')
    press_key('f')
    press_key('f')
    press_key('f')
    press_key('f')
    press_key('f')
    press_key('f')
    press_key('f')
    press_key('f')
    press_key('f')
    press_key('f')
    press_key('f')
    press_key('f')  # "well, well"
    press_key('f')
    press_key('f')
    press_key('f')
    press_key('f')
    press_key('f')
    press_key('f')
    press_key('f')  # give a nickname selection
    press_key('s')
    for _ in range(49):
        press_key('f')
    for _ in range(10):
        press_key('s')  # outside of lab
    for _ in range(18):
        press_key('f')
    press_key('f')
    press_key('f')
    press_key('f')
    press_key('f')
    for _ in range(26):
        press_key('f')  # save 6, outside of poke mart
    for _ in range(34):
        press_key('a')
    press_key('a')
    press_key('s')
    for _ in range(6):
        press_key('s')
    press_key('s')
    for _ in range(24):
        press_key('a')
    press_key('a')
    press_key('w')
    press_key('w')
    press_key('w')
    for _ in range(15):
        press_key('a')
    press_key('a')
    for _ in range(35):
        press_key('s')
    press_key('s')
    press_key('d')
    press_key('d')
    press_key('d')
    press_key('d')
    press_key('w')
    press_key('w')  # enter home
    press_key('w')
    press_key('w')
    press_key('d')
    press_key('f')
    press_key('f')
    press_key('f')
    for _ in range(18):
        press_key('f')
    time.sleep(5)
    for _ in range(16):
        press_key('f')
    press_key('s')
    press_key('s')
    press_key('s')  # outside of moms house (heading_to_jubilife save)
    press_key('a', 2)
    press_key('a')
    press_key('a')
    press_key('a', 2)
    press_key('w', 2)
    for _ in range(33):
        press_key('w')
    press_key('w', 2)
    press_key('d', 2)
    press_key('d')
    press_key('d')
    for _ in range(11):
        grass_cycle_right()
    for _ in range(19):
        press_key('d')
    press_key('d', 2)
    press_key('w', 2)
    for _ in range(7):
        grass_cycle_up()
    for _ in range(4):
        grass_cycle_right()
    for _ in range(34):
        press_key('d')
    press_key('d', 2)
    press_key('w', 2)
    for _ in range(18):
        press_key('w')
    press_key('w', 2)
    press_key('a', 2)
    press_key('a')
    press_key('a')
    press_key('a')
    press_key('a')
    press_key('f', 2)
    press_key('f', 2)
    press_key('f', 2)
    press_key('f', 2)
    press_key('f', 2)
    time.sleep(60)
    for _ in range(18):
        press_key('f', 2)  # dawn tutorial ends
    time.sleep(5)
    for _ in range(5):
        grass_cycle_left()
    for _ in range(5):
        press_key('a')
    grass_cycle_left()
    grass_cycle_left()
    grass_cycle_left()
    for _ in range(9):
        grass_cycle_up()
    press_key('w')
    press_key('w')
    press_key('w')
    press_key('w', 2)
    press_key('d', 2)  # save before first trainer


# Execute the main function
if __name__ == "__main__":
    main()
