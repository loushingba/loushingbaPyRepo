# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 19:29:01 2020

@author: sanathoi
"""
import turtle
t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("black")
t.pencolor("white")
a=b=0
t.speed(0)
t.penup()
t.goto(0,200)
t.pendown()
while True:
    t.forward(a)
    t.right(b)
    a+=2
    b+=1
    if b==210:
        break
    t.hideturtle()
turtle.done()