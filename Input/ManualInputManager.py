from Logic.Tetris import Tetris
import pygame


class ManualInputManager:

    def __init__(self, game: Tetris):
        self.game: Tetris = game
        pygame.display.init()

    def main_loop(self):
        while not self.game.scoreboard.game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.game.move_left()
                    elif event.key == pygame.K_RIGHT:
                        self.game.move_right()
                    elif event.key == pygame.K_UP:
                        self.game.rotate()
                    elif event.key == pygame.K_DOWN:
                        self.game.drop_piece()
