from turtle import Turtle

# Create a turtle
class Create_turtle(Turtle):
    def __init__(self, shape: str = "classic", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.penup()
        self.shape("turtle")
        self.left(90)
        
    def move_forward(self):
        self.forward(10)