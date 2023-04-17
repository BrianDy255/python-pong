from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from borders import *
import time
from tkinter import *
from tkinter import messagebox


def game_start():
    #creating the window size for the game
    screen = Screen()
    screen.bgcolor('black')
    screen.title("Brian's Pong Game")
    screen.setup(width=850,height=650)
    screen.tracer(0)

    #create the borders of the screen
    border_top = Border_top()
    border_bottom = Border_bottom()

    #Print welcome intro
    messagebox.showinfo("Lets get ready to play!", "A simple Pong game created in python using the Turtle library. \n\nFirst to 3 wins")

    #creating the classes for the game
    r_paddle = Paddle((350,0))
    l_paddle = Paddle((-350,0))
    ball = Ball()
    scoreboard = Scoreboard()

    # onscreen event listeners
    screen.listen()
    screen.onkeypress(r_paddle.go_up, 'Up')
    screen.onkeypress(r_paddle.go_down, 'Down')
    screen.onkeypress(l_paddle.go_up, 'w')
    screen.onkeypress(l_paddle.go_down, 's')

    game_is_on = True
    while game_is_on:
        time.sleep(ball.move_speed) #sets a timer for updating the values on the screen
        screen.update() #updates the screen every iteration to show "movement"
        ball.move()

        #detecting collision
        if ball.ycor() > 280 or ball.ycor() < -280:
            # needs to bounce
            ball.bounce_y()

        #detect collision with r_paddle
        if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
            ball.bounce_x()

        #R sided paddle miss
        if ball.xcor() > 350:
            ball.reset_position()
            scoreboard.l_point()

        #L sided paddle miss
        if ball.xcor() < -350:
            ball.reset_position()
            scoreboard.r_point()

        # set win condition
        if scoreboard.l_score == 3:
            messagebox.showinfo("Game Over", "Player One wins!")
            game_is_on = False
        if scoreboard.r_score == 3:
            messagebox.showinfo("Game Over", "Player Two wins!")
            game_is_on = False

    #create an instance to replay the game
    if game_is_on is False:
        is_continue= messagebox.askquestion("Continue", "Would you like to play again?")
        if is_continue == "yes":
            game_is_on = True
            screen.clear()
            game_start()
        else:
            print("Thanks for playing this simple classic game")

    #prevents screen from closing automatically
    screen.exitonclick()

game_start()