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
boss = Image(Point(800, 300), "greed.png")
boss.draw(win)

items = ["water", "gold", "mansion", "food", "wine", "fame", "money"]
yes = 0
no = 0

optionScreen = Rectangle(Point(200,600),Point(1400,850))
optionScreen.setFill("white")
optionScreen.draw(win)

for i in range (0,6):
    question = Text(Point(800, 700), "Do you want {}? \n ".format(items[i]))
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

