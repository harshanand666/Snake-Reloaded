import pygame
import config
import random


class Game:
    def __init__(self, snake, fruit, game_window):
        """
        Initializes the game with a snake, fruit, game window, score, and other game elements.
        """
        self.snake = snake
        self.fruit = fruit
        self.score = 0
        self.game_window = game_window
        self.walls = []
        self.directional_blocks = []
        self.fruit.set_position(self.snake, self.walls, self.directional_blocks)

    def restart(self):
        """
        Restarts the game by resetting the snake, fruit, score, and other elements.
        """
        self.snake.set_start_position()
        self.snake.set_start_body()
        self.fruit.set_position(self.snake, self.walls, self.directional_blocks)
        self.score = 0
        self.walls = []
        self.snake.speed = config.start_speed

    def overlap_all(self, position):
        """
        Checks if a given position overlaps with the snake, walls, or directional blocks.

        Args:
            position (list): The position to check for overlap.

        Returns:
            bool: True if there is an overlap, False otherwise.
        """
        if position in self.snake.body:
            return True
        elif any([position in wall for wall in self.walls]):
            return True
        elif position in self.directional_blocks:
            return True
        return False

    def increase_speed(self):
        """
        Increases the speed of the snake.

        Returns:
            str: Message indicating the action taken.
        """
        self.snake.speed += 10
        return "INCREASING SPEED"

    def add_wall(self):
        """
        Adds a new wall to the game at a random position.

        Returns:
            str: Message indicating the action taken.
        """
        while True:
            random_position = [
                random.randrange(1, (config.window_width // config.block_size))
                * config.block_size,
                random.randrange(1, (config.window_height // config.block_size))
                * config.block_size,
            ]
            if not self.overlap_all(random_position):
                break

        start_x, start_y = random_position[0], random_position[1]
        wall_direction = random.choice(["V", "H"])
        if wall_direction == "H":
            new_wall = [
                [start_x - i, start_y]
                for i in range(
                    0, config.wall_size * config.block_size, config.block_size
                )
            ]
        else:
            new_wall = [
                [start_x, start_y - i]
                for i in range(
                    0, config.wall_size * config.block_size, config.block_size
                )
            ]
        self.walls.append(new_wall)
        return "ADDING WALL"

    def draw_walls(self):
        """
        Draws all walls on the game window.
        """
        for wall in self.walls:
            for pos in wall:
                pygame.draw.rect(
                    self.game_window,
                    config.red,
                    pygame.Rect(pos[0], pos[1], config.block_size, config.block_size),
                )

    def add_directional_block(self):
        """
        Adds a new directional block to the game at a random position.

        Returns:
            str: Message indicating the action taken.
        """
        while True:
            random_position = [
                random.randrange(1, (config.window_width // config.block_size))
                * config.block_size,
                random.randrange(1, (config.window_height // config.block_size))
                * config.block_size,
            ]
            if not self.overlap_all(random_position):
                self.position = random_position
                break
        self.directional_blocks.append(random_position)
        return "ADDING DIRECTIONAL BLOCK"

    def draw_directional_blocks(self):
        """
        Draws all directional blocks on the game window.
        """
        for pos in self.directional_blocks:
            pygame.draw.rect(
                self.game_window,
                config.yellow,
                pygame.Rect(pos[0], pos[1], config.block_size, config.block_size),
            )

    def add_poisonous_fruit(self):
        """
        Adds a poisonous fruit to the game.

        Returns:
            str: Message indicating the action taken.
        """
        self.fruit.poisonous = True
        return "ADDING POISONOUS FRUIT"

    def increase_difficulty(self):
        """
        Increases the difficulty of the game by adding speed, walls, directional blocks, or poisonous fruit.

        Returns:
            str: Message indicating the action taken.
        """
        diff_options = [
            self.increase_speed,
            self.add_wall,
            self.add_directional_block,
            self.add_poisonous_fruit,
        ]
        diff_text = random.choice(diff_options)()

        diff_surface = pygame.font.SysFont(*config.difficulty_font).render(
            diff_text, True, config.blue
        )
        diff_rect = diff_surface.get_rect()
        diff_rect.center = (config.window_width / 2, config.window_height / 2)
        self.game_window.blit(diff_surface, diff_rect)
        pygame.display.flip()
        pygame.time.delay(1000)

    def show_score(self):
        """
        Displays the current score on the game window.
        """
        score_surface = pygame.font.SysFont(*config.score_font).render(
            "Score : " + str(self.score), True, config.white
        )
        score_rect = score_surface.get_rect()

        self.game_window.blit(score_surface, score_rect)

    def game_over(self):
        """
        Displays the game over message and waits for user input to restart or exit the game.
        """
        score_surface = pygame.font.SysFont(*config.game_over_font).render(
            f"Your Score is : {self.score}", True, config.red
        )
        score_rect = score_surface.get_rect()
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

    def check_game_over(self):
        """
        Checks if the game is over by detecting snake's collision with its body or walls.
        """
        if self.snake.body_collision() or self.snake.wall_collision(self.walls):
            self.game_over()

    def run(self):
        """
        Runs the game loop, handling events, updating game state, and rendering the game.
        """
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

        self.snake.move(new_direction, self.fruit, self.directional_blocks)

        if self.fruit.eaten:
            self.score += 1
            if self.score % 1 == 0:
                self.increase_difficulty()
            self.fruit.eaten = False
            self.fruit.set_position(self.snake, self.walls, self.directional_blocks)
        elif self.fruit.poisonous_eaten:
            self.score = max(self.score - config.poison_score_penalty, 0)
            snake_len = len(self.snake.body)
            self.snake.body = self.snake.body[
                : max(snake_len // 2, config.start_snake_size)
            ]
            self.fruit.poisonous_eaten = False
            self.fruit.poisonous = False
            self.fruit.set_position(self.snake, self.walls, self.directional_blocks)

        self.game_window.fill(config.black)

        self.snake.draw(self.game_window)
        self.fruit.draw(self.game_window)
        self.draw_walls()
        self.draw_directional_blocks()

        self.check_game_over()

        self.show_score()
