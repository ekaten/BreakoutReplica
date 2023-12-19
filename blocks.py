from turtle import Turtle
import random




class Blocks():
    def __init__(self):
        self.all_blocks = []

    def build(self, n_lines):
        colors = ["red", "blue", "pink", "purple", "orange", "yellow", "green"]
        line_start_x = -455
        line_start_y = 150
        for n in range(n_lines):
            color = random.choice(colors)
            if n % 2 == 0:
                blocks_per_row = 11
            else:
                blocks_per_row = 12
            for i in range(blocks_per_row):
                block = Turtle()
                block.penup()
                block.shape("square")
                block.shapesize(stretch_wid=2, stretch_len=4)
                block.color("red")
                block.setposition(line_start_x, line_start_y)
                line_start_x += 90
                block.color(color)
                self.all_blocks.append(block)
            line_start_x -= 1035
            line_start_y += -50
            colors.remove(color)


