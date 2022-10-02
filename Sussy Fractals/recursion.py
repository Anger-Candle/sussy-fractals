import turtle
tur = turtle.Turtle()

# PARAMETERS AND INITIAL POSITION

tur.speed(-1)
tur.getscreen().bgcolor("black")
tur.color("cyan")
tur.pensize(2)

# INPUTS (OR THINGS THAT SHOULD BE)
length = 400
angle = 90
sides = 4
level = 10 # NUMBER OF RECURSIONS
count = level

tur.penup()
tur.back(length/2)
tur.right(90)
tur.forward(length/2)
tur.left(90)
savedposA = []
savedposB = []

def PolygonCountToA(length, angle, sides):
    tur.pendown()
    tur.color("red")
    while sides != 0:
        sides = sides - 1
        savedposA.append(tur.pos())
        tur.forward(length)
        tur.left(angle)

def PolygonCountToB(length, angle, sides):
    tur.pendown()
    tur.color("orange")
    while sides != 0:
        sides = sides - 1
        savedposB.append(tur.pos())
        tur.forward(length)
        tur.left(angle)

while count != 0:
    count = count - 1
    PolygonCountToA(length, angle, sides)
    length = length/2
    tur.right(angle)
    while len(savedposA) != 0:
        tur.penup()
        tur.color("blue")
        tur.goto(savedposA[0])
        tur.left(angle)
        savedposA = savedposA[1:]
        tur.pendown()
        PolygonCountToB(length, angle, sides)
    length = length/2
    while len(savedposB) != 0:
        tur.penup()
        tur.color("orange")
        tur.goto(savedposB[0])
        tur.left(angle)
        savedposB = savedposB[1:]
        tur.pendown()
        PolygonCountToA(length,angle,sides)


turtle.done()