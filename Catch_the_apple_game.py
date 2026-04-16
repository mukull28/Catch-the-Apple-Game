import turtle
import random

# Screen setup
screen = turtle.Screen()
screen.title("Catch the Apples Game")
screen.bgcolor("black")
screen.setup(width=600, height=600)

# Player (basket)
player = turtle.Turtle()
player.shape("square")
player.color("brown")
player.shapesize(stretch_wid=1, stretch_len=5)
player.penup()
player.goto(0, -250)

# Falling object (apple)
apple = turtle.Turtle()
apple.shape("circle")
apple.color("red")
apple.penup()
apple.goto(0, 250)

# Score and speed
score = 0
fall_speed = 18   # 🔥 faster starting speed

score_display = turtle.Turtle()
score_display.hideturtle()
score_display.color("white")
score_display.penup()
score_display.goto(0, 260)
score_display.write("Score: 0", align="center", font=("Arial", 16, "bold"))

# Movement functions
def move_left():
    x = player.xcor()
    if x > -250:
        player.setx(x - 25)

def move_right():
    x = player.xcor()
    if x < 250:
        player.setx(x + 25)

# Keyboard binding
screen.listen()
screen.onkey(move_left, "Left")
screen.onkey(move_right, "Right")

# Game loop
def game_loop():
    global score, fall_speed

    # Move apple down
    y = apple.ycor()
    apple.sety(y - fall_speed)

    # Catch condition
    if apple.distance(player) < 50 and apple.ycor() < -220:
        apple.goto(random.randint(-250, 250), 250)
        score += 1
        fall_speed += 0.5   # 🔥 gradually increase speed

        score_display.clear()
        score_display.write(f"Score: {score}", align="center", font=("Arial", 16, "bold"))

    # Miss condition
    if apple.ycor() < -300:
        score_display.goto(0, 0)
        score_display.write("Game Over!", align="center", font=("Arial", 24, "bold"))
        return

    # Win condition
    if score >= 15:
        score_display.goto(0, 0)
        score_display.write("You Win! 🎉", align="center", font=("Arial", 24, "bold"))
        return

    screen.ontimer(game_loop, 50)

# Start game
game_loop()

turtle.done()