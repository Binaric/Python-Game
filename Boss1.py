from graphics import *
import pygame
import random
import time

def drawAll(shapes):
    for shape in shapes:
        shape.draw(win)
def undrawAll(shapes):
    for shape in shapes:
        shape.undraw()
def colorAll(color, shapes):
    for shape in shapes:
        shape.setFill(color)
def outAll(color, shapes):
    for shape in shapes:
        shape.setOutline(color)
        
win = GraphWin("The Eighth Sin", 1600,900)
boss = Image(Point(1400, 300), "lust.png")
boss.draw(win)

hpBar = Rectangle(Point(1300,80), Point(1500,100))
hpBar.setFill("lime")
hpBar.draw(win)

violet = Image(Point(300, 700), "violetback.png")
violet.draw(win)
