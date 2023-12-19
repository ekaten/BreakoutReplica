from turtle import Turtle


class TopBar(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(0, 300)
        self.shape("square")
        self.shapesize(stretch_wid=0.2, stretch_len=100)


class Points(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.amount = 0
        self.increase_by = 1
        self.update()

    def update(self):
        point_display = f"💰{self.amount}"
        self.clear()
        self.goto(450, 320)
        self.write(point_display, align="right", font=("Currier", 50, "normal"))

    def add(self, x):
        self.amount += x


class Lives(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.remaining = "🏐"
        self.update_lives()

    def update_lives(self):
        self.clear()
        self.goto(-450, 320)
        self.write(self.remaining, align="left", font=("Currier", 40, "normal"))


class Level(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.number = 1
        self.update_level()

    def update_level(self):
        self.clear()
        self.goto(0, 320)
        level = f"Level {self.number}"
        self.write(level, align="center", font=("Currier", 40, "normal"))