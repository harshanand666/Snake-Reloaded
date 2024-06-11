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

# FPS (frames per second) controller
fps = pygame.time.Clock()

game_window = pygame.display.set_mode((config.window_width, config.window_height))

snake = Snake()
fruit = Fruit()
game = Game(snake, fruit, game_window)

# Main Function
while True:

    game.run()

    # Refresh game screen
    pygame.display.update()

    # Frame Per Second /Refresh Rate
    fps.tick(snake.speed)
