"""
Created on Thu Sep 15 11:39:56 2020
PC04 start code
@author: YOUR NAME HERE

********* HEY, READ THIS FIRST **********

This is a description of the code that is written out below.

This code is meant to generate different shapes of different amount of sides, different sizes, and different colors everytime you run the code.

"""
import turtle
import math, random

turtle.colormode(255)
# turtle.tracer(0) # uncomment this line to turn off turtle's animation. You must update the image yourself using panel.update() (line 42)

# Create a panel to draw on. 
panel = turtle.Screen()
w = 700 # width of panel
h = 700 # height of panel
panel.setup(width=w, height=h) #600 x 600 is a decent size to work on. 
#You can experiment by making 

# You must make 2 turtle variables
# You must use 2 for loops (a nested for loop counts as 2!)
# You must use at least 1 random element (something from the random library)
# Don't forget to comment your code! (what does each for loop do? What does the random function you'll use do?)

# =============== ADD YOUR CODE BELOW! =================
randomShape = turtle.Turtle()
colorPalletBG = [(0,0,255), (0,255,255), (0, 204,255),(0,255,0),(0,128,0),(51,153,102)]
sizePallet = [(50),(40),(30),(20),(10)]
sidesPallet = [(3),(4),(5),(6)]

size = random.choice(sizePallet)
sides = random.choice(sidesPallet)
angle = 360/sides
inc = 10
numIt = int(360/inc)
innerCirc = 10
for k in range(12):
    randomShape.goto(random.randint(-200,200),random.randint(-200,200))
    randomShape.color(random.choice(colorPalletBG))
    randomShape.down()
    for i in range(sides):
        randomShape.forward(size)
        randomShape.right(angle)
    randomShape.up()
    randomShape.forward(innerCirc)
    randomShape.right(inc)
    
randomFilledShape = turtle.Turtle()
for p in range(12):
    randomFilledShape.goto(random.randint(-200,200),random.randint(-200,200))
    randomFilledShape.color(random.choice(colorPalletBG))
    randomFilledShape.begin_fill()
    for j in range(sides):
        print(18)
        randomShape.down()
        randomFilledShape.forward(size)
        randomFilledShape.right(angle)
    randomFilledShape.end_fill()
    randomFilledShape.forward(innerCirc)
    randomFilledShape.right(inc)
    randomFilledShape.up()



# panel.update() # uncomment this if you've turned off animation (line 26). I recommend leaving this outside of loops, for now.
# =================== CLEAN UP =========================
# uncomment the line below when you are finished with your code (before you turn it in)

