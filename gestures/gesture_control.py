# gesture control python program for controlling certain functions in web bro234 

# add pyautogui library for programmatically controlling the mouse and keyboard.
import pyautogui
import time

# Disable the fail-safe feature
pyautogui.FAILSAFE = False
screen_width, screen_height = pyautogui.size()

def action_func(hand_sign):

    # print the incoming data
    print('gesture', hand_sign)

    if 'Zoom In' in hand_sign:                    # zoom in
        pyautogui.hotkey('ctrl', '=')
        time.sleep(0.2)

    if 'Zoom Out' in hand_sign:                    # zoom out
        pyautogui.hotkey('ctrl', '-')
        time.sleep(0.2)

    if 'Scroll Up' in hand_sign:                   # scroll up
        # pyautogui.press('up')                      # performs "up arrow" operation which scrolls up the page
        pyautogui.scroll(300)
        time.sleep(0.2)

    if 'Scroll Down' in hand_sign:                 # scroll down
        # pyautogui.press('down')                   # performs "down arrow" operation which scrolls down the page
        pyautogui.scroll(-300)
        time.sleep(0.2)

    if 'Left' in hand_sign:                  # left slide
        pyautogui.moveTo(round(screen_width*3/4),round( screen_height/2)) # move to start point
        pyautogui.dragRel(-screen_width*2/3, 0, duration=1)  # move left to end point
        time.sleep(0.5)
    if 'Right' in hand_sign:                  # right slide
        pyautogui.moveTo(round(screen_width*1/4),round( screen_height/2)) # move to start point
        pyautogui.dragRel(screen_width*2/3, 0, duration=1)  # move left to end point
        time.sleep(0.5)
    
    # if 'Ok' in hand_sign:                  # Ok



    hand_sign = ""                            # clears the data
