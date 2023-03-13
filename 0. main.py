# pip install opencv-python을 깔아서 뒤에 confidence=0.7 (70%만 일치해도 인식!!!)
# if(??):형식!!
import pyautogui as py
import time
import keyboard

def findandClick(png):
    Po = py.locateOnScreen(png, confidence=0.75)
    if(Po):
        py.click(Po)


# findandClick(r"No Today.PNG")
# time.sleep(1)
# findandClick(r"LuckyBOX.PNG")
# time.sleep(1)
# findandClick(r"BixBox.PNG")
# time.sleep(2)
# findandClick(r"OpentheBox.PNG")
# time.sleep(4)
# findandClick(r"Okay.PNG")
# time.sleep(5)
# findandClick(r"\Back.PNG")
# time.sleep(1)
# findandClick(r"Join.PNG")
# time.sleep(1)

while keyboard.is_pressed('q') == False:
    findandClick(r"Blue.PNG")
    time.sleep(0.5)
    findandClick(r"X.PNG")
    if py.locateOnScreen(r"Green.PNG", confidence=0.75):
        break