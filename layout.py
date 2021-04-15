from turtle import Turtle

FONT = ("Courier", 10, "bold")


class Layout(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.speed(0)
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
            self.stamp()
            self.setheading(90)
            self.forward(34)
            self.stamp()

    def victorious_turtle(self, winner_color):
        self.goto(-200, 10)
        self.shape("turtle")
        self.color(winner_color)
        self.shapesize(stretch_wid=2, stretch_len=2)
        self.showturtle()
        while 1:
            self.tilt(1)

    def victory(self, winner_color):
        self.hideturtle()
        self.goto(-100, -55)
        self.write(arg=f"You've Won.\nThe {winner_color} turtle is the winner", align="center", font=FONT)
        self.victorious_turtle(winner_color)

    def defeat(self, winner_color):
        self.hideturtle()
        self.goto(-100, -55)
        self.write(arg=f"You've Lost.\nThe {winner_color} turtle is the winner", align="center", font=FONT)
        self.victorious_turtle(winner_color)
