import turtle
import pyautogui
import time 
import math 

def draw_hands(turt: turtle.Turtle(), color: str, length: int, degree: int):

    turt.penup()
    turt.goto(0, 0)
    turt.color(color)
    # turtle points straight up
    turt.setheading(90)

    # rotate to correct spot
    turt.rt(degree)
    turt.pendown()
    # draw the turtle
    turt.fd(length)

    turt.penup()
   

# get the user screen size
width, height= pyautogui.size()

# create new window obj
window = turtle.Screen()

# i want to make a square shape hence, i will find the least of the two width and height values and just use the half of that
dimension = width if width < height else height
# idk arbitrary size i like this one the most on my computer
window.setup(width = dimension // 3 * 2, height = dimension // 3 * 2)

# gray-ish
# jk changed to black since unsure why turtle still shows despite turtle.hideturtle() so background will match turtle color
window.bgcolor("#000000")
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

# error handling so when you close there is no error
# error happens since when you close, the loop continues and might try to draw something to the screen that isnt there
running = True
canvas = window.getcanvas()
root = canvas.winfo_toplevel()

def on_close():
    global running
    running = False

root.protocol("WM_DELETE_WINDOW", on_close)

while running:
    if not running:
        # not sure if I need to have this before every action but it isn't causing any errors when I close the window now
        # just delays which is fine!
        break
    # now draw the circle for the clock
    # since dimension is the width of the entire screen, we want our radius to be less than half the screen so it shows
    # //4 is the first one that shows it all so I will use that since it is also even!
    turt.up()
    turt.goto(0, dimension//4)
    turt.setheading(180)
    # neon green
    turt.color("#6ceb85")
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


    turt.pensize(5)
    # now draw the hands
    # moved code for minute above hour so I can better adjust the hour hand
    # care %m gives month 1-12 while %M gives time 0-59
    minute = int(time.strftime("%M"))
    draw_hands(turt, "#eb2876", dimension//7, minute/60*360)

    # draw hour hand
    # hour var will be 1-12 -> so use %I since %H is 0-23
    hour = int(time.strftime("%I"))
    # so we have hour, 1-12 then divide by 12 the times 360 to get the degree
    # have turt point straight up first to have it be 0 degrees
    # ex: hour 12: 12/12 = 1 * 360 = 360 --> points directly up
    # how can make it so the hour moves slightly depending on where the minute is?
    # so add x degrees based on minute degrees? div 12 --> yup works perfectly!
    draw_hands(turt, "#b8b0b0", dimension//11, hour/12*360 + minute/60*360/12)

    # gives 0-61
    # apparently for leap seconds pretty interesting
    second = int(time.strftime("%S"))
    draw_hands(turt, "#4cb7f5", dimension//5, second/60*360)

    # now to wait a second before updating
    # clear the screen
    # need to call update remember since tracer(0)
    # also reset pensize to 3 for the borders
    window.update()
    turt.pensize(3)
    time.sleep(1)
    turt.clear()
    

# no need for window.mainloop() since i call window.update()
# print("Good bye!")
