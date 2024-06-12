import pygame
import config
import random


class Snake:

    def __init__(self):
        self.speed = config.start_speed
        self.position = [0, 0]
        self.body = []
        self.cur_direction = "RIGHT"
        self.set_start_position()
        self.set_start_body()

    def set_start_position(self):
        """
        Sets the start position of the snake randomly on the screen
        """
        self.position = [
            random.randrange(1, (config.window_width // config.block_size))
            * config.block_size,
            random.randrange(1, (config.window_height // config.block_size * 2))
            * config.block_size,
        ]

    def set_start_body(self):
        """
        Creates the starting body of the snake based on its location
        """
        start_x, start_y = self.position[0], self.position[1]
        self.body = [
            [start_x - i, start_y]
            for i in range(
                0, config.start_snake_size * config.block_size, config.block_size
            )
        ]

    def valid_change(self, new_direction):
        opposites = {"UP": "DOWN", "DOWN": "UP", "LEFT": "RIGHT", "RIGHT": "LEFT"}
        return new_direction != opposites[self.cur_direction]

    def update_position(self, direction):
        if direction == "UP":
            self.position[1] -= config.block_size
        elif direction == "DOWN":
            self.position[1] += config.block_size
        elif direction == "LEFT":
            self.position[0] -= config.block_size
        elif direction == "RIGHT":
            self.position[0] += config.block_size

        if self.position[0] < 0:
            self.position[0] = config.window_width - config.block_size
        elif self.position[0] > config.window_width - config.block_size:
            self.position[0] = 0

        if self.position[1] < 0:
            self.position[1] = config.window_height - config.block_size
        elif self.position[1] > config.window_height - config.block_size:
            self.position[1] = 0
        # self.position[0] %= config.window_width
        # self.position[1] %= config.window_height

    def update_body(self, fruit):
        self.body.insert(0, list(self.position))
        if self.position == fruit.position:
            fruit.eaten = True
        elif self.position == fruit.poisonous_position:
            fruit.poisonous_eaten = True
        else:
            self.body.pop()

    def move(self, new_direction, fruit, directional_blocks):
        # Make logic better
        if self.directional_collision(directional_blocks):
            opposites = {"UP": "DOWN", "DOWN": "UP", "LEFT": "RIGHT", "RIGHT": "LEFT"}
            valid_dirs = [
                dir
                for dir in ["UP", "DOWN", "LEFT", "RIGHT"]
                if dir != opposites[self.cur_direction]
            ]
            self.cur_direction = random.choice(valid_dirs)
        elif self.valid_change(new_direction):
            self.cur_direction = new_direction
        self.update_position(self.cur_direction)
        self.update_body(fruit)

    def draw(self, game_window):
        for pos in self.body:
            pygame.draw.rect(
                game_window,
                config.green,
                pygame.Rect(pos[0], pos[1], config.block_size, config.block_size),
            )

    def body_collision(self):
        for block in self.body[1:]:
            if self.position == block:
                return True
        return False

    def wall_collision(self, walls):
        for wall in walls:
            if self.position in wall:
                return True
        return False

    def directional_collision(self, directional_blocks):
        for block in directional_blocks:
            if self.position == block:
                return True
        return False
