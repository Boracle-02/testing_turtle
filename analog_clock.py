import turtle
import pyautogui
import time 
import math 

# get the user screen size
width, height= pyautogui.size()

# create new window obj
window = turtle.Screen()

# i want to make a square shape hence, i will find the least of the two width and height values and just use the half of that
dimension = width if width < height else height
# idk arbitrary size i like this one the most on my computer
window.setup(width = dimension // 3 * 2, height = dimension // 3 * 2)


# window.bgcolor("black")
window.title("Clock ig")

# this means that the turtle will not make its little drawing animation
# essentially you have to call .update to show
# since we are doing a clock, we do not want a drawing animation, we want the little clock to move instantly!
window.tracer(0)
# this breaks the circle weirdy??

pen = turtle.Turtle()
# pen.hideturtle()
pen.speed(0)
pen.pensize(3)

# now draw the circle for the clock
pen.up()
pen.goto(0, 210)
pen.setheading(180)
pen.color("green")
pen.pendown()
pen.circle(210)


window.mainloop()
