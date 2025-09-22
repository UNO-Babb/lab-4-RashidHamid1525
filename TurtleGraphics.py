# TurtleGraphics.py
# Name: Rashid
# Date: 9/21/2025
# Assignment: Turtle Graphics Assignment


import turtle  # Needed generally but not in CodeHS
hideturtle()

def drawSquare(myTurtle, size):
    for i in range(4):
        myTurtle.forward(size)
        myTurtle.right(90)

def drawPolygon(tim, sides):
    for s in range(sides):
        tim.forward(50)
        tim.right(360 / sides)

def fillCorner(tom, corner):
    drawSquare(tom, 100)

    if corner == 1:
        tom.begin_fill()
        drawSquare(tom, 50)
        tom.end_fill()

    elif corner == 2:
        tom.forward(50)
        tom.begin_fill()
        drawSquare(tom, 50)
        tom.end_fill()

    elif corner == 3:
        tom.right(90)
        tom.forward(50)
        tom.left(90)
        tom.begin_fill()
        drawSquare(tom, 50)
        tom.end_fill()

    elif corner == 4:
        tom.right(90)
        tom.forward(100)
        tom.left(90)
        tom.forward(50)
        tom.left(90)
        tom.forward(50)
        tom.right(90)
        tom.begin_fill()
        drawSquare(tom, 50)
        tom.end_fill()

def squaresInSquares(sally, squares):
    sally.up()
    sally.goto(-175, 175)
    sally.down()
    drawSquare(sally, 250)
    x = 1
    for q in range(squares - 1):
        x += 40
        sally.up()
        sally.forward(20)
        sally.right(90)
        sally.forward(20)
        sally.left(90)
        sally.down()
        drawSquare(sally, 250 - x)

def main():
    myTurtle = turtle.Turtle()
   

    # Uncomment the function you want to test:
    drawPolygon(myTurtle, 5)  # Draws a pentagon
    # drawPolygon(myTurtle, 8)  # Draws an octagon

    # fillCorner(myTurtle, 2)  # Top right corner filled
    # fillCorner(myTurtle, 3)  # Bottom left corner filled

    # squaresInSquares(myTurtle, 5)  # 5 concentric squares
    # squaresInSquares(myTurtle, 3)  # 3 concentric squares

    myTurtle.hideturtle()
    turtle.done()

main()
