from turtle import Screen
import time
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

TOP_WALL = 275
BOTTOM_WALL = -275


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")

screen.tracer(0) #turns off the animation

r_paddle = Paddle((380, 0))
l_paddle = Paddle((-388, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()

screen.onkey(r_paddle.move_up,"Up")
screen.onkey(r_paddle.move_down, "Down")
screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")

ball.set_direction()

game_is_on = True
while game_is_on:
    
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    
    # detecting colloisions with top and bottom walls
    if ball.ycor() >= TOP_WALL or ball.ycor() <= BOTTOM_WALL:
        
        ball.ball_wall_bounce()
    

    #detecting collisions with paddles
    collide_with_r_paddle = False
    collide_with_l_paddle = False
    if (r_paddle.xcor()-20 <= ball.xcor() <= r_paddle.xcor()) and (r_paddle.ycor()-50 <= ball.ycor() <= r_paddle.ycor()+50):
        collide_with_r_paddle = True
        
    if (l_paddle.xcor() <= ball.xcor() <= l_paddle.xcor()+20) and (l_paddle.ycor()-50 <= ball.ycor() <= l_paddle.ycor()+50):
        collide_with_l_paddle = True
        
    if collide_with_l_paddle or collide_with_r_paddle:
        ball.ball_paddle_bounce()
        
    if ball.xcor()>=420 or ball.xcor()<=-420:
        if ball.xcor() < 0:
            scoreboard.r_point()
        elif ball.xcor() > 0:
            scoreboard.l_point()
            
        ball.reset_position()
        screen.update()
        time.sleep(1)
        ball.set_direction()
        
    if scoreboard.r_score>=10 or scoreboard.l_score>=10:
        scoreboard.declare_winner()
        game_is_on = False
        
    

screen.exitonclick()