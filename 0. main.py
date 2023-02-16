# pip install opencv-python을 깔아서 뒤에 confidence=0.7 (70%만 일치해도 인식!!!)
# if(??):형식!!
import pyautogui as py
import time

def findandClick(png):
    Po = py.locateOnScreen(png, confidence=0.75)
    if(Po):
        py.click(Po)


findandClick(r"auto\python\mobile BlueStacks\WannaI\No Today.PNG")
time.sleep(1)
findandClick(r"auto\python\mobile BlueStacks\WannaI\Join.PNG")
time.sleep(1)
findandClick(r"auto\python\mobile BlueStacks\WannaI\LuckyBOX.PNG")
time.sleep(1)
findandClick(r"auto\python\mobile BlueStacks\WannaI\BixBox.PNG")
time.sleep(1)
findandClick(r"auto\python\mobile BlueStacks\WannaI\OpentheBox.PNG")
time.sleep(1)
findandClick(r"auto\python\mobile BlueStacks\WannaI\Okay.PNG")
time.sleep(1)
findandClick(r"auto\python\mobile BlueStacks\WannaI\Back.PNG")
time.sleep(1)
findandClick(r"auto\python\mobile BlueStacks\WannaI\Join.PNG")
time.sleep(1)

while True:
    findandClick(r"auto\python\mobile BlueStacks\WannaI\Blue.PNG")
    time.sleep(0.5)
    findandClick(r"auto\python\mobile BlueStacks\WannaI\X.PNG")
    if findandClick(r"auto\python\mobile BlueStacks\WannaI\Green.PNG"):
        break