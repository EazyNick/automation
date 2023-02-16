#최종본
import pyautogui as py
import time

def findandClick(png):
    Po = py.locateOnScreen(png, confidence=0.75)
    if(Po):
        py.click(Po)

while True:
    findandClick(r"auto\python\mobile BlueStacks\WannaI\Feed.PNG")
    time.sleep(2.2)
    findandClick(r"auto\python\mobile BlueStacks\WannaI\Thebogi.PNG")
    time.sleep(0.1)
    pF = py.move(0,-20,0)
    time.sleep(0.1)
    py.click(pF)
    time.sleep(13.5)
    findandClick(r"auto\python\mobile BlueStacks\WannaI\Back.PNG")
    time.sleep(2)
    findandClick(r"auto\python\mobile BlueStacks\WannaI\Back.PNG")
    time.sleep(3)
    PoE = py.locateOnScreen(r"auto\python\mobile BlueStacks\WannaI\wannai.PNG", confidence=0.75)
    if not (PoE):
        findandClick(r"auto\python\mobile BlueStacks\WannaI\Escape.PNG")
        time.sleep(1)
        findandClick(r"auto\python\mobile BlueStacks\WannaI\Delete.PNG")
        time.sleep(1)
        findandClick(r"auto\python\mobile BlueStacks\WannaI\Icon.PNG")
        time.sleep(5)
        findandClick(r"auto\python\mobile BlueStacks\WannaI\Join.PNG")
        time.sleep(1)
#break로 빠져나오고 재실행 후 다시 while True를 쓸라고 했으나
#그러면 무한 재생이 안되서 그냥 이렇게 넣음.
