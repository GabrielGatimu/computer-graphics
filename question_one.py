import turtle

# Setup the turtle screen
screen = turtle.Screen()
screen.title("Basic Graphics Constructions")
screen.bgcolor("white")

# Create a turtle instance
t = turtle.Turtle()
t.speed(2)  # Set the turtle speed

# Draw a line
t.penup()
t.goto(-100, 100)
t.pendown()
t.forward(200)

# Draw a circle
t.penup()
t.goto(100, 100)
t.pendown()
t.circle(50)

# Draw an arc
t.penup()
t.goto(-100, -100)
t.pendown()
t.setheading(-45)
t.circle(100, 90)

# Draw an ellipse
t.penup()
t.goto(100, -100)
t.pendown()
t.setheading(0)
t.circle(80, 90)
t.circle(80, 90)

# Draw a rectangle
t.penup()
t.goto(-100, 0)
t.pendown()
t.setheading(0)
for _ in range(2):
    t.forward(100)
    t.right(90)
    t.forward(50)
    t.right(90)

# Hide the turtle
t.hideturtle()

# Exit on click
turtle.done()
