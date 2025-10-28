from turtle import Turtle
UP_DOWN_SPEED = 6

class Paddle(Turtle):
    def __init__(self, position, shape = "square"):
        super().__init__(shape)
        self.color("white")
        self.penup()
        self.speed(0)
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.setposition(position)
        self.speed(UP_DOWN_SPEED)
        
    def move_up(self):
        if self.ycor() < 250:
            new_y = self.ycor()+25
            self.goto(self.xcor(), new_y)
            
    def move_down(self):
        if self.ycor() > -250:
            new_y = self.ycor()-25
            self.goto(self.xcor(), new_y)