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

    def increase_speed(self):
        # Fix font and make code efficient / cleaner
        speed_surface = pygame.font.SysFont(*config.difficulty_font).render(
            "INCREASING SPEED", True, config.blue
        )
        speed_rect = speed_surface.get_rect()
        speed_rect.center = (config.window_width / 2, config.window_height / 2)
        self.game_window.blit(speed_surface, speed_rect)
        self.snake.speed += 10
        pygame.display.flip()
        pygame.time.delay(1000)

    def show_score(self):

        # Surface and rect to show score
        score_surface = pygame.font.SysFont(*config.score_font).render(
            "Score : " + str(self.score), True, config.white
        )
        score_rect = score_surface.get_rect()

        self.game_window.blit(score_surface, score_rect)

    def game_over(self):

        # Surface and rect to show game over text
        score_surface = pygame.font.SysFont(*config.game_over_font).render(
            f"Your Score is : {self.score}", True, config.red
        )
        score_rect = score_surface.get_rect()

        # Position text
        score_rect.midtop = (config.window_width / 2, config.window_height / 4)
        self.game_window.blit(score_surface, score_rect)

        restart_surface = pygame.font.SysFont(*config.game_over_font).render(
            "Press space to restart. Escape to exit.", True, config.red
        )
        restart_rect = restart_surface.get_rect()
        restart_rect.midtop = (config.window_width / 2, config.window_height / 2)
        self.game_window.blit(restart_surface, restart_rect)

        pygame.display.flip()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.restart()
                        return
                    elif event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        quit()
                elif event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

    def run(self):
        new_direction = self.snake.cur_direction
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
                quit()

        self.snake.move(new_direction, self.fruit)

        if self.fruit.eaten:
            self.score += 1
            if self.score % 5 == 0:
                self.increase_speed()
            self.fruit.eaten = False
            self.fruit.set_position(self.snake)

        self.game_window.fill(config.black)

        self.snake.draw(self.game_window)
        self.fruit.draw(self.game_window)

        # Touching the snake body
        if self.snake.check_body_collision():
            self.game_over()

        self.show_score()
