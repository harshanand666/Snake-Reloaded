# importing libraries
import pygame
import config
from game import Game

# Initialising pygame
pygame.init()
pygame.mixer.init()


# Initialise game window
pygame.display.set_caption("Snake Reloaded")

# FPS (frames per second) controller
fps = pygame.time.Clock()

game_window = pygame.display.set_mode((config.window_width, config.window_height))

game = Game(game_window)

# Main Function
while True:

    game.run()

    # Refresh game screen
    pygame.display.update()

    # Frame Per Second /Refresh Rate
    fps.tick(game.snake.speed)
