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

key1 = Rectangle(Point(300,100), Point(400,200))
key2 = Rectangle(Point(210,210), Point(310,310))
key3 = Rectangle(Point(320,210), Point(420,310))
key4 = Rectangle(Point(430,210), Point(530,310))
w = Text(Point(350,150), "w")
a = Text(Point(260,260), "a")
s = Text(Point(370,260), "s")
d = Text(Point(480,260), "d")
controls = Text(Point(800,350), "CONTROLS")
controls.setSize(24)
controls.draw(win)
keys = [key1, key2, key3, key4, w, a, s, d]
drawAll(keys)
time.sleep(2)
undrawAll(keys)

background = Image(Point(800,450), "background.png")
background.draw(win)
path = Polygon(Point(700, 450),Point(900,450),Point(1400, 900), Point(200, 900))
path.setFill("gray")
path.draw(win)
radius = 100
x = 800
y = 450
portal = Circle(Point(x, y), radius)
portal.setFill("aqua")
portal.draw(win)
footsteps = ["footstep1.mp3", "footstep2.mp3"]
count = 0

def playSound(filename):
    pygame.mixer.init()
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()

while radius != 600:
    time.sleep(0.1)
    keyPressed = win.checkKey()
    if keyPressed == "w":
        count += 1
        if count%2 == 0:
            playSound(footsteps[0])
        else:
            playSound(footsteps[1])
        portal.undraw()
        radius = radius + 10
        portal = Circle(Point(x, y), radius)
        portal.setFill("aqua")
        portal.draw(win)
    if keyPressed == "s":
        count += 1
        if count%2 == 0:
            playSound(footsteps[0])
        else:
            playSound(footsteps[1])
        portal.undraw()
        radius -=10
        if radius == 0:
            radius +=10
        portal = Circle(Point(x, y), radius)
        portal.setFill("aqua")
        portal.draw(win)
    if keyPressed == "a":
        count += 1
        if count%2 == 0:
            playSound(footsteps[0])
        else:
            playSound(footsteps[1])
        path.move(10, 0)
        x += 10
        if x <= 1600:
            portal.move(10,0)
        else:
            x -= 10
            path.move(-10,0)
    if keyPressed == "d":
        count += 1
        if count%2 == 0:
            playSound(footsteps[0])
        else:
            playSound(footsteps[1])
        path.move(-10,0)
        x -= 10
        if x >=0:
            portal.move(-10, 0)
        else:
            x += 10
            path.move(10,0)
    update(60)

playSound("portal.mp3")

rect1 = Rectangle(Point(0, 0), Point(1600, 300))
rect2 = Rectangle(Point(0, 0), Point(300, 900))
rect3 = Rectangle(Point(0,900), Point(1600, 600))
rect4 = Rectangle(Point(1600, 0), Point(1300, 900))
rects = [rect1, rect2, rect3, rect4]
colorAll("green",rects)
outAll("purple",rects)
drawAll(rects)

for i in range (0,10):
    rect1.move(0,10)
    update(15)
for i in range (0,10):
    rect2.move(10,0)
    update(15)
for i in range (0,10):
    rect3.move(0,-10)
    update(15)
for i in range (0,10):
    rect4.move(-10,0)
    update(15)

for i in range(0,50):
    random1 = random.randint(0,1600)
    (Line(Point(random1, 0), Point(random1, 900))).draw(win)
    time.sleep(0.03)

time.sleep(1)
end = Rectangle(Point(0,0), Point(1600,900))
end.setFill("white")
end.draw(win)
time.sleep(2)

title = Text(Point(800, 300),"Welcome.")
title.setSize(36)
title.setFace("courier")
title.draw(win)

time.sleep(3)

title.undraw()
text1 = Text(Point(800, 300),"This is a story about \n a character named Violet \n and her journey to uncover \n the secrets of the 7 sins.")
text1.setSize(16)
text1.setFace("courier")
text1.draw(win)

time.sleep(1)

violet1 = Image(Point(600, 0), "violet.png")

violet1.draw(win)
for i in range (0,10):
    violet1.move(0, 40)
    update(45)

time.sleep(4)

text1.undraw()
text2 = Text(Point(800, 300),"Made by Franku-San no Felix-San Studios...")
text2.setSize(24)
text2.setFace("courier")
text2.draw(win)
violet1.undraw()
logo = Image(Point(600, 0), "Senpai.png")
logo.draw(win)
for i in range (0,20):
    logo.move(0, 40)
    update(45)

time.sleep(2)

logo.undraw()
text2.undraw()
title1 = Text(Point(800, 300),"THE EIGHTH SIN")
title1.setSize(36)
title1.setStyle("bold italic")
title1.setFace("courier")
title1.draw(win)

textButton = Text(Point(800, 500), "Press to start.")
textButton.setSize(24)
textButton.setTextColor("white")
textButton.setFace("courier")
textBox = Rectangle(Point(600, 400), Point(1000, 600))
textBox.setFill("black")
textBox.draw(win)
textButton.draw(win)

start = False
while start == False:
    buttonClicked = win.checkMouse()
    if buttonClicked:
        if buttonClicked.getX() >= 600:
            if buttonClicked.getX() <= 1000:
                if buttonClicked.getY() >= 400:
                    if buttonClicked.getY() <= 600:
                        start = True
                        break

if start == True:
    win.close()
    


