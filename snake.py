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
        # Middle of screen moving right
        self.position = [
            random.randrange(1, (config.window_width // 20)) * 10,
            random.randrange(1, (config.window_height // 20)) * 10,
        ]

    def set_start_body(self):
        start_x, start_y = self.position[0], self.position[1]
        self.body = [
            [start_x - i, start_y] for i in range(0, config.start_snake_size * 10, 10)
        ]

    def valid_change(self, new_direction):
        opposites = {"UP": "DOWN", "DOWN": "UP", "LEFT": "RIGHT", "RIGHT": "LEFT"}
        return new_direction != opposites[self.cur_direction]

    def update_position(self, direction):
        if direction == "UP":
            self.position[1] -= 10
        elif direction == "DOWN":
            self.position[1] += 10
        elif direction == "LEFT":
            self.position[0] -= 10
        elif direction == "RIGHT":
            self.position[0] += 10

        if self.position[0] < 0:
            self.position[0] = config.window_width - 10
        elif self.position[0] > config.window_width - 10:
            self.position[0] = 0

        if self.position[1] < 0:
            self.position[1] = config.window_height - 10
        elif self.position[1] > config.window_height - 10:
            self.position[1] = 0
        # self.position[0] %= config.window_width
        # self.position[1] %= config.window_height

    def update_body(self, fruit):
        self.body.insert(0, list(self.position))
        if self.position == fruit.position:
            fruit.eaten = True
        else:
            self.body.pop()

    def move(self, new_direction, fruit):
        if self.valid_change(new_direction):
            self.cur_direction = new_direction
        self.update_position(self.cur_direction)
        self.update_body(fruit)

    def draw(self, game_window):
        for pos in self.body:
            pygame.draw.rect(
                game_window, config.green, pygame.Rect(pos[0], pos[1], 10, 10)
            )

    def check_body_collision(self):
        for block in self.body[1:]:
            if self.position == block:
                return True
        return False
