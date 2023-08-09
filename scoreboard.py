from turtle import Turtle

STYLE = ("Gilroy", 16, "normal")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("White")
        self.penup()
        self.setpos(0, 270)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", move=False, align="center", font=STYLE)

    def game_over(self):
        self.setpos(0, 0)
        self.write("GAME OVER", move=False, align="center", font=("arial", 24, "normal"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()