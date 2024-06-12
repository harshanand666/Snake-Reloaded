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

    def overlap(self, position, snake, walls, directional_blocks):
        if position in snake.body:
            return True
        elif any([position in wall for wall in walls]):
            return True
        elif position in directional_blocks:
            return True
        return False

    def set_position(self, snake, walls, directional_blocks):
        while True:
            position = [
                random.randrange(1, (config.window_width // config.block_size))
                * config.block_size,
                random.randrange(1, (config.window_height // config.block_size))
                * config.block_size,
            ]

            if not self.overlap(position, snake, walls, directional_blocks):
                self.position = position
                break

        if self.poisonous:
            while True:
                poisonous_position = [
                    random.randrange(1, (config.window_width // config.block_size))
                    * config.block_size,
                    random.randrange(1, (config.window_height // config.block_size))
                    * config.block_size,
                ]
                if (
                    not self.overlap(
                        poisonous_position, snake, walls, directional_blocks
                    )
                    and poisonous_position != position
                ):
                    self.poisonous_position = poisonous_position
                    break

    def draw(self, game_window):
        food_color = config.purple if self.poisonous else config.white
        pygame.draw.rect(
            game_window,
            food_color,
            pygame.Rect(
                self.position[0], self.position[1], config.block_size, config.block_size
            ),
        )
        if self.poisonous:
            pygame.draw.rect(
                game_window,
                food_color,
                pygame.Rect(
                    self.poisonous_position[0],
                    self.poisonous_position[1],
                    config.block_size,
                    config.block_size,
                ),
            )
