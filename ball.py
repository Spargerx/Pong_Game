from turtle import Turtle
import random

BALL_STEP = 10

class Ball(Turtle):
    
    def __init__(self, shape = "circle"):
        super().__init__(shape)
        self.color("White")
        self.penup()
        self.move_speed = 0.06 ## Movement speed of the ball
        
    def set_direction(self):
        ranges = [(25, 65), (115, 155), (205, 245), (295, 335)]
        low, high = random.choice(ranges)
        angle = random.randint(low, high)
        self.setheading(angle)
        
    def move(self):
        self.forward(BALL_STEP)
        
    def ball_wall_bounce(self):
        new_heading = 360 - self.heading()
        self.setheading(new_heading % 360)
            
    def ball_paddle_bounce(self):
        new_heading = 180 - self.heading()
        self.setheading(new_heading % 360)
        self.increase_speed()
        self.forward(10)
        
    def reset_position(self):
        self.goto(0,0)
        self.move_speed = 0.06 # change speed
        
    def increase_speed(self):
        self.move_speed *= 0.9

