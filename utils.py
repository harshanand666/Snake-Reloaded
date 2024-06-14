import config
import random


def get_random_position():
    """
    Gets a random position on the game window

    Returns:
        List: x,y coordinates of the position
    """
    return [
        random.randrange(1, (config.window_width // config.block_size))
        * config.block_size,
        config.strip_height
        + random.randrange(1, (config.game_window_height // config.block_size))
        * config.block_size,
    ]


def overlap_all(position, snake, fruit, walls, directional_blocks):
    """
    Checks if a given position overlaps with the snake, walls, or directional blocks.

    Args:
        position (list): The position to check for overlap.

    Returns:
        bool: True if there is an overlap, False otherwise.
    """
    if position in snake.body:
        return True
    elif any([position in wall for wall in walls]):
        return True
    elif position in directional_blocks:
        return True
    elif position in fruit.position or position in fruit.poisonous_position:
        return True
    return False
