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
def colorAll(color, shapes):
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
background = Image(Point(800,450), "background2.png")
background.draw(win)

playSound("battlesong.mp3")

intro1 = Text(Point(800,400), "In Irkalla, there was one rule: \n Never devulge into the 7 sins.")
intro1.setSize(36)
intro1.setTextColor("white")
intro1.draw(win)

intro2 = Text(Point(800,600), "Unfortunately, Violet broke that rule by commiting the eighth sin.")
intro2.setSize(36)
intro2.setTextColor("white")
intro2.draw(win)

for i in range (0,2):
    for j in range (0,20):
        background.move(5,5)
        update(10)
    for k in range (0,20):
        background.move(-5,-5)
        update(10)

intro1.undraw()
intro2.undraw()
background.undraw()

time.sleep(0.5)

background1 = Image(Point(800,450), "background3.png")
background1.draw(win)

god = Image(Point(800,600), "god.png")
god.draw(win)

intro3 = Text(Point(800,400), "Violet was sent on a journey to defeat the 7 sins. \n by God.")
intro3.setSize(36)
intro3.draw(win)

time.sleep(3)

pygame.mixer.music.stop()
win.close()

        
    
