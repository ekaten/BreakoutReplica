from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.penup()
        self.starting_position = (x, y)
        self.setposition(self.starting_position)
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=8)
        self.move_px = 40

    def go_left(self, limit):
        if self.xcor() > limit:
            x_left = self.xcor() - self.move_px
            self.goto(x_left, self.ycor())

    def go_right(self, limit):
        if self.xcor() < limit:
            x_right = self.xcor() + self.move_px
            self.goto(x_right, self.ycor())

    def reset_position(self):
        self.setposition(self.starting_position)
