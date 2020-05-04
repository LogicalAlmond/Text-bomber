import pyautogui
from time import sleep
import argparse

# Set up cli arguments
parser = argparse.ArgumentParser(description='Text Bombing application. Open iMessage and the message thread you would like to bomb before continuing.')
parser.add_argument('message', type=str, help='The message to be sent')
parser.add_argument('max', type=int, help='Number of times to send the message')
args = parser.parse_args()

# Put code into a function instead of free-ballin
def textbomber(message, maxsend):
    pyautogui.FAILSAFE = True
    sleep(1)
    pyautogui.keyDown('command')
    pyautogui.keyDown('tab')
    pyautogui.keyUp('command')
    pyautogui.keyUp('tab')
    sleep(2)
    sent = 0
    pyautogui.PAUSE = 0.05
    while sent < maxsend:
        pyautogui.typewrite(message)
        pyautogui.press('enter')
        sent += 1

if __name__ == '__main__':
    textbomber(args.message, args.max)
