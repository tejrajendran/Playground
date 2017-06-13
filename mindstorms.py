import turtle
def draw_square(some_turtle):
    for side in range(1,5):
        some_turtle.forward(100)
        some_turtle.right(90)

def draw_circle(some_turtle):
    some_turtle.circle(100)


def draw_art():
    window = turtle.Screen()
    window.bgcolor("pink")

    circleDrawer = turtle.Turtle()
    circleDrawer.shape("turtle")
    circleDrawer.color("blue")
    draw_circle(circleDrawer)

    squareDrawer = turtle.Turtle()
    squareDrawer.shape("turtle")
    squareDrawer.color("green")
    squareDrawer.speed(4)

    for numSquares in range(1,37):
        draw_square(squareDrawer)
        squareDrawer.right(10)

def draw_initials():
    window = turtle.Screen()
    window.bgcolor("black")

    drawer = turtle.Turtle()
    drawer.shape("turtle")
    drawer.color("blue")

    drawer.penup()
    drawer.goto(10,10)

    drawer.pendown()
    drawer.forward(100)
    drawer.seth(0)
    drawer.goto(55,10)
    drawer.seth(270)
    drawer.forward(150);

    drawer.penup()
    drawer.goto(120,10)
    drawer.pendown()
    drawer.seth(270)
    drawer.forward(150)

    drawer.goto(120,10)
    drawer.seth(180)
    drawer.circle(50,-180)
    drawer.seth(315)
    drawer.forward(50)
#draw_art()
draw_initials()
