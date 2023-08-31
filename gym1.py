import time
import pyautogui

# Function to press and hold a key, then release it
def press_key(key, delay=0.5):
    pyautogui.keyDown(key)  # hold duration
    pyautogui.keyUp(key)
    time.sleep(delay)  # delay between each key press

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
    press_key('s')  # Exit House


# Execute the main function
if __name__ == "__main__":
    main()
