import pyautogui
import time

msg = "deviated septum check oop"
rep = 365

for i in range(5):
    print(i)
    time.sleep(1)

for i in range(rep):
    pyautogui.typewrite(msg + '\n')
    time.sleep(86400)
