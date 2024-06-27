from pyautogui import * 
import pyautogui 
import time 
import keyboard 
import win32api
import win32con
import winsound
import subprocess

running = True

def toggle_script():
    global running
    running = not running
    print("Script is", "running" if running else "paused")

# Hotkey
keyboard.add_hotkey(']', toggle_script)

def press_and_hold_enter():
    subprocess.run(['PressEnter.exe'])

def play_sound():
    winsound.Beep(523, 250)
    winsound.Beep(659, 250)
    winsound.Beep(784, 250)
    winsound.Beep(1047, 250)
    

print('Start/Stop script: "]"')
print('Script is running')

while True:
    if running:
        try:
            if pyautogui.locateOnScreen('pan.png', region=(1777,949,46,27), grayscale=True, confidence=0.8) is not None:
                press_and_hold_enter()
                time.sleep(0.5)
        except pyautogui.ImageNotFoundException:
            pass  # Do nothing

        try:
            if pyautogui.locateOnScreen('full.png', region=(1597,673,278,29), grayscale=True, confidence=0.8) is not None:
                play_sound()
                time.sleep(0.5)
                play_sound()
                time.sleep(0.5)
                play_sound()
                time.sleep(0.5)
                toggle_script()
        except pyautogui.ImageNotFoundException:
            pass  # Do nothing
    else:
        time.sleep(0.5)  # Pause script
