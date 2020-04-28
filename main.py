import pyautogui
from time import sleep

print("Please open iMessage and the message thread you'd like to bomb before continuing.")

# Enable failsafe
pyautogui.FAILSAFE = True

# Get basic inputs from user
sendMsg = str(input('What would you like to send?: '))
maxSend = int(input('How many times do you want to send it?: '))
sent = 0

# Sleep for one second
sleep(1)

# Press command+tad to switch windows
pyautogui.keyDown('command')
pyautogui.keyDown('tab')
pyautogui.keyUp('command')
pyautogui.keyUp('tab')

# Sleep for 2 seconds
sleep(2)

# Pause between typing for .05 seconds
pyautogui.PAUSE = 0.05

# While loop to send the message
while sent < maxSend:
    pyautogui.typewrite(sendMsg)
    pyautogui.press('enter')
    sent += 1
