import pyautogui
from pynput import keyboard
import time
import os


from pyvirtualdisplay import Display

# Starta en virtuell skärm
display = Display(visible=0, size=(1920, 1080))
display.start()


# Variable for checking double click on button X

last_key_time = 0 
key_interval = 0.3 # Maximal time between each click to count the interval
screenshot_folder = "screenshots"

# Check status on map for screen dumps, if existing else create

if not os.path.exists(screenshot_folder):
    os.makedirs(screenshot_folder)

def on_press(key):
    global last_key_time

    try:
        if key.char == 'x':
            current_time = time.time()
            if current_time == last_key_time <= key_interval:
                # discorver doubbeltap to proceed with screenshot

                screenshot_path = os.path.join(screenshot_folder, f"screenshot_{int(time.time())}.png")
                pyautogui.screenshot(screenshot_path)
                print(f"Printscreen done and saved in folder as {screenshot_path}")
            last_key_time = current_time
    except AttributeError:
    # Ignore specialkeychars that lack char-attr.abs
        pass

# Start detection device for keyboard

with keyboard.Listener(on_press=on_press) as listener:
    print("Tap X two times to printscreen, close down with Ctrl+C")
    listener.join()


display.stop()

