import keyboard
import mouse
import time

# You can change this hotkey and button
hotkey = "F4"
button = "left"

isClicking = False

def set_clicker():
    global isClicking
    if isClicking:
        isClicking = False
        print("AutoClicker are offline")
    else:
        isClicking = True
        print("AutoClicker is online")


keyboard.add_hotkey(hotkey, set_clicker)

while True:
    if isClicking:
        mouse.double_click(button = button)
        time.sleep(0.01)