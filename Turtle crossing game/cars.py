from random import randint
from turtle import Turtle


# Create a cars
class Create_car(Turtle):
    def __init__(self, shape: str = "classic", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)

        self.colors = ["red","blue","green","yellow"]
        self.penup()
        self.ys = [0,23,-23,-111,-122,-100,111,222,333,21,60,90,100,89,23,27]
        self.xs = [-200,-300,-222,-432,-545,-200,-555]
        self.goto(x=self.xs[randint(0,6)],y=self.ys[randint(0,15)])
    

    def colored_cars(self):
        self.color(self.colors[randint(0,3)])

    def move_car(self):
        self.shape("square")
        self.forward(1)

    def end(self):
        self.goto(x=self.xs[randint(0,6)],y=self.ys[randint(0,7)])