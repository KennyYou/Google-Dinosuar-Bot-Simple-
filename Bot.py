from PIL import ImageGrab, ImageOps
import pyautogui
import time
from numpy import *


class Cordinates():
    replayBtn = (480, 520)
    dinosaur = (230, 530)
    # x = 260 (cordinate to check for tree)
    # y = 570 (cordinate of half tree


# restart game function
def restartGame():
    pyautogui.click(Cordinates.replayBtn)


restartGame()


def pressSpace():
    pyautogui.keyDown('space')
    time.sleep(0.05)
    print("jump")
    pyautogui.keyUp('space')


pressSpace()


def imageGrab():
    box = (Cordinates.dinosaur[0] + 60, Cordinates.dinosaur[1],
           Cordinates.dinosaur[0] + 100, Cordinates.dinosaur[1] + 30)
    image = ImageGrab.grab(box)
    grayImage = ImageOps.grayscale(image)
    a = array(grayImage.getcolors())
    print(a.sum())
    return a.sum()

def main():
    restartGame()
    while True:
        if(imageGrab()!=1447):
            pressSpace()
        #Setting Time to no lag enables higher score
        time.sleep(0.0)

main()
imageGrab()




