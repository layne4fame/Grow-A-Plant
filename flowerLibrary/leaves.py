#!/usr/bin/env python3

import turtle
import time

#a should be 5 if using drawstem
def drawleafNeutralRIGHT(a, b):
    leaf = turtle.Turtle()
    leaf.speed(000)
    leaf.hideturtle()
    leaf.pensize(5)
    leaf.color("lightgreen")
    leaf.penup()
    leaf.goto(a, b)
    leaf.pendown()
    leaf.begin_fill()
    leaf.fillcolor("lightgreen")
    leaf.circle(20, extent = 100)
    leaf.goto(a, b+10)
    leaf.goto(a, b)
    leaf.end_fill()


def drawleafSadRIGHT(a, b):
    leaf = turtle.Turtle()
    leaf.speed(000)
    leaf.hideturtle()
    leaf.pensize(5)
    leaf.color("yellow")
    leaf.penup()
    leaf.goto(a, b)
    leaf.pendown()
    leaf.begin_fill()
    leaf.fillcolor("yellow")
    leaf.circle(20, extent = 100)
    leaf.goto(a, b+10)
    leaf.goto(a, b)
    leaf.end_fill()


def drawleafHappyRIGHT(a, b):
    leaf = turtle.Turtle()
    leaf.speed(000)
    leaf.hideturtle()
    leaf.pensize(5)
    leaf.color("LimeGreen")
    leaf.penup()
    leaf.goto(a, b)
    leaf.pendown()
    leaf.begin_fill()
    leaf.fillcolor("LimeGreen")
    leaf.circle(20, extent = 100)
    leaf.goto(a, b+10)
    leaf.goto(a, b)
    leaf.end_fill()

#a should be -5 if using drawstem
def drawleafNeutralLEFT(a, b):
    leaf = turtle.Turtle()
    leaf.speed(000)
    leaf.hideturtle()
    leaf.pensize(5)
    leaf.color("lightgreen")
    leaf.penup()
    leaf.goto(a, b)
    leaf.pendown()
    leaf.begin_fill()
    leaf.fillcolor("lightgreen")
    leaf.circle(20, extent = -100)
    leaf.goto(a, b+10)
    leaf.goto(a, b)
    leaf.end_fill()


def drawleafSadLEFT(a, b):
    leaf = turtle.Turtle()
    leaf.speed(000)
    leaf.hideturtle()
    leaf.pensize(5)
    leaf.color("yellow")
    leaf.penup()
    leaf.goto(a, b)
    leaf.pendown()
    leaf.begin_fill()
    leaf.fillcolor("yellow")
    leaf.circle(20, extent = -100)
    leaf.goto(a, b+10)
    leaf.goto(a, b)
    leaf.end_fill()


def drawleafHappyLEFT(a, b):
    leaf = turtle.Turtle()
    leaf.speed(000)
    leaf.hideturtle()
    leaf.pensize(5)
    leaf.color("LimeGreen")
    leaf.penup()
    leaf.goto(a, b)
    leaf.pendown()
    leaf.begin_fill()
    leaf.fillcolor("LimeGreen")
    leaf.circle(20, extent = -100)
    leaf.goto(a, b+10)
    leaf.goto(a, b)
    leaf.end_fill()
