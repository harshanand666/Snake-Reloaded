# importing libraries
import pygame
import config
from snake import Snake
from fruit import Fruit
from game import Game

# Initialising pygame
pygame.init()

# Initialise game window
pygame.display.set_caption("Snake Reloaded")
game_window = pygame.display.set_mode((config.window_width, config.window_height))

# FPS (frames per second) controller
fps = pygame.time.Clock()

snake = Snake()

fruit = Fruit()
game = Game(snake, fruit, game_window)


# Main Function
while True:

    game.run()

    # Refresh game screen
    pygame.display.update()

    # Frame Per Second /Refresh Rate
    fps.tick(config.snake_speed)
