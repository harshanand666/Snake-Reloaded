import pygame
import config
import random
from snake import Snake
from fruit import Fruit
import utils


class Game:
    def __init__(self, game_window):
        """
        Initializes the game with a snake, fruit, game window, score, and other game elements.
        """
        self.snake = Snake()
        self.fruit = Fruit()
        self.score = 0
        self.game_window = game_window
        self.walls = []
        self.directional_blocks = []
        self.fruit.set_position(
            self.snake, self.fruit, self.walls, self.directional_blocks
        )
        self.score_color = config.white
        self.score_color_counter = 0

        # Music assets
        self.background_music = "./assets/sounds/background.mp3"
        self.game_over_sound = "./assets/sounds/game_over.wav"

        pygame.mixer.music.load(self.background_music)
        pygame.mixer.music.play(-1)  # Loop indefinitely

    def restart(self):
        """
        Restarts the game by resetting the snake, fruit, score, and other elements.
        """
        self.score = 0
        self.walls = []
        self.directional_blocks = []
        self.fruit.poisonous = False
        self.fruit.poisonous_eaten = False
        self.snake.set_start_position()
        self.snake.set_start_body()
        self.snake.speed = config.start_speed
        self.fruit.set_position(
            self.snake, self.fruit, self.walls, self.directional_blocks
        )

        # Restart background music
        pygame.mixer.music.load(self.background_music)
        pygame.mixer.music.play(-1)

    def increase_speed(self):
        """
        Increases the speed of the snake.

        Returns:
            str: Message indicating the action taken.
        """
        self.snake.speed += config.speed_increase
        return "INCREASING SPEED"

    def add_wall(self):
        """
        Adds a new wall to the game at a random position.

        Returns:
            str: Message indicating the action taken.
        """
        while True:
            random_position = utils.get_random_position()
            if not utils.overlap_all(
                random_position,
                self.snake,
                self.fruit,
                self.walls,
                self.directional_blocks,
            ):
                break

        start_x, start_y = random_position[0], random_position[1]
        # Get orientation of wall
        wall_direction = random.choice(["V", "H"])
        if wall_direction == "H":
            new_wall = [
                [start_x + i, start_y]
                for i in range(
                    0, config.wall_size * config.block_size, config.block_size
                )
            ]
        else:
            new_wall = [
                [start_x, start_y + i]
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
            random_position = utils.get_random_position()
            if not utils.overlap_all(
                random_position,
                self.snake,
                self.fruit,
                self.walls,
                self.directional_blocks,
            ):
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
        """
        # Choose random event
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

        # Show flashing message indicating the event chosen
        for _ in range(config.diff_message_count):

            # Draw the text
            self.game_window.blit(diff_surface, diff_rect)
            pygame.display.flip()
            pygame.time.delay(config.diff_message_duration)

            # Clear the text by filling the area with the background color
            self.game_window.fill(config.black, diff_rect)

            # Re-draw game elements
            self.snake.draw(self.game_window)
            self.fruit.draw(self.game_window)
            self.draw_walls()
            self.draw_directional_blocks()
            self.show_score_strip()
            pygame.display.flip()
            pygame.time.delay(config.diff_message_duration)

    def show_score(self):
        """
        Displays the current score on the game window.
        """
        score_surface = pygame.font.SysFont(*config.score_font).render(
            "Score : " + str(self.score), True, self.score_color
        )
        score_rect = score_surface.get_rect()
        score_rect.topleft = (config.score_x, config.score_y)
        self.game_window.blit(score_surface, score_rect)

    def show_legend(self):
        """
        Displays the legend for different objects in the game.
        """
        legend_items = [
            ("Directional Block", config.yellow),
            ("Poisonous Fruit", config.purple),
            ("Wall", config.red),
        ]

        font = pygame.font.SysFont(*config.legend_font)

        for index, (text, color) in enumerate(legend_items):
            # Draw colored square
            pygame.draw.rect(
                self.game_window,
                color,
                pygame.Rect(
                    config.legend_x_offset + index * config.legend_spacing,
                    config.legend_y_offset,
                    config.block_size,
                    config.block_size,
                ),
            )

            # Draw text
            legend_surface = font.render(text, True, config.white)
            legend_rect = legend_surface.get_rect()
            legend_rect.topleft = (
                config.legend_x_offset
                + index * config.legend_spacing
                + config.legend_text_x_space,
                config.legend_y_offset - config.legend_text_y_space,
            )
            self.game_window.blit(legend_surface, legend_rect)

    def show_score_strip(self):
        """
        Creates the strip to show the score and legend at the top of the screen.
        """
        pygame.draw.rect(
            self.game_window,
            config.grey,
            pygame.Rect(0, 0, config.window_width, config.strip_height),
        )
        self.show_score()
        self.show_legend()
        # Counter to keep track of red score when eating poisonous fruit
        if self.score_color_counter > 0:
            self.score_color = config.red
            self.score_color_counter -= 1
        else:
            self.score_color = config.white

    def game_over(self):
        """
        Displays the game over message and waits for user input to restart or exit the game.
        """

        # Stop the background music
        pygame.mixer.music.stop()

        # Play the game over sound
        pygame.mixer.music.load(self.game_over_sound)
        pygame.mixer.music.play()

        # Display game over text
        score_surface = pygame.font.SysFont(*config.game_over_font).render(
            f"Your Score is : {self.score}", True, config.blue
        )
        score_rect = score_surface.get_rect()
        score_rect.midtop = (config.window_width / 2, config.window_height / 4)
        self.game_window.blit(score_surface, score_rect)

        restart_surface = pygame.font.SysFont(*config.game_over_font).render(
            "Press space to restart. Escape to exit.", True, config.blue
        )
        restart_rect = restart_surface.get_rect()
        restart_rect.midtop = (config.window_width / 2, config.window_height / 2)
        self.game_window.blit(restart_surface, restart_rect)

        pygame.display.flip()

        while True:
            # Wait for user input
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
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
            elif event.type == pygame.QUIT:
                pygame.quit()
                quit()

        self.snake.move(new_direction, self.fruit, self.directional_blocks)

        # Check if fruit or poisonous fruit eaten
        if self.fruit.eaten:
            self.fruit.poisonous = False
            self.score += 1
            if self.score % config.difficulty_multiple == 0:
                # Increase difficulty based on multiple from config
                self.increase_difficulty()
            self.fruit.eaten = False
            self.fruit.poisonous_eaten = False
            self.fruit.set_position(
                self.snake, self.fruit, self.walls, self.directional_blocks
            )
        elif self.fruit.poisonous_eaten:
            self.score = max(self.score - config.poison_score_penalty, 0)
            snake_len = len(self.snake.body)
            self.snake.body = self.snake.body[
                : max(snake_len - config.poison_score_penalty, config.start_snake_size)
            ]
            self.score_color_counter = config.score_color_counter
            self.fruit.eaten = False
            self.fruit.poisonous_eaten = False
            self.fruit.poisonous = False
            self.fruit.set_position(
                self.snake, self.fruit, self.walls, self.directional_blocks
            )

        self.game_window.fill(config.black)

        # Draw all elements
        self.snake.draw(self.game_window)
        self.fruit.draw(self.game_window)
        self.draw_walls()
        self.draw_directional_blocks()

        # Check for game over
        self.check_game_over()
        self.show_score_strip()
