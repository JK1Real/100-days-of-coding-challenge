# Leveling up 
from turtle import Turtle

class Score(Turtle):
    def __init__(self, shape: str = "classic", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)

        self.penup()
        self.hideturtle()
        self.goto(x=-250,y=250)
    
    def levelup(self,score):
        self.write(f"Level: {score}", align="center",font=("Bold", 18, "normal"))
