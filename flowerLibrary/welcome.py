#!/usr/bin/env python3
from turtle import *
import turtle
import time
import background




def get_name():
    return textinput("Name","Enter a name under 8 characters")


def writeTheRules():
    return 0

def weclomeScreen():
    background.drawOverBackground("black")
    tegan = turtle.Turtle()
    tegan.hideturtle()
    tegan.fillcolor("white")
    tegan.color("white")
    tegan.speed(1)
    tegan.penup()
    tegan.goto(-300, 0)
    tegan.pendown()
    arg = "Welcome to Plant Time!"
    tegan.write(arg, move=False, align='left', font=('Georgia',30,'bold'))
    time.sleep(5)
    background.drawOverBackground("black")
    
    tegan.penup()
    tegan.goto(-10, 220)
    tegan.pendown()
    arg = "How to play"
    tegan.write(arg, move=False, align='center', font=('Georgia',30,'bold'))
    #time.sleep(5)

    tegan.color("springgreen")
    tegan.penup()
    tegan.goto(-400, 150)
    tegan.pendown()
    arg = "1) Place your sensors where you would \nwant a plant to grow"
    tegan.write(arg, move=False, align='left', font=('Georgia',20,'bold'))
    

    tegan.penup()
    tegan.goto(-400, 80)
    tegan.pendown()
    arg = "2) Look at happy level to know how well \nyour plant is doing"
    tegan.write(arg, move=False, align='left', font=('Georgia',20,'bold'))
    

    tegan.penup()
    tegan.goto(-400, 10)
    tegan.pendown()
    arg = "3) Make sure you move around your light and \ntemperature sensors to ensure proper placement"
    tegan.write(arg, move=False, align='left', font=('Georgia',20,'bold'))
    


    tegan.penup()
    tegan.goto(-400, -60)
    tegan.pendown()
    arg = "4) Wait for leaves to appear to track your \nprogress throughout the day."
    tegan.write(arg, move=False, align='left', font=('Georgia',20,'bold'))
    
    tegan.penup()
    tegan.goto(-400, -100)
    tegan.pendown()
    arg = "5) Once done the petals will show final results."
    tegan.write(arg, move=False, align='left', font=('Georgia',20,'bold'))
    
    time.sleep(10)


def startButton(x, y):
    #-250 = x and y = -200
    pen = turtle.Turtle()
    pen.hideturtle()
    pen.color("red")
    pen.fillcolor("red")
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.begin_fill()
    pen.circle(50)
    pen.end_fill()

    pen.penup()
    pen.goto(x-35, y+40)
    pen.pendown()
    pen.color("white")
    arg = "START"
    pen.write(arg, move=False, align='left', font=('Georgia',20,'bold'))
        

    
    





