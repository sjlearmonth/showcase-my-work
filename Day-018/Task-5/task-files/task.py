# Day 18 - Task 5 - Draw a Spirograph.

# Import the Turtle class and Screen class from the turtle module.
from turtle import Turtle, Screen

# Import the random class from the Random module.
from random import randint

# Import custom module to save screen image content to a .png file.
from save import *

# Create object instance of Turtle class.
timmy_the_turtle = Turtle()

# Set turtle speed to the fastest.
timmy_the_turtle.speed('fastest')

# Set starting position of turtle to face "West".
timmy_the_turtle.screen.mode("standard")
timmy_the_turtle.home()
timmy_the_turtle.setheading(180)

# Create object instance of the Screen class.
screen = Screen()

# Set the color mode.
screen.colormode(255)

# Define a function to generate a random color.
def generate_random_color():

    red = randint(0, 255)

    green = randint(0, 255)

    blue = randint(0, 255)

    return red, green, blue

# Define a function to draw a spirograph pattern.
def draw_spirograph():

    for _ in range(0, 59):

        color = generate_random_color()

        timmy_the_turtle.pencolor(color)

        timmy_the_turtle.circle(50, 360)

        timmy_the_turtle.circle(100, 6)

    return

# Call the function to draw the spirograph pattern.
draw_spirograph()

# Call function to save screen image.
save_image(screen, "Spirograph")

# Configure the screen to exit the program when clicked.
screen.exitonclick()


