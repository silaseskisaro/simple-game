# player move forever forward
# background a colour
# bubble for player to collect

import turtle
import random
import time

# quick variables

player_speed = 0.2

# making the turtles

player = turtle.Turtle()
enemy = turtle.Turtle()
bubble = turtle.Turtle()
window = turtle.Screen()
display = turtle.Turtle()


# turtle setup
display.penup()
player.penup()

display.hideturtle()
player.hideturtle()
bubble.hideturtle()
enemy.hideturtle()
# introduction

window.bgcolor("sky blue")
display.setposition(-200, 100)
display.write("Use the arrow keys to move left and right", font = ['Arial', 20, 'normal'])

count_down_to_start = 5

display.setposition(-200 , -100)
display.write("The game will start in {} seconds." . format(count_down_to_start), font = ['Arial', 20, 'normal'])

time.sleep(2)

for count in range(5):
    time.sleep(1)
    count_down_to_start = count_down_to_start - 1
    display.clear()
    display.write("The game will start in {} seconds.".format(count_down_to_start), font = ['Arial', 20, 'normal'])

# more turtle setup

display.showturtle()
player.showturtle()
bubble.showturtle()



random_color = ["orange", "sky blue", "green", "red", "purple", "black", "turquoise"]

score = 2

display.clear()
display.setposition(0, 200)

display.write("Score: 0", font = ['Arial', 20, 'normal'])

bubble.color(random.choice(random_color))
enemy.color(random.choice(random_color))
display.hideturtle()
turtle.hideturtle()
enemy.showturtle()
player.color("red")
window.bgcolor("pink")
enemy.shape("square")
player.shape("turtle")
bubble.shape("circle")
enemy.turtlesize(1)
player.turtlesize(2)
enemy.penup()
bubble.penup()
player.penup()

window.tracer(0)

# functions


def forward_faster():
    player.forward(1)


def player_left():
    player.left(15)
    player.forward(1)


def player_right():
    player.right(15)
    player.forward(1)


def bubble_teleport():
    bubble.setx(random.randint(-400, 400))
    bubble.sety(random.randint(-250, 250))
    bubble.color(random.choice(random_color))
    bubble.dot(50)


def enemy_teleport():
    enemy.setx(random.randint(-400, 400))
    enemy.sety(random.randint(-250, 250))
    enemy.color(random.choice(random_color))
    enemy.shape("square")



# movement keys

window.onkeypress(player_left, "Left")
window.onkeypress(player_right, "Right")
window.onkeypress(forward_faster, "Up")
window.listen()

bubble_teleport()
enemy_teleport()
# game loop

while True:
    player.forward(player_speed)

    window.update()
#  if the player is touching bubble teleport

    if player.distance(bubble) < 40:
        bubble.clear()
        bubble_teleport()
        score = score + 2
        display.clear()
        display.write("Score: {}".format(score), font = ["Arial", 20, "normal"])
        enemy.clear()
        enemy_teleport()

#   if player is on the side of the screen teleport

    if player.xcor() > 600:
        player.setx(-600)
    if player.xcor() < -600:
        player.setx(600)
    if player.ycor() > 300:
        player.sety(-300)
    if player.ycor() < -300:
        player.sety(300)
        player.sety(-300)
    if player.ycor() < -300:
        player.sety(300)

# if the enemy is touching bubble teleport

    if enemy.distance(bubble) < 50:
        enemy.clear()
        enemy_teleport()

    if player.distance(enemy) < 40:
        enemy.clear()
        enemy_teleport()
        score = -1
        display.clear()
        display.write("Score: {}".format(score), font=["Arial", 20, "normal"])


    if score < 0:
        player.hideturtle()
        display.clear()
        enemy.hideturtle()
        bubble.hideturtle()
        display.setposition(-70, 0)
        display.write("you died", font=["Arial", 50, "normal"])
        time.sleep(200)



    if score == 10:
       enemy.turtlesize(2)
    if score == 20:
        enemy.turtlesize(4)
    if score > 22:
        player.hideturtle()
        display.clear()
        enemy.hideturtle()
        bubble.hideturtle()
        display.setposition(-70, 0)
        display.write("You Win!!!", font=["Arial", 50, "normal"])
        time.sleep(200)