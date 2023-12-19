import time
import pyautogui

def toggle_caps_lock():
    # Simulate pressing and releasing the Caps Lock key
    pyautogui.press('capslock')
    pyautogui.press('capslock')

if __name__ == "__main__":
    while True:
        toggle_caps_lock()
        time.sleep(10)  # Wait for 60 seconds before toggling again
