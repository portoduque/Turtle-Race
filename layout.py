from turtle import Turtle


class Layout(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=0.8, stretch_len=0.8)
        self.penup()

    def draw_end_flag(self):
        self.goto(218, -120)
        for x in range(8):
            self.setheading(90)
            self.stamp()
            self.forward(34)

        self.goto(235, -103)
        for i in range(6):
            self.setheading(90)
            self.stamp()
            self.forward(34)