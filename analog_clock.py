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

# gray-ish
window.bgcolor("#454441")
window.title("Clock ig")

# this means that the turtle will not make its little drawing animation
# essentially you have to call .update to show
# since we are doing a clock, we do not want a drawing animation, we want the little clock to move instantly!
# window.tracer(0)
# this breaks the circle weirdy??

pen = turtle.Turtle()
# pen.hideturtle()
pen.speed(0)
pen.pensize(3)
pen.hideturtle()

# now draw the circle for the clock
# since dimension is the width of the entire screen, we want our radius to be less than half the screen so it shows
# //4 is the first one that shows it all so I will use that since it is also even!
pen.up()
pen.goto(0, dimension//4)
pen.setheading(180)

# neon green
pen.color("#00ff22")
pen.pendown()
pen.circle(dimension//4)


window.mainloop()
