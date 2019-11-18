class Scoreboard:

    MAX_LEVEL: int = 9

    def __init__(self):
        self.level = 0
        self.lines = 0
        self.score = 0
        self.game_over = False

    def get_speed(self) -> int:
        if self.level == 0:
            return 100
        elif self.level == 1:
            return 600
        elif self.level == 2:
            return 500
        elif self.level == 3:
            return 400
        elif self.level == 4:
            return 350
        elif self.level == 5:
            return 300
        elif self.level == 6:
            return 250
        elif self.level == 7:
            return 150
        elif self.level == 8:
            return 150
        elif self.level == 9:
            return 100
        else:
            return 100

    def add_score(self, score):
        self.score += score

    def add_lines(self, lines_cleared):
        self.add_score(lines_cleared)
        self.lines += lines_cleared

        if self.lines > 0 and self.lines % 10 == 0 and self.level <= Scoreboard.MAX_LEVEL:
            self.level += 1
