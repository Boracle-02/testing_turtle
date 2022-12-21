import turtle
import pyautogui
import time 
import math 

def draw_hands(color: str, length: int, degree: int):
    pass
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
window.tracer(0)
# this breaks the circle weirdy??
# well not anymore after i drew the other stuff ;-;

turt = turtle.Turtle()
# pen.hideturtle()
turt.speed(0)
turt.pensize(3)
turt.hideturtle()

# now draw the circle for the clock
# since dimension is the width of the entire screen, we want our radius to be less than half the screen so it shows
# //4 is the first one that shows it all so I will use that since it is also even!
turt.up()
turt.goto(0, dimension//4)
turt.setheading(180)

# neon green
turt.color("#00ff22")
turt.pendown()
turt.circle(dimension//4)

# now draw each individual hour tick
# how to draw number? can use png background of clock ngl

turt.penup()
turt.goto(0,0)
turt.setheading(90) # ^

# we are at center, so lets move up x amount, then pendown then back up draw the hour 
# rad is dimmension // 4 so lets have our hand lenghh be dimension // 12
# turt.forward(dimension//4 - dimension//12)
# turt.pendown()
# turt.fd(dimension//12)

# set back to 0,0 turn the turtle 360 // 12 then do same
# can do loop 


for _ in range(12):
    turt.forward(dimension//4 - dimension//30)
    turt.pendown()
    turt.fd(dimension//30)
    turt.penup()
    turt.goto(0,0)
    # rt is rotate in degrees
    turt.rt(360//12)

# now draw the hands
# draw hour hand
# hour var will be 1-12
hour = int(time.strftime("%I"))

turt.color("#6b7af2")

window.mainloop()
