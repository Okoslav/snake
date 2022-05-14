from turtle import Turtle



class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, 280)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Skóre = {self.score}, Nejvyšší skóre = {self.high_score}", align="center", font=("Arial", 12, "normal"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 1
        self.update_score()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(f"Konec hry! Tvé skóre = {self.score}", align="center", font=("Arial", 25, "bold"))

