import random
import config
import pygame


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

    def overlap(self, position, snake, walls, directional_blocks):
        """
        Checks if a given position overlaps with the snake, walls, or directional blocks.

        Args:
            position (list): The position to check for overlap.
            snake (Snake): The snake object.
            walls (list): List of wall positions.
            directional_blocks (list): List of directional blocks positions.

        Returns:
            bool: True if there is an overlap, False otherwise.
        """
        if position in snake.body:
            return True
        elif any([position in wall for wall in walls]):
            return True
        elif position in directional_blocks:
            return True
        return False

    def set_position(self, game):
        """
        Sets a random position for the fruit and a poisonous fruit if applicable.

        Args:
            snake (Snake): The snake object.
            walls (list): List of wall positions.
            directional_blocks (list): List of directional blocks positions.
        """
        while True:
            position = [
                random.randrange(1, (config.window_width // config.block_size))
                * config.block_size,
                random.randrange(1, (config.window_height // config.block_size))
                * config.block_size,
            ]
            if not game.overlap_all(position):
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
                    not game.overlap_all(poisonous_position)
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
