import pyautogui
from time import sleep

print("Please open iMessage and the message thread you'd like to bomb before continuing.")

# Get basic inputs from user
sendMsg = str(input('What would you like to send?: '))
maxSend = int(input('How many times do you want to send it?: '))

# Sleep for one second
sleep(1)

# Enable failsafe
pyautogui.FAILSAFE = True

# Press command+tad to switch windows
pyautogui.keyDown('command')
pyautogui.keyDown('tab')
pyautogui.keyUp('command')
pyautogui.keyUp('tab')

# Sleep for 2 seconds
sleep(2)

# Pause between typing for .05 seconds
pyautogui.PAUSE = 0.05

# While loops to repeatedly send the message
count = 0
while count < maxSend:
    pyautogui.typewrite(sendMsg)
    pyautogui.press('enter')
    count += 1