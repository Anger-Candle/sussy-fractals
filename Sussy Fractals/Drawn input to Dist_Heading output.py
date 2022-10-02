import turtle
import math
from itertools import cycle
from turtle import Turtle, Screen

screen = Screen()

screen.title("Space to save image, Right Click to clear")
t = Turtle("turtle")

t.speed(-1)


def dragging(x, y):
    t.ondrag(None)
    t.setheading((t.towards(x, y)))
    anglesList.append(t.heading())
    t.goto(x, y)

    t.ondrag(dragging)


def clickright(x, y):
    t.clear()
    t.end_poly()
    anglesList.clear()
    t.begin_poly()


def saveImage():
    global coordsList
    t.end_poly()
    screen.bye()
    coordsList = t.get_poly()


def main():
    global anglesList
    anglesList = []
    turtle.listen()
    t.begin_poly()
    t.ondrag(dragging)

    turtle.onscreenclick(clickright, 3)
    turtle.onkey(saveImage, "space")

    screen.mainloop()

    running = True
    rawCoords = cycle(coordsList)
    distanceList = []

    nextPos = next(rawCoords)
    while running:
        thisPos, nextPos = nextPos, next(rawCoords)
        if nextPos == (0.00, 0.00):
            running = False
        else:
            nextDist = math.dist(thisPos, nextPos)

            distanceList.append(round(nextDist))


    return distanceList, anglesList


main()
