# automation
def findandClick(png):
    Po = py.locateOnScreen(png, confidence=0.75)
    if(Po):
        py.click(Po)
