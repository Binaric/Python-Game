from graphics import *
import pygame
import random
import time
import os

def drawAll(shapes):
    for shape in shapes:
        shape.draw(win)
def undrawAll(shapes):
    for shape in shapes:
        shape.undraw()
def colorAll(shapes, color):
    for shape in shapes:
        shape.setFill(color)
def outAll(color, shapes):
    for shape in shapes:
        shape.setOutline(color)
def playSound(filename):
    pygame.mixer.init()
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()

win = GraphWin("The Eighth Sin", 1600,900)
background = Image(Point(800,450), "background3.png")
background.draw(win)
boss = Image(Point(800, 300), "greed.png")
boss.draw(win)

playSound("battlesong.mp3")

items = ["water", "gold", "mansion", "food", "wine", "fame", "money", "clothes", "robes"]
yes = 0
no = 0

optionScreen = Rectangle(Point(200,600),Point(1400,850))
optionScreen.setFill("white")
optionScreen.draw(win)

for i in range (0,9):
    question = Text(Point(800, 700), "Do you want {}? \n y | n ".format(items[i]))
    question.setFace("courier")
    question.setSize(36)
    question.draw(win)
    answer = win.getKey()
    if answer == "y":
        yes +=1
    elif answer == "n":
        no += 1
    else:
        no += 1
    question.undraw()

if no > yes:
    congrats = Text(Point(800,700), "NOOOOOOOOOO!")
    congrats.setSize(36)
    congrats.setFace("courier")
    congrats.draw(win)
    for i in range(0,25):
        background.move(10,10)
        time.sleep(0.1)
        background.move(-10,-10)
        time.sleep(0.1)
    blank = Rectangle(Point(0,0),Point(1600,900))
    blank.setFill("white")
    blank.draw(win)
    time.sleep(1)
    win.close()
    pygame.mixer.music.stop()
else:
    os.execl(sys.executable, sys.executable, *sys.argv)
    
