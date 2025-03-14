# Day 18 - Task 6 - Draw a Hirst Painting.

# Import the colorgram module.
import colorgram

# Define a function to extract colors from an image and return them in a List.
def extract_colors( image_file ):
    """
    This function uses the extract(...) function in the colorgram module
     to extract the ten most common colors in a .jpg image file.

     The colors are contained inside a Python List of integer tuples in the form
     (red, green, blue) where red, green and blue are integer values in the range 0...255.

    :param image_file:
    :return: rgb_colors
    """

    # Extract the 10 most common colors from an image of a Hirst spotty painting.
    colors = colorgram.extract( "../image-files/" + image_file, 10)

    # Create an empty Lit for rgb color tuples.
    rgb_colors = []

    # Loop through each color in the extracted color list.
    for color in colors:

        # Get the next red color value.
        red = color.rgb.r

        # Get the next green color value.
        green = color.rgb.g

        # Get the next blue color value.
        blue = color.rgb.b

        # Create the next tuple of extracted colors.
        rgb = red, green, blue

        # Append the next color tuple to the list.
        rgb_colors.append(rgb)

    return rgb_colors

# Define a functon to open a text file for writing a Python List of integer tuples.
def write(data, filename):
    """
    Writes a Python List of integer tuples in the parameter "data" to a text file whose filename
     is the parameter "filename".

    :param data:
    :param filename:
    :return:
    """

    # Open a text file for writing.
    with open("../data-files/" + filename, 'w') as f:

        # Loop through each tuple item in the list.
        for item in data:

            # Convert the next integer tuple to a string tuple.

            item_string = str(item[0]) + " " + str(item[1]) + " " + str(item[2])

            # Write the next string tuple to the text file.
            f.write('%s\n' % item_string)

    # Close the text file.
    f.close()

# Define a function to open a text file for reading lines of string tuples.
def read(filename):
    """
    This function opens a text file specified by the parameter "filename" for reading
    lines of string tuples and saves them as integer tuples in a Python list which it returns.

    :param filename:
    :return: color_tuples
    """

    # Initialise an empty Python List for integer tuples.
    color_tuples = []

    # open text file for reading lines of text.
    f = open("../data-files/" + filename, 'r')

    # Loop through each line in the text file.
    for item in f.readlines():

        # Create string tuple from the next line in the text file, removing spaces.
        string_tuple = item.split()

        # Create the next integer tuple from the string tuple.
        int_tuple = int(string_tuple[0]), int(string_tuple[1]), int(string_tuple[2])

        # Append the next integer tuple to the Python List.
        color_tuples.append(int_tuple)

    # close the file.
    f.close()

    # Return the Python List of integer tuples.
    return color_tuples

# Call the function to extract colors from image file.
extracted_colors = extract_colors(image_file = "hirst-painting.jpg")

# Write the extracted colors to a text file.
write(data = extracted_colors, filename = "hirst.dat")

