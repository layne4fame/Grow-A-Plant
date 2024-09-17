#!/usr/bin/env python3

import turtle
import time



def drawGround():
    ground = turtle.Turtle()
    ground.speed(000)
    ground.hideturtle()
    ground.pensize(10)
    ground.penup()
    ground.goto(-700, -200)
    ground.pendown()
    ground.right(90)
    i = 0
    while i < 36:
        if(i%2 == 0):
            ground.color("darkgreen")
            ground.fillcolor("darkgreen")
            ground.begin_fill()
            ground.circle(20, extent = -180)
            ground.end_fill()
        else:
            ground.color("darkgreen")
            ground.fillcolor("darkgreen")
            ground.begin_fill()
            ground.circle(-20, extent = 180)
            ground.end_fill()
        i = i + 1
    
    ground.fillcolor("darkgreen")
    ground.begin_fill()
    ground.goto(500, -500)
    ground.goto(-700, -500)
    ground.goto(-700, -200)
    ground.end_fill()

def drawOverBackground(color):
    blue = turtle.Turtle()
    blue.speed(000)
    blue.penup()
    blue.color(color)
    blue.goto(-700, 700)
    blue.begin_fill()
    blue.pendown()
    blue.pensize(15)
    blue.fillcolor(color)
    blue.goto(700, 700)
    blue.goto(700, -700)
    blue.goto(-700, -700)
    blue.end_fill()


def theCategories():
    tegan = turtle.Turtle()
    colors = turtle.Turtle()
    colors.hideturtle()
    tegan.hideturtle()
    tegan.fillcolor("white")
    tegan.color("white")
    tegan.speed(000000)
    tegan.penup()
    tegan.goto(-450, 300)
    tegan.pendown()
    arg = "Key for Petal Color:"
    tegan.write(arg, move=False, align='left', font=('Georgia',15,'bold'))

    tegan.penup()
    tegan.goto(-450, 280)
    tegan.pendown()
    arg = "Good"
    tegan.write(arg, move=False, align='left', font=('Georgia',15,'bold'))
    colors.penup()
    colors.goto(-350, 285)
    colors.pendown()
    colors.begin_fill()
    colors.color("yellow")
    colors.pensize(5)
    colors.circle(5)
    colors.end_fill()

    tegan.penup()
    tegan.goto(-450, 265)
    tegan.pendown()
    arg = "Nuetral"
    tegan.write(arg, move=False, align='left', font=('Georgia',15,'bold'))
    colors.penup()
    colors.goto(-350, 270)
    colors.pendown()
    colors.begin_fill()
    colors.color("white")
    colors.pensize(5)
    colors.circle(5)
    colors.end_fill()

    tegan.penup()
    tegan.goto(-450, 250)
    tegan.pendown()
    arg = "Bad"
    tegan.write(arg, move=False, align='left', font=('Georgia',15,'bold'))
    colors.penup()
    colors.goto(-350, 255)
    colors.pendown()
    colors.begin_fill()
    colors.color("brown")
    colors.pensize(5)
    colors.circle(5)
    colors.end_fill()
    
    
    tegan.penup()
    tegan.goto(-450, 200)
    tegan.pendown()
    arg = "Key for Leaf Color:"
    tegan.write(arg, move=False, align='left', font=('Georgia',15,'bold'))

    tegan.penup()
    tegan.goto(-450, 180)
    tegan.pendown()
    arg = "Good"
    tegan.write(arg, move=False, align='left', font=('Georgia',15,'bold'))
    colors.penup()
    colors.goto(-350, 185)
    colors.pendown()
    colors.begin_fill()
    colors.color("limegreen")
    colors.pensize(5)
    colors.circle(5)
    colors.end_fill()
    
    tegan.penup()
    tegan.goto(-450, 165)
    tegan.pendown()
    arg = "Nuetral"
    tegan.write(arg, move=False, align='left', font=('Georgia',15,'bold'))
    colors.penup()
    colors.goto(-350, 170)
    colors.pendown()
    colors.begin_fill()
    colors.color("lightgreen")
    colors.pensize(5)
    colors.circle(5)
    colors.end_fill()

    tegan.penup()
    tegan.goto(-450, 150)
    tegan.pendown()
    arg = "Bad"
    tegan.write(arg, move=False, align='left', font=('Georgia',15,'bold'))
    colors.penup()
    colors.goto(-350, 155)
    colors.pendown()
    colors.begin_fill()
    colors.color("yellow")
    colors.pensize(5)
    colors.circle(5)
    colors.end_fill()


    
    