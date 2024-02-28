import turtle

# Create a Turtle object & assign properties:
bob = turtle.Turtle()
bob.shape('turtle')
bob.color('black')
bob.fillcolor('#419f6a')
bob.pensize(3)
bob.speed(10)

# Draw a filled circle:
bob.begin_fill()
bob.circle(100)
bob.end_fill()

# Draw and fill some half-circles:
bob.fillcolor('#3c79b8')
bob.begin_fill()
bob.circle(50,180)
bob.circle(-50,180)
bob.circle(-100, 180)
bob.end_fill()