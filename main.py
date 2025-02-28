import turtle
import random



# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Bouncing Ball Animation")

# Create a Turtle object for drawing the ball
ball = turtle.Turtle()
ball.shape("circle")
ball.color("blue")
ball.penup()
ball.goto(0, -200)
ball.speed(0)

# Display bounce counter
counter = turtle.Turtle()
counter.hideturtle()
counter.penup()
counter.goto(-180, 220)
counter.color("white")

# Set initial ball movement parameters
ball.dx = 2
ball.dy = 2
bounce_count = 0

# Function to update bounce counter
def update_counter():
    counter.clear()
    counter.write(f"Bounces: {bounce_count}", font=("Arial", 14, "bold"))

# Function to change ball color
def change_color():
    colors = ["red", "green", "yellow", "purple", "orange", "white", "pink"]
    ball.color(random.choice(colors))

# Animation loop
while True:
    # Move the ball
    ball.sety(ball.ycor() + ball.dy)
    ball.setx(ball.xcor() + ball.dx)

    # Bounce the ball off the top and bottom
    if ball.ycor() > 200:
        ball.sety(200)
        ball.dy *= -1
        bounce_count += 1
        update_counter()
        change_color()
        ball.dy *= 1.1  # Increase speed

    if ball.ycor() < -200:
        ball.sety(-200)
        ball.dy *= -1
        bounce_count += 1
        update_counter()
        change_color()
        ball.dy *= 1.1

    # Bounce the ball off the sides
    if ball.xcor() > 200:
        ball.setx(200)
        ball.dx *= -1
        bounce_count += 1
        update_counter()
        change_color()
        ball.dx *= 1.1

    if ball.xcor() < -200:
        ball.setx(-200)
        ball.dx *= -1
        bounce_count += 1
        update_counter()
        change_color()
        ball.dx *= 1.1

screen.mainloop()
