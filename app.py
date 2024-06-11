# importing libraries
import pygame
import time
import config
from snake import Snake
from fruit import Fruit

# Initialising pygame
pygame.init()

# Initialise game window
pygame.display.set_caption("Snake Reloaded")
game_window = pygame.display.set_mode((config.window_width, config.window_height))

# FPS (frames per second) controller
fps = pygame.time.Clock()

snake = Snake()

fruit = Fruit()
fruit.set_fruit_position(snake)

# initial score
score = 0


# displaying Score function
def show_score(choice, color, font, size):

    # creating font object score_font
    score_font = pygame.font.SysFont(font, size)

    # create the display surface object
    # score_surface
    score_surface = score_font.render("Score : " + str(score), True, color)

    # create a rectangular object for the text
    # surface object
    score_rect = score_surface.get_rect()

    # displaying text
    game_window.blit(score_surface, score_rect)


# game over function
def game_over():

    # creating font object my_font
    my_font = pygame.font.SysFont("times new roman", 50)

    # creating a text surface on which text
    # will be drawn
    score_str = f"Your Score is : {score}"
    score_surface = my_font.render(score_str, True, config.red)

    # create a rectangular object for the text
    # surface object
    score_rect = score_surface.get_rect()

    # setting position of the text
    score_rect.midtop = (config.window_width / 2, config.window_height / 4)

    # blit will draw the text on screen
    game_window.blit(score_surface, score_rect)

    restart_str = f"Press space to restart"
    restart_surface = my_font.render(restart_str, True, config.red)

    # create a rectangular object for the text
    # surface object
    restart_rect = restart_surface.get_rect()

    # setting position of the text
    restart_rect.midtop = (config.window_width / 2, config.window_height / 2)

    # blit will draw the text on screen
    game_window.blit(restart_surface, restart_rect)
    pygame.display.flip()

    # after 2 seconds we will quit the program
    time.sleep(2)

    # deactivating pygame library
    pygame.quit()

    # quit the program
    quit()


# Main Function
while True:

    new_direction = snake.cur_direction
    # handling key events
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                new_direction = "UP"
            if event.key == pygame.K_DOWN:
                new_direction = "DOWN"
            if event.key == pygame.K_LEFT:
                new_direction = "LEFT"
            if event.key == pygame.K_RIGHT:
                new_direction = "RIGHT"

    # Moving the snake
    snake.move(new_direction, fruit)

    # Snake body growing mechanism
    # if fruits and snakes collide then scores
    # will be incremented by 10
    if fruit.eaten:
        score += 10
        fruit.eaten = False
        fruit.set_fruit_position(snake)

    game_window.fill(config.black)

    snake.draw(game_window)
    fruit.draw(game_window)

    # Game Over conditions

    # Touching the snake body
    if snake.check_body_collision():
        game_over()

    # displaying score continuously
    show_score(1, config.white, "times new roman", 20)

    # Refresh game screen
    pygame.display.update()

    # Frame Per Second /Refresh Rate
    fps.tick(config.snake_speed)
