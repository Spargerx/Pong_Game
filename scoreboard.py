from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("White")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update()
        
    def update(self):
        self.clear()
        self.goto(-100, 200)
        self.write(arg=self.l_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(arg=self.r_score, align="center", font=("Courier", 80, "normal"))
        
    def l_point(self):
        self.l_score +=1
        self.update()
        
    def r_point(self):
        self.r_score +=1
        self.update()
        
    def declare_winner(self):
        if self.l_score > self.r_score:
            argument = "Left Side Won!"
        elif self.r_score > self.l_score:
            argument = "Right Side Won!"
        self.goto(0,0)
        self.write(arg=argument, align="center", font=("Arial", 40, "bold"))