import turtle as t

# Set up the screen
screen = t.Screen()
screen.bgcolor("white")

# Create a Turtle for drawing the cube
cube = t.Turtle()
cube.speed(1)

# Function to draw a square
def draw_square():
    for _ in range(4):
        cube.forward(100)
        cube.right(90)

# Draw the front square
cube.penup()
cube.goto(-50, -50)
cube.pendown()
cube.begin_fill()
cube.color("blue")
draw_square()
cube.end_fill()

# Draw the back square (shifted for the illusion of depth)
cube.penup()
cube.goto(-30, -30)
cube.pendown()
cube.begin_fill()
cube.color("lightblue")
draw_square()
cube.end_fill()

# Connect the front and back squares
cube.penup()
cube.goto(-50, -50)
cube.pendown()
cube.color("blue")
cube.setheading(150)
cube.forward(50)
cube.setheading(60)
cube.forward(50)
cube.setheading(210)
cube.forward(100)
cube.setheading(90)
cube.forward(20)
cube.setheading(0)
cube.forward(100)

# Hide the turtle
cube.hideturtle()

# Close the window on click
screen.exitonclick()