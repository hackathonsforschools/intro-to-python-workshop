import turtle

t = turtle.Turtle()

def drawSquare():
    for i in range(4):
        t.forward(100)
        t.right(90)

def drawTriangle():
    for i in range(3):
        t.forward(100)
        t.right(120)

print('''
Choose any of the three following shapes to draw...
1. Square
2. Triangle
3. Circle

If you enter none of the above, a line will be drawn.
''')

choice = int(input("Pick your choice (enter number 1-3) > "))

if (choice == 1):
    drawSquare()
elif (choice == 2):
    drawTriangle()
elif (choice == 3):
    t.circle(50) # no need for a function - it's one line
else:
    t.forward(100) # same reasoning here - it's one line