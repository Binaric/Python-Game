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

HPstat = 0

hpBar = Rectangle(Point(1300,80), Point(1500,100))
hpBar.setFill("lime")
hpBar.draw(win)

hplose1 = Rectangle(Point(1450,80), Point(1500,100))
hplose1.setFill("red")

hplose2 = Rectangle(Point(1400,80), Point(1500,100))
hplose2.setFill("red")

hplose3 = Rectangle(Point(1350,80), Point(1500,100))
hplose3.setFill("red")

hplose4 = Rectangle(Point(1300,80), Point(1500,100))
hplose4.setFill("red")

violet = Image(Point(300, 700), "violetback.png")
violet.draw(win)

attackBox = Rectangle(Point(450,675),Point(1500,875))
attackBox.setFill("white")
attackBox.draw(win)

attack1 = Text(Point(600,725), "Magic Ball")
attack1.setSize(24)
attack1.setFace("courier")
attack1.draw(win)

attack2 = Text(Point(1200,725), "Magic Laser")
attack2.setSize(24)
attack2.setFace("courier")
attack2.draw(win)

attack3 = Text(Point(1225, 800), "One Shot Magic")
attack3.setSize(24)
attack3.setFace("courier")
attack3.draw(win)

attack4 = Text(Point(600,800), "Earthquake")
attack4.setSize(24)
attack4.setFace("courier")
attack4.draw(win)

select1 = Rectangle(Point(480,700),Point(725,750))
select2 = Rectangle(Point(1075,700),Point(1325,750))
select3 = Rectangle(Point(480,775),Point(725,825))
select4 = Rectangle(Point(1075,775),Point(1400,825))

select1.draw(win)
select2.draw(win)
select3.draw(win)
select4.draw(win)

alive = True
HP = 4

while alive == True:
    buttonClicked = win.getMouse()
    if buttonClicked.getX() >= 480:
            if buttonClicked.getX() <= 725:
                if buttonClicked.getY() >= 700:
                    if buttonClicked.getY() <= 750:
                        HP -= 1
                        HPstat += 1
    if buttonClicked.getX() >= 1075:
            if buttonClicked.getX() <= 1325:
                if buttonClicked.getY() >= 700:
                    if buttonClicked.getY() <= 750:
                        HP -= 1
                        HPstat += 1
    if buttonClicked.getX() >= 480:
            if buttonClicked.getX() <= 725:
                if buttonClicked.getY() >= 775:
                    if buttonClicked.getY() <= 825:
                        HP -= 1
                        HPstat += 1
    if buttonClicked.getX() >= 1075:
            if buttonClicked.getX() <= 1400:
                if buttonClicked.getY() >= 775:
                    if buttonClicked.getY() <= 825:
                        HP -= 4
                        HPstat += 4 - HPstat
    if HPstat == 1:
        hplose1.draw(win)
    if HPstat == 2:
        hplose2.draw(win)
    if HPstat == 3:
        hplose3.draw(win)
    if HPstat == 4:
        hplose4.draw(win)
    if HP == 0:
        alive = False
    
