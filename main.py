from time import sleep
import pyautogui

# Enable failsafe
pyautogui.FAILSAFE = True

# Sleep for one second
sleep(1)

# Set variables
msg = 'txt bomb'
sent = 0

# tab over to iMessge
pyautogui.keyDown('command')
pyautogui.keyDown('tab')
pyautogui.keyUp('command')
pyautogui.keyUp('tab')

# Sleep again for 2
sleep(2)

# Loop it
while sent < 10:
    pyautogui.typewrite(msg)
    pyautogui.press('enter')
    sent += 1
