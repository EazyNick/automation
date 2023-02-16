#사진을 찾는다면, 못찾는다면 어떻게하지? True, False로는 안되던데..
#첫 시행착오 파일. I'm nerd ㅜㅜ
import pyautogui
import time

def findandClick():
    xPosition = pyautogui.locateOnScreen(r"auto\python\mobile BlueStacks\WannaI\X.PNG", confidence=0.6)
    picPosition1 = pyautogui.locateOnScreen(r"auto\python\mobile BlueStacks\WannaI\Feed.PNG", confidence=0.7)
    picPosition2 = pyautogui.locateOnScreen(r"auto\python\mobile BlueStacks\WannaI\Thebogi.PNG", confidence=0.68)
    picPosition3 = pyautogui.locateOnScreen(r"auto\python\mobile BlueStacks\WannaI\Click.PNG", confidence=0.6)
    # picPosition4 = pyautogui.locateOnScreen(r"auto\python\mobile BlueStacks\WannaI\4.PNG", confidence=0.6)
    # picPosition5 = pyautogui.locateOnScreen(r"auto\python\mobile BlueStacks\WannaI\5.PNG", confidence=0.6)
    # picPosition6 = pyautogui.locateOnScreen(r"auto\python\mobile BlueStacks\WannaI\6.PNG", confidence=0.6)
    # picPosition7 = pyautogui.locateOnScreen(r"auto\python\mobile BlueStacks\WannaI\7.PNG", confidence=0.6)
    picPosition8 = pyautogui.locateOnScreen(r"auto\python\mobile BlueStacks\WannaI\Back.PNG", confidence=0.8)
    picPosition9 = pyautogui.locateOnScreen(r"auto\python\mobile BlueStacks\WannaI\444444444.PNG", confidence=0.7)
    pyautogui.click(picPosition2)
    time.sleep(1)
    final = pyautogui.move(0,-20,0)
    pyautogui.click(final)
    pyautogui.click(picPosition9)
    time.sleep(1)
    final2 = pyautogui.move(0,-20,0)
    pyautogui.click(final2)
    time.sleep(20)
    pyautogui.click(picPosition8)
    time.sleep(1)
    # pyautogui.click(picPosition8)
    # elif picPosition3 == True:
    #     pyautogui.move(0, 20, 0)
    #     pyautogui.click
    #     time.sleep(0.5)
    # elif picPosition4 == True:
    #     pyautogui.move(0, 20, 0)
    #     pyautogui.click
    #     time.sleep(0.5)
    # elif picPosition5 == True:
    #     pyautogui.move(0, 20, 0)
    #     pyautogui.click
    #     time.sleep(0.5)
    # elif picPosition6 == True:
    #     pyautogui.move(0, 20, 0)
    #     pyautogui.click
    #     time.sleep(0.5)
    # elif picPosition7 == True:
    #     pyautogui.move(0, 20, 0)
    #     pyautogui.click
    #     time.sleep(0.5)

findandClick()
