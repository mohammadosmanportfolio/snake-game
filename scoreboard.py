from turtle import Turtle

SCORE_FONT = ('Arial', 12, 'normal')
GAME_OVER_FONT = ('Arial', 16, 'normal')
SCORE_ALIGNMENT = 'center'
GAME_OVER_ALIGNMENT = 'center'

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore = self.get_high_score()
        self.hideturtle()
        self.penup()
        self.setpos(0, 280)
        self.color('white')
        self.write(arg=f"Score: {self.score}. High Score: {self.highscore}", align=SCORE_ALIGNMENT,
                   font=SCORE_FONT)
        
    def get_high_score(self):
        with open('current high score.txt') as high_score_file:
            return high_score_file.read()
    
    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Score: {self.score}. High Score: {self.highscore}", align=SCORE_ALIGNMENT,
                   font=SCORE_FONT)
        
    def increment_score(self):
        self.score += 1
        self.update_scoreboard()
        
    def reset(self):
        if self.score > int(self.highscore):
            with open('current high score.txt', 'w') as high_score_file:
                high_score_file.write(str(self.score))
                self.highscore = self.score
        self.score = 0
        self.update_scoreboard()

