from turtle import *
import random as r

xxx = ["red","blue","yellow","orange"]
color("red")
speed(10)
for b in range (10):
    penup()
    goto(r.randint(-100,100),r.randint(-150,100))
    pendown()
    color(r.choice(xxx))
    for b in range (4):
      color("olive")
      forward(100)
      right(90)
