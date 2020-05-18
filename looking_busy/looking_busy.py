#looking_busy.py
"""A program to determine whether you are idle, or away from your computer, by detecting a lack of mouse movement over some
period of time"""

import time
"""pyautogui lets your Python scripts control the mouse and keyboard to automate interactions with other applications."""
import pyautogui

#Method to move mouse every 10 seconds to keep apps active
def busy():
    print('Press CTRL-C to quit.')
    try:
        while True:
            #pyautogui.moveRel(xOffset, yOffset, duration)
            pyautogui.moveRel(5, 0, 0.5)
            pyautogui.moveRel(-5, 0, 0.5)

            #10 secs sleep time interval
            time.sleep(10)
    except KeyboardInterrupt:
        print('Process has quit...')

#Main method
if __name__ == "__main__":
    #Calling busy method
    busy()