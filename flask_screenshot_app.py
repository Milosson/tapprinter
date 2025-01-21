from flask import Flask
import pyautogui
import os
import time
from pyvirtualdisplay import Display

# Starta en virtuell skärm
display = Display(visible=0, size=(1920, 1080))
display.start()

app = Flask(__name__)
screenshot_folder = "screenshots"

if not os.path.exists(screenshot_folder):
    os.makedir(screenshot_folder)



@app.route("/screenshot", method=["GET"])

def take_screenshot():
    screenshot_path = os.path.join(screenshot_folder, f"screenshot_{int(time.time())}.png")
    pyautogui.screenshot(screenshot_path)
    return f"SCreenshot taken and saved in folder as {screenshot_path}"

if __name__ == "__main__":
    app.run(debug=True)


display.stop()