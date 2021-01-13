from graphics import *
import math

# 500x500 window
win = GraphWin(width=500, height=500) # create a window
# Set scale of the window
win.setCoords(0, 0, 500, 500) # set the coordinates of the window; bottom left is (0, 0) and top right is (10, 10)

# Self-explanatory
def drawTriangle(x, y, size):
    xOff, yOff = getXYOffset(size)
    p1 = Point(x, y)
    p2 = Point(x-xOff, y-yOff)
    p3 = Point(x+xOff, y-yOff)
    tri = Polygon(p1, p2, p3)
    tri.draw(win)

# Helper method to keep things cleaner
def getXYOffset(size):
    xOff = size / 2
    yOff = size * math.sqrt(3) / 2
    return xOff, yOff

# Recursive method
def sierpinski(x, y, size, order):
    # Base case
    if order == 0:
        drawTriangle(x, y, size)
    # Recursive case
    else:
        xOff, yOff = getXYOffset(size/2)
        sierpinski(x, y, size/2, order-1)
        sierpinski(x-xOff, y-yOff, size/2, order-1)
        sierpinski(x+xOff, y-yOff, size/2, order-1)

sierpinski(250, 450, 400, 6)

win.getMouse() # pause before closing
