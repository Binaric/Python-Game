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
def mBall():
    blast = Circle(Point(375,600),50)
    blast.setFill("aqua")
    blast.draw(win)
    playSound("magicball.mp3")
    for i in range (105):
        blast.move(10,-4)
        update(60)
    blast.undraw()
    boss.move(10,0)
    time.sleep(0.3)
    boss.move(-10,0)
    time.sleep(0.3)
    boss.move(10,0)
    time.sleep(0.3)
    boss.move(-10,0)
def mLaser():
    lightning = Line(Point(350, 650),Point(1400, 300))
    lightning1 = Line(Point(350, 650),Point(1400, 290))
    lightning2 = Line(Point(350, 650),Point(1400, 310))
    lightning3 = Line(Point(350, 650),Point(1400, 320))
    lightning4 = Line(Point(350, 650),Point(1400, 280))
    lightnings = [lightning, lightning1, lightning2,lightning3,lightning4]
    drawAll(lightnings)
    playSound("magiclaser.mp3")
    for i in range (0, 30):
        colorAll(lightnings,"purple")
        time.sleep(0.1)
        colorAll(lightnings,"blue")
    undrawAll(lightnings)
    boss.move(10,0)
    time.sleep(0.3)
    boss.move(-10,0)
    time.sleep(0.3)
    boss.move(10,0)
    time.sleep(0.3)
    boss.move(-10,0)
def quake():
    playSound("quake.mp3")
    for i in range(0,25):
        background.move(10,10)
        time.sleep(0.1)
        background.move(-10,-10)
        time.sleep(0.1)
    boss.move(10,0)
    time.sleep(0.3)
    boss.move(-10,0)
    time.sleep(0.3)
    boss.move(10,0)
    time.sleep(0.3)
    boss.move(-10,0)
def oneShot():
    playSound("ko.mp3")
    radius = 50
    ball = Circle(Point(800,450), radius)
    ball.draw(win)
    for i in range (0,60):
        radius += 10
        ball.undraw()
        ball = Circle(Point(800,450), radius)
        ball.draw(win)
        update(15)
    ball.undraw()
    boss.move(10,0)
    time.sleep(0.3)
    boss.move(-10,0)
    time.sleep(0.3)
    boss.move(10,0)
    time.sleep(0.3)
    boss.move(-10,0)
    
win = GraphWin("The Eighth Sin", 1600,900)
background = Image(Point(800,450), "background2.png")
background.draw(win)
boss = Image(Point(1400, 300), "sloth.png")
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

miss = Text(Point(900, 400), "MISS")
miss.setFace("courier")
miss.setTextColor("white")
miss.setSize(36)


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
                        mBall()
    if buttonClicked.getX() >= 1075:
            if buttonClicked.getX() <= 1325:
                if buttonClicked.getY() >= 700:
                    if buttonClicked.getY() <= 750:
                        mLaser()
                        HP -= 1
                        HPstat += 1
    if buttonClicked.getX() >= 480:
            if buttonClicked.getX() <= 725:
                if buttonClicked.getY() >= 775:
                    if buttonClicked.getY() <= 825:
                        quake()
                        HP -= 1
                        HPstat += 1
    if buttonClicked.getX() >= 1075:
            if buttonClicked.getX() <= 1400:
                if buttonClicked.getY() >= 775:
                    if buttonClicked.getY() <= 825:
                        oneShot()
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
    if HP <= 0:
        alive = False

time.sleep(2)
blank = Rectangle(Point(0,0),Point(1600,900))
blank.setFill("white")
blank.draw(win)
restart = Text(Point(800, 400), "Restart? (y OR n) \n n to continue story")
restart.setFace("courier")
restart.setSize(36)
restart.draw(win)
keyPressed = win.getKey()
if keyPressed == "y":
    os.execl(sys.executable, sys.executable, *sys.argv)
else:
    win.close()
    
    
