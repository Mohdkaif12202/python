import turtle

# Create a turtle pen
pen = turtle.Turtle()

# Draw a square
for _ in range(4):
    pen.forward(100)  # move forward
    pen.right(90)     # turn right
    pen.right(90)     # turn right

turtle.done()
