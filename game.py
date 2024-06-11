import pygame
import config


class Game:

    def __init__(self, snake, fruit, game_window):
        self.snake = snake
        self.fruit = fruit
        self.fruit.set_position(self.snake)
        self.score = 0
        self.game_window = game_window

    def restart(self):
        self.snake.set_start_position()
        self.snake.set_start_body()
        self.fruit.set_position(self.snake)
        self.score = 0

    def show_score(self):

        # create the display surface object
        # score_surface
        score_surface = pygame.font.SysFont(*config.score_font).render(
            "Score : " + str(self.score), True, config.white
        )

        # create a rectangular object for the text
        # surface object
        score_rect = score_surface.get_rect()

        # displaying text
        self.game_window.blit(score_surface, score_rect)

    def game_over(self):

        # creating a text surface on which text
        # will be drawn
        score_surface = pygame.font.SysFont(*config.game_over_font).render(
            f"Your Score is : {self.score}", True, config.red
        )

        # create a rectangular object for the text
        # surface object
        score_rect = score_surface.get_rect()

        # setting position of the text
        score_rect.midtop = (config.window_width / 2, config.window_height / 4)

        # blit will draw the text on screen
        self.game_window.blit(score_surface, score_rect)

        restart_surface = pygame.font.SysFont(*config.game_over_font).render(
            "Press space to restart. Escape to exit.", True, config.red
        )

        # create a rectangular object for the text
        # surface object
        restart_rect = restart_surface.get_rect()

        # setting position of the text
        restart_rect.midtop = (config.window_width / 2, config.window_height / 2)

        # blit will draw the text on screen
        self.game_window.blit(restart_surface, restart_rect)
        pygame.display.flip()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.restart()
                        return
                    elif event.key == pygame.K_ESCAPE:
                        # deactivating pygame library
                        pygame.quit()
                        # quit the program
                        quit()
                elif event.type == pygame.QUIT:
                    pygame.quit()
                    # quit the program
                    quit()

    def run(self):
        new_direction = self.snake.cur_direction
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
            elif event.type == pygame.QUIT:
                pygame.quit()
                # quit the program
                quit()

        # Moving the snake
        self.snake.move(new_direction, self.fruit)

        # Snake body growing mechanism
        # if fruits and snakes collide then scores
        # will be incremented by 10
        if self.fruit.eaten:
            self.score += 1
            self.fruit.eaten = False
            self.fruit.set_position(self.snake)

        self.game_window.fill(config.black)

        self.snake.draw(self.game_window)
        self.fruit.draw(self.game_window)

        # Game Over conditions

        # Touching the snake body
        if self.snake.check_body_collision():
            self.game_over()

        # displaying score continuously
        self.show_score()
