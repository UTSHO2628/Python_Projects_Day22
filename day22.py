import turtle

# সেটআপ
screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Python Logo")
pen = turtle.Turtle()
pen.speed(10)

# Function to draw rounded rectangles
def draw_half_logo(color, x, y, rotate):
    pen.penup()
    pen.goto(x, y)
    pen.setheading(rotate)
    pen.pendown()
    pen.fillcolor(color)
    pen.begin_fill()

    # Draw the main body
    pen.forward(100)
    pen.circle(50, 90)
    pen.forward(150)
    pen.circle(50, 90)
    pen.forward(50)
    pen.right(90)
    pen.forward(50)
    pen.right(90)
    pen.forward(50)
    pen.circle(-50, 90)
    pen.forward(100)
    pen.circle(-50, 90)
    pen.end_fill()

    # Draw the cut-out rectangle
    pen.penup()
    pen.goto(x + 100, y - 25)
    pen.setheading(rotate)
    pen.pendown()
    pen.fillcolor("white")
    pen.begin_fill()
    pen.forward(50)
    pen.right(90)
    pen.forward(20)
    pen.right(90)
    pen.forward(50)
    pen.right(90)
    pen.forward(20)
    pen.end_fill()

# Draw the eyes
def draw_eye(x, y):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.dot(25, "white")

# Draw yellow part
draw_half_logo("gold", -50, 50, 90)

# Draw blue part
draw_half_logo("blue", 50, -150, 270)

# Draw eyes
draw_eye(-70, 100)  # Top eye
draw_eye(70, -100)  # Bottom eye

# Hide the turtle
pen.hideturtle()
screen.mainloop()
