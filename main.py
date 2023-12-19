from turtle import Screen
from paddle import Paddle
from ball import Ball
from info import TopBar, Lives, Points, Level
from blocks import Blocks
import time

game_on = True
screen = Screen()
screen.setup(width=1000, height=800)
screen.bgcolor("black")
screen.title("Breakout")
screen.tracer(0)

blocks = Blocks()
blocks.build(3)
ball = Ball()
paddle = Paddle(0, -350)
bar = TopBar()
points = Points()
lives = Lives()
level = Level()


def move_paddle_left():
    paddle.go_left(-410)


def move_paddle_right():
    paddle.go_right(401)


def hit_ball_with_paddle():
    if paddle.xcor() - 90 <= ball.xcor() <= paddle.xcor() + 90 \
            and paddle.ycor() - 20 <= ball.ycor() <= paddle.ycor() + 20:
        ball.y_move *= -1
        ball.goto(ball.xcor(), ball.ycor() + 10)


def ball_fall_loose_life():
    global game_on
    if ball.ycor() < -700:
        ball.y_move = 4
        screen_reset()
        lives.remaining = lives.remaining[:-1]
        lives.update_lives()
        paddle.reset_position()
        if lives.remaining == "":
            game_on = False


def screen_reset():
    paddle.reset_position()
    ball.reset_position()


def level_up():
    level.number += 1
    level.update_level()
    ball.x_move += 1
    ball.y_move += 1
    points.increase_by *= 5
    screen_reset()
    blocks.build(3)


def destroy_blocks():
    for block in blocks.all_blocks:
        if block.xcor() - 55 <= ball.xcor() <= block.xcor() + 55 \
                and block.ycor() - 35 <= ball.ycor() <= block.ycor() + 35:

            ball.y_move *= -1
            if ball.y_move > 0:
                ball.goto(ball.xcor(), ball.ycor() + 10)
            else:
                ball.goto(ball.xcor(), ball.ycor() - 20)

            block.reset()
            points.add(points.increase_by)
            points.update()
            blocks.all_blocks.remove(block)

    if not blocks.all_blocks:
        level_up()


def clear_screen():
    paddle.reset()
    ball.reset()
    points.reset()


def game_over():
    clear_screen()
    with open("highest_score.txt") as file:
        highest_score = int(file.read())

        message = "GAME OVER"
        level.goto(0, 200)
        level.write(message, align="center", font=("Currier", 60, "normal"))
        level.goto(0, -50)
        score = f"Your Score: 💰{points.amount}"
        level.write(score, align="center", font=("Currier", 40, "normal"))

        level.goto(0, -100)

        if points.amount > highest_score:
            level.color("red")
            level.write("New Highest Score!", align="center", font=("Currier", 40, "normal"))
            with open("highest_score.txt", mode="w") as score_file:
                score_file.write(str(points.amount))
        else:
            message = f"Highest Score: {highest_score}"
            level.write(message, align="center", font=("Currier", 30, "normal"))


def start_game():
    screen.listen()
    screen.onkey(move_paddle_right, "Right")
    screen.onkey(move_paddle_left, "Left")

    global game_on
    game_on = True
    while game_on:
        time.sleep(ball.move_speed)
        screen.update()
        ball.move()
        ball.bounce_of_walls()
        hit_ball_with_paddle()
        ball_fall_loose_life()
        destroy_blocks()


start_game()


game_over()


screen.mainloop()

