## STEP 1 ##

import turtle

t = turtle.Turtle()

t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)

## STEP 2 ##

import turtle

t = turtle.Turtle()

def forwardRight():
    t.forward(100)
    t.right(90)

forwardRight()
forwardRight()
forwardRight()
forwardRight()

## STEP 3 ## 

import turtle

t = turtle.Turtle()

def forwardRight():
    t.forward(100)
    t.right(90)

for i in range(4):
    print(i)
    forwardRight()