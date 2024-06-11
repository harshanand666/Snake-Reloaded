import random
import config
import pygame


class Fruit:
    def __init__(self):
        self.position = [0, 0]
        self.eaten = False

    def overlap(self, random_position, snake):
        if random_position in snake.body:
            return True
        return False

    def set_position(self, snake):
        while True:
            random_position = [
                random.randrange(1, (config.window_width // 10)) * 10,
                random.randrange(1, (config.window_height // 10)) * 10,
            ]
            if not self.overlap(random_position, snake):
                self.position = random_position
                break

    def draw(self, game_window):
        pygame.draw.rect(
            game_window,
            config.white,
            pygame.Rect(self.position[0], self.position[1], 10, 10),
        )
