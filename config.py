import pygame

start_snake_size = 8
start_speed = 20

# Window size
window_width = 720
window_height = 480

# defining colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)
yellow = pygame.Color(255, 255, 0)
purple = (128, 0, 128)

# Font
score_font = ("times new roman", 20)
game_over_font = ("times new roman", 40)
difficulty_font = ("times new roman", 40)

# Wall
wall_size = 5

# Block size
block_size = 10

# poisonous
poison_score_penalty = 3
