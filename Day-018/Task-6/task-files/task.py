# Day 18 - Task 6 - Draw a Hirst Painting.

# Import the turtle class from the turtle module.
from turtle import Turtle, Screen

# Import the random class from the Random module.
from random import choice

# Import custom module to save screen image content to a .png file.
from save import save_image

# Import the custom extract module.
from extract import read

# Create object instance of Turtle class.
timmy_the_turtle = Turtle()

# Set turtle speed to the fastest.
timmy_the_turtle.speed('fastest')

# Create object instance of the Screen class.
screen = Screen()

# Set the color mode.
screen.colormode(255)

# Define a function to draw my own Hirst spot painting.
def draw_hirst_painting( filename ):
    """
    This function has parameter "filename" which is a text file of
    string integer values of the ten most common colors found in a
    Hirst spot painting and draws spots of diameter 20, 50 units apart
    in a 10 x 10 grid with each spot having a different color randomly sellected
    from the text file.

    :param filename:
    :return:
    """

    # Read the text file  and save each line of text as an integer tuple ina Python List.
    colors = read(filename = filename)

    # Raise the turtle pen as no drawing is required.
    timmy_the_turtle.penup()

    # Move the turtle left of center.
    timmy_the_turtle.backward( 4 * 50 + 25)

    # Turn right 90 degrees.
    timmy_the_turtle.right(90)

    # Move the turtle half way down turtle GUI screen.
    timmy_the_turtle.forward( 4 * 50 + 25 )

    # Turn left 90 degrees ready to start drawing the first spot at bottom left-hand corner.
    timmy_the_turtle.left(90)

    # Loop through each row from bottom to top.
    for row in range(10):

        # Loop through each row column from left to right.
        for col in range(10):

            # Get the next random color.
            next_random_color = choice(colors)

            # Draw the next spot with the next random color.
            timmy_the_turtle.dot(20, next_random_color)

            # Is it the first or 9th column yet?
            if col < 9:

                # Yes, so move turtle forward ready to draw the next spot.
                timmy_the_turtle.forward(50)

            # No, it is the last spot on this row.
            else:

                # Position turtle ready to start drawing spots for the next row starting at the first column.
                timmy_the_turtle.left(90)

                timmy_the_turtle.forward(50)

                timmy_the_turtle.left(90)

                timmy_the_turtle.forward(col * 50)

                timmy_the_turtle.right(90)

                timmy_the_turtle.right(90)

# Call the Python function to draw a Hirst spot painting
draw_hirst_painting("hirst.dat")

# Call function to save the turtle GUI screen.
save_image(screen, "my-hirst-painting")

# Configure the screen to exit the program when clicked.
screen.exitonclick()









