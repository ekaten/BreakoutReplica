from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.starting_position = (0, -310)
        self.setposition(self.starting_position)
        self.shape("circle")
        self.shapesize(stretch_wid=1.5, stretch_len=1.5)
        self.color("grey")
        self.speed("slow")
        self.move_speed = 0.001
        self.x_move = 4
        self.y_move = 4

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x,  new_y)

    def bounce_of_walls(self):
        if self.ycor() > 285:
            self.y_move *= -1

        if self.xcor() > 480 or self.xcor() < -480:
            self.x_move *= -1

    def reset_position(self):
        self.setposition(self.starting_position)