import pygame

start_snake_size = 8
start_speed = 20
speed_increase = 10
difficulty_multiple = 1

# Window size
window_width = 720
window_height = 480
strip_height = 40  # Height of the strip for score and legend
game_window_height = window_height - strip_height

# defining colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)
yellow = pygame.Color(255, 255, 0)
purple = pygame.Color(128, 0, 128)
grey = pygame.Color(105, 105, 105)

# Font
score_font = ("times new roman", 20)
legend_font = ("times new roman", 20)
game_over_font = ("times new roman", 40)
difficulty_font = ("times new roman", 40)

# Wall
wall_size = 5

# Block size
block_size = 10

# poisonous
poison_score_penalty = 3
score_color_counter = 20

# opposite directions
direction_dir = {"UP": "DOWN", "DOWN": "UP", "LEFT": "RIGHT", "RIGHT": "LEFT"}
