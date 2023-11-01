#CS175
#Sashank Vaddiparty
#Turtle_Stop_Sign

import turtle  # Quick import of lib to draw turtle
import math

length = 200

def draw_border():
    length = 170
    s = turtle.Turtle()
    x = length / math.sqrt(2)
    diameter = length + (2 * x)
    starting_point_x = -diameter / 2 + x
    starting_point_y = -length / 2
    
    s.goto(starting_point_x, starting_point_y)
    s.pensize(10)  # Thicker line for border
    s.color("white")
    s.shape("turtle")

    for x in range(8):
        s.forward(length)
        s.left(45)
    
    s.hideturtle()


def draw_sign():
    length = 200
    s = length 
    x = s / math.sqrt(2)
    diameter = s + (2 * x)
    starting_point_x = -diameter / 2 + x
    starting_point_y = -s / 2
    s = turtle.Turtle()
    s.goto(starting_point_x, starting_point_y)
    s.pensize(3)
    s.color("red")
    s.shape("turtle")

    s.begin_fill()
    for x in range(8):
        s.forward(length)
        s.left(45)
    s.end_fill()
    s.penup()
    s.goto(25,-200)
    s.left(90)


def draw_pole():
    p = turtle.Turtle()
    p.pensize(15)
    p.color("black")
    p.shape("turtle")
    p.goto(0, -length/2 - 20)  # Starting just below the sign
    p.setheading(-90)  # Pointing downwards
    p.forward(300)  # Length of pole
    p.hideturtle()

def write_sign():
    t = turtle.Turtle()
    t.pensize(3)
    t.color("#FFFFFF")
    t.shape("classic")
    t.penup()
    t.goto(-90, 90)
    t.write("STOP", font=("Impact", 70))
    t.hideturtle()

#Calling the functions.
draw_sign()
draw_border()
write_sign()
draw_pole()

turtle.done()  # To keep the window open after drawing
