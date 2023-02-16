# automation
내 일을 자동화 해주는 코드
def findandClick(png):
    Po = py.locateOnScreen(png, confidence=0.75)
    if(Po):
        py.click(Po)
