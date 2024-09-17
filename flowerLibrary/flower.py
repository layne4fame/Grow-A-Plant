#!/usr/bin/env python3

import turtle
import time

# screen = turtle.Screen()
# screen.bgcolor("LightSkyBlue")



def drawstem():
    layne = turtle.Turtle()
    layne.hideturtle()
    layne.pensize(8)
    layne.fillcolor("darkgreen")
    layne.color("darkgreen")
    layne.speed(0000)
    layne.penup()
    layne.goto(5, -200)
    layne.pendown()
    layne.goto(5, 0)

def drawpetals():
    jake = turtle.Turtle()
    jake.hideturtle()
    jake.pensize(8)
    jake.speed(0000)

    #first petals
    jake.penup()
    color = "seashell"
    size = 40
    jake.color(color)
    
    jake.goto(5, 75)
    jake.pendown()
    jake.begin_fill()
    jake.left(50)
    jake.circle(size, extent=100)
    jake.right(300)
    jake.circle(size, extent=100)
    jake.end_fill()
    jake.penup()

    jake.goto(20, 60)
    jake.pendown()
    jake.begin_fill()
    jake.right(10)
    jake.left(50)
    jake.circle(size, extent=100)
    jake.right(300)
    jake.circle(size, extent=100)
    jake.end_fill()
    jake.penup()


    jake.goto(5, 40)
    jake.pendown()
    jake.begin_fill()
    jake.right(10)
    jake.left(50)
    jake.circle(size, extent=100)
    jake.right(300)
    jake.circle(size, extent=100)
    jake.end_fill()
    jake.penup()

    jake.goto(-15, 40)
    jake.pendown()
    jake.begin_fill()
    jake.right(10)
    jake.left(50)
    jake.circle(size, extent=100)
    jake.right(300)
    jake.circle(size, extent=100)
    jake.end_fill()
    jake.penup()

    jake.goto(-17, 55)
    jake.pendown()
    jake.begin_fill()
    jake.right(10)
    jake.left(50)
    jake.circle(size, extent=100)
    jake.right(300)
    jake.circle(size, extent=100)
    jake.end_fill()
    jake.penup()

    jake.goto(-13, 70)
    jake.pendown()
    jake.begin_fill()
    jake.right(10)
    jake.left(50)
    jake.circle(size, extent=100)
    jake.right(300)
    jake.circle(size, extent=100)
    jake.end_fill()
    jake.penup()

    #second petals
    jake.penup()
    color ="seashell3"
    jake.color(color)
    #jake.right(30)
    size = 30
    
    jake.goto(5, 75)
    jake.pendown()
    jake.begin_fill()
    jake.left(50)
    jake.circle(size, extent=100)
    jake.right(300)
    jake.circle(size, extent=100)
    jake.end_fill()
    jake.penup()

    jake.goto(20, 60)
    jake.pendown()
    jake.begin_fill()
    jake.right(10)
    jake.left(50)
    jake.circle(size, extent=100)
    jake.right(300)
    jake.circle(size, extent=100)
    jake.end_fill()
    jake.penup()


    jake.goto(5, 40)
    jake.pendown()
    jake.begin_fill()
    jake.right(10)
    jake.left(50)
    jake.circle(size, extent=100)
    jake.right(300)
    jake.circle(size, extent=100)
    jake.end_fill()
    jake.penup()

    jake.goto(-15, 40)
    jake.pendown()
    jake.begin_fill()
    jake.right(10)
    jake.left(50)
    jake.circle(size, extent=100)
    jake.right(300)
    jake.circle(size, extent=100)
    jake.end_fill()
    jake.penup()

    jake.goto(-17, 55)
    jake.pendown()
    jake.begin_fill()
    jake.right(10)
    jake.left(50)
    jake.circle(size, extent=100)
    jake.right(300)
    jake.circle(size, extent=100)
    jake.end_fill()
    jake.penup()

    jake.goto(-13, 70)
    jake.pendown()
    jake.begin_fill()
    jake.right(10)
    jake.left(50)
    jake.circle(size, extent=100)
    jake.right(300)
    jake.circle(size, extent=100)
    jake.end_fill()
    jake.penup()


    #third petals
    jake.penup()
    color = "seashell4"
    jake.color(color)
    size = 20
    
    jake.goto(5, 75)
    jake.pendown()
    jake.begin_fill()
    jake.left(50)
    jake.circle(size, extent=100)
    jake.right(300)
    jake.circle(size, extent=100)
    jake.end_fill()
    jake.penup()

    jake.goto(20, 60)
    jake.pendown()
    jake.begin_fill()
    jake.right(10)
    jake.left(50)
    jake.circle(size, extent=100)
    jake.right(300)
    jake.circle(size, extent=100)
    jake.end_fill()
    jake.penup()


    jake.goto(5, 40)
    jake.pendown()
    jake.begin_fill()
    jake.right(10)
    jake.left(50)
    jake.circle(size, extent=100)
    jake.right(300)
    jake.circle(size, extent=100)
    jake.end_fill()
    jake.penup()

    jake.goto(-15, 40)
    jake.pendown()
    jake.begin_fill()
    jake.right(10)
    jake.left(50)
    jake.circle(size, extent=100)
    jake.right(300)
    jake.circle(size, extent=100)
    jake.end_fill()
    jake.penup()

    jake.goto(-17, 55)
    jake.pendown()
    jake.begin_fill()
    jake.right(10)
    jake.left(50)
    jake.circle(size, extent=100)
    jake.right(300)
    jake.circle(size, extent=100)
    jake.end_fill()
    jake.penup()

    jake.goto(-13, 70)
    jake.pendown()
    jake.begin_fill()
    jake.right(10)
    jake.left(50)
    jake.circle(size, extent=100)
    jake.right(300)
    jake.circle(size, extent=100)
    jake.end_fill()
    jake.penup()
    

def sad(a, b):
    mulan = turtle.Turtle() 
    mulan.hideturtle()
    mulan.color("black")   
    mulan.penup()
    mulan.goto(a, b)
    mulan.pendown()
    mulan.right(-90)
    mulan.circle(5, extent= 180)

    mulan.penup()
    mulan.pensize(5)
    mulan.goto(a+5, b+15)
    mulan.pendown()
    mulan.dot()

    mulan.penup()
    mulan.pensize(5)
    mulan.goto(a-15, b+15)
    mulan.pendown()
    mulan.dot()



    
def happy(a, b):
    belle = turtle.Turtle() 
    belle.hideturtle()
    belle.color("black")   
    belle.penup()
    belle.goto(a, b)
    belle.pendown()
    belle.right(-90)
    belle.circle(5, extent= -180)

    belle.penup()
    belle.pensize(5)
    belle.goto(a+5, b+15)
    belle.pendown()
    belle.dot()

    belle.penup()
    belle.pensize(5)
    belle.goto(a-15, b+15)
    belle.pendown()
    belle.dot()


def neutral(a, b):
    belle = turtle.Turtle() 
    belle.hideturtle()
    belle.color("black")   
    belle.penup()
    belle.goto(a - 10, b)
    belle.pendown()
    belle.goto(a, b)
    

    belle.penup()
    belle.pensize(5)
    belle.goto(a+5, b+15)
    belle.pendown()
    belle.dot()

    belle.penup()
    belle.pensize(5)
    belle.goto(a-15, b+15)
    belle.pendown()
    belle.dot()


def drawMiddle():

    tegan = turtle.Turtle()
    tegan.hideturtle()
    tegan.fillcolor("gold1")
    tegan.color("gold1")
    tegan.speed(000000)

    tegan.pensize(20)
    tegan.penup()
    tegan.goto(-2, 37)
    tegan.pendown()
    tegan.fillcolor("gold1")
    tegan.begin_fill()
    tegan.circle(17)
    tegan.end_fill()




