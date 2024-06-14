import random
import config
import pygame
import utils


class Fruit:
    def __init__(self):
        """
        Initializes the fruit with a position and state flags.
        """
        self.position = [0, 0]
        self.eaten = False
        self.poisonous = False
        self.poisonous_position = [0, 0]
        self.poisonous_eaten = False

    def set_position(self, snake, fruit, walls, directional_blocks):
        """
        Sets a random position for the fruit and a poisonous fruit if applicable.

        Args:
            snake (Snake): The snake object.
            walls (list): List of wall positions.
            directional_blocks (list): List of directional blocks positions.
        """
        while True:
            position = utils.get_random_position()
            if not utils.overlap_all(
                position,
                snake,
                fruit,
                walls,
                directional_blocks,
            ):
                self.position = position
                break

        if self.poisonous:
            while True:
                poisonous_position = utils.get_random_position()
                if (
                    not utils.overlap_all(
                        poisonous_position,
                        snake,
                        fruit,
                        walls,
                        directional_blocks,
                    )
                    and poisonous_position != position
                ):
                    self.poisonous_position = poisonous_position
                    break

    def draw(self, game_window):
        """
        Draws the fruit on the game window.

        Args:
            game_window (pygame.Surface): The game window surface.
        """
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
