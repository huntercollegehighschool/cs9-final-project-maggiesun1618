#Use of this page is optional. If you use code here, make sure either import page2 or from page2 import * appear on your main.py page.

import turtle

thing = turtle.Turtle()
thing.penup()
thing.setpos(-20,-70)

def draw_gallow(x, color):
  x.pendown()
  x.fillcolor(color)
  x.right(180)
  x.forward(80)
  x.right(180)
  x.forward(20)
  x.left(90)
  x.forward(150)
  x.right(90)
  x.forward(50)
  x.right(90)
  x.forward(20)
  x.penup()

def draw_head(x,color):
  x.pendown()
  x.right(90)
  x.fillcolor(color)
  x.circle(15)
  x.penup()

def draw_spine(x,color):
  x.setpos(-30,30)
  x.pendown()
  x.fillcolor(color)
  x.left(90)
  x.forward(50)
  x.penup()

def draw_leftarm(x,color):
  x.pendown()
  x.fillcolor(color)
  x.setpos(-30,10)
  x.right(120)
  x.forward(30)
  x.penup()

def draw_rightarm(x,color):
  x.pendown()
  x.fillcolor(color)
  x.setpos(-30,10)
  x.right(120)
  x.forward(30)
  x.penup()

def draw_leftleg(x, color):
  x.setpos(-30,-20)
  x.pendown()
  x.fillcolor(color)
  x.right(180)
  x.forward(30)
  x.penup()

def draw_rightleg(x, color):
  x.setpos(-30,-20)
  x.pendown()
  x.fillcolor(color)
  x.left(120)
  x.forward(30)
  x.penup()

def draw_lefteye(x,color):
  x.setpos(-35,50)
  x.pendown()
  x.fillcolor(color)
  x.circle(1)
  x.penup()

def draw_righteye(x,color):
  x.setpos(-25,50)
  x.pendown()
  x.fillcolor(color)
  x.circle(1)
  x.penup()

def draw_mouth(x,color):
  x.setpos(-35,40)
  x.pendown()
  x.fillcolor(color)
  x.left(30)
  x.forward(10)
  x.penup()
  x.setpos(0,0)