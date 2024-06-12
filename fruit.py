import random
import config
import pygame


class Fruit:
    def __init__(self):
        self.position = [0, 0]
        self.eaten = False
        self.poisonous = False
        self.poisonous_position = [0, 0]
        self.poisonous_eaten = False

    def overlap(self, random_position, snake):
        if random_position in snake.body:
            return True
        return False

    def set_position(self, snake):
        while True:
            position = [
                random.randrange(1, (config.window_width // 10)) * 10,
                random.randrange(1, (config.window_height // 10)) * 10,
            ]

            if not self.overlap(position, snake):
                self.position = position
                break

        if self.poisonous:
            while True:
                poisonous_position = [
                    random.randrange(1, (config.window_width // 10)) * 10,
                    random.randrange(1, (config.window_height // 10)) * 10,
                ]
                if (
                    not self.overlap(poisonous_position, snake)
                    and poisonous_position != position
                ):
                    self.poisonous_position = poisonous_position
                    break

    def draw(self, game_window):
        pygame.draw.rect(
            game_window,
            config.white,
            pygame.Rect(self.position[0], self.position[1], 10, 10),
        )
        if self.poisonous:
            pygame.draw.rect(
                game_window,
                config.white,
                pygame.Rect(
                    self.poisonous_position[0], self.poisonous_position[1], 10, 10
                ),
            )
