#최종본
import pyautogui as py
import time
import keyboard

def findandClick(png):
    Po = py.locateOnScreen(png, confidence=0.75)
    if(Po):
        py.click(Po)

while keyboard.is_pressed('q') == False:
    findandClick(r"Feed.PNG")
    time.sleep(2.2)
    findandClick(r"Thebogi.PNG")
    time.sleep(0.1)
    pF = py.move(0,-20,0)
    time.sleep(0.1)
    py.click(pF)
    time.sleep(14.5)
    findandClick(r"Back.PNG")
    time.sleep(4.1)
    findandClick(r"Back.PNG")
    time.sleep(2.4)
    PoE = py.locateOnScreen(r"wannai.PNG", confidence=0.75)
    if not (PoE):
        findandClick(r"Escape.PNG")
        time.sleep(2)
        findandClick(r"Delete.PNG")
        time.sleep(1)
        findandClick(r"Icon.PNG")
        time.sleep(5)
        findandClick(r"Join.PNG")
        time.sleep(1)
#break로 빠져나오고 재실행 후 다시 while True를 쓸라고 했으나
#그러면 무한 재생이 안되서 그냥 이렇게 넣음.
