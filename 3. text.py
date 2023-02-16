import pyautogui as py
import time

def findandClick(png):
    Po = py.locateOnScreen(png, confidence=0.75)
    if(Po):
        py.click(Po)

findandClick(r"auto\python\mobile BlueStacks\WannaI\Escape.PNG")
time.sleep(1)
findandClick(r"auto\python\mobile BlueStacks\WannaI\Delete.PNG")
time.sleep(1)
findandClick(r"auto\python\mobile BlueStacks\WannaI\Icon.PNG")
time.sleep(5)
findandClick(r"auto\python\mobile BlueStacks\WannaI\Join.PNG")
time.sleep(1)
