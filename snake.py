import pygame
import config
import random


class Snake:
    def __init__(self):
        """
        Initializes the snake with starting speed, position, body, and direction.
        """
        self.speed = config.start_speed
        self.position = [0, 0]
        self.body = []
        self.cur_direction = random.choice(list(config.direction_dir.keys()))
        self.set_start_position()
        self.set_start_body()

    def set_start_position(self):
        """
        Sets the start position of the snake randomly on the screen.
        """
        self.position = [
            random.randrange(1, (config.window_width // config.block_size))
            * config.block_size,
            random.randrange(1, (config.window_height // config.block_size))
            * config.block_size,
        ]

    def set_start_body(self):
        """
        Creates the starting body of the snake based on its location.
        """
        start_x, start_y = self.position[0], self.position[1]
        self.body = [
            [start_x - i, start_y]
            for i in range(
                0, config.start_snake_size * config.block_size, config.block_size
            )
        ]

    def valid_change(self, new_direction):
        """
        Checks if the new direction is valid (not opposite to the current direction).

        Args:
            new_direction (str): The new direction to be checked.

        Returns:
            bool: True if the change is valid, False otherwise.
        """
        return new_direction != config.direction_dir[self.cur_direction]

    def update_position(self, direction):
        """
        Updates the snake's position based on the direction.

        Args:
            direction (str): The direction in which the snake is moving.
        """
        if direction == "UP":
            self.position[1] -= config.block_size
        elif direction == "DOWN":
            self.position[1] += config.block_size
        elif direction == "LEFT":
            self.position[0] -= config.block_size
        elif direction == "RIGHT":
            self.position[0] += config.block_size

        if self.position[0] < config.block_size:
            self.position[0] = config.window_width - config.block_size
        elif self.position[0] > config.window_width - config.block_size:
            self.position[0] = 0

        if self.position[1] < config.block_size:
            self.position[1] = config.window_height - config.block_size
        elif self.position[1] > config.window_height - config.block_size:
            self.position[1] = 0
        # self.position[0] %= config.window_width
        # self.position[1] %= config.window_height

    def update_body(self, fruit):
        """
        Updates the snake's body. Grows the body if the snake eats a fruit.

        Args:
            fruit (Fruit): The fruit object to check if eaten.
        """
        self.body.insert(0, list(self.position))
        if self.position == fruit.position:
            fruit.eaten = True
        elif self.position == fruit.poisonous_position:
            fruit.poisonous_eaten = True
        else:
            self.body.pop()

    def move(self, new_direction, fruit, directional_blocks):
        """
        Moves the snake in the specified direction and updates its body.

        Args:
            new_direction (str): The new direction to move.
            fruit (Fruit): The fruit object to check if eaten.
            directional_blocks (list): List of directional blocks positions.
        """
        if self.directional_collision(directional_blocks):
            valid_dirs = [
                dir
                for dir in config.direction_dir.keys()
                if dir != config.direction_dir[self.cur_direction]
            ]
            self.cur_direction = random.choice(valid_dirs)
        elif self.valid_change(new_direction):
            self.cur_direction = new_direction
        self.update_position(self.cur_direction)
        self.update_body(fruit)

    def draw(self, game_window):
        """
        Draws the snake on the game window.

        Args:
            game_window (pygame.Surface): The game window surface.
        """
        for pos in self.body:
            pygame.draw.rect(
                game_window,
                config.green,
                pygame.Rect(pos[0], pos[1], config.block_size, config.block_size),
            )

    def body_collision(self):
        """
        Checks if the snake has collided with its own body.

        Returns:
            bool: True if there is a collision, False otherwise.
        """
        for block in self.body[1:]:
            if self.position == block:
                return True
        return False

    def wall_collision(self, walls):
        """
        Checks if the snake has collided with any walls.

        Args:
            walls (list): List of wall positions.

        Returns:
            bool: True if there is a collision, False otherwise.
        """
        for wall in walls:
            if self.position in wall:
                return True
        return False

    def directional_collision(self, directional_blocks):
        """
        Checks if the snake has collided with any directional blocks.

        Args:
            directional_blocks (list): List of directional blocks positions.

        Returns:
            bool: True if there is a collision, False otherwise.
        """
        for block in directional_blocks:
            if self.position == block:
                return True
        return False
