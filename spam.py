import pyautogui
import time
time.sleep(5)
with open("spamfile.txt" ,"r") as f:

    for lines in f:
        pyautogui.typewrite(lines)
        pyautogui.press("enter")