# Day 18 - Task 6 - Draw a Hirst Spot Painting

In this task I used all my knowledge of the Python programming lnaguage to write a program which would draw my own version of a Damien Hirst spot painting.

I first of all wrote a helper Python function called;

```
extract_colors(...)
```
in the Python file;
```
extract.py
```
to extract the 10 most common colors in a Damien Hirst spot painting from a .jpg image file passed as an argument to the function in the parameter "image-file" and save them as a text file of three integer strings per line, using another Python helper function;
```
write(...)
```
I later created a third helper Python function;
```
read(...)
```
in the same Python file which reads the text file and creates a Python List of integer tuples of three values each from 0 to 255, corresponding to the red, green and blue components of the 10 most common colors.

The final function;
```
draw_hirst_painting(...)
```
in the Python file;
```
task.py
```
calls the
```
read(..)
```
function to read a text file of color string integer values and create the List of color integer tuples to draw a 10 by 10 grid of spots of diameter 20 units spaced 50 units apart, each spot color selected randomly from the List of color integer values.

Finally the Python function;
```
save_image(...)
```
in the Python file;
```
save.py
```
saves the Hirst spot painting on the screen GUI to a .png image file of the image content of the turtle screen to a .png image file which can be viewed [here](https://github.com/sjlearmonth/100-Days-of-Code---The-Complete-Python-Pro-Bootcamp/blob/d0d095c0aadb6bb2d4e64450ba6f352b98174b9d/Day-011...020/Day-018/Task-6/image-files/my-hirst-painting.png).

