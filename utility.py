from random import randint

def generate_random_position(x_max: int, y_max: int, x_min: int = 0, y_min: int = 0) -> tuple[int, int]:
    return (randint(x_max, x_min), randint(y_max, y_min))

def generate_random_position_inside_screen(size: tuple[int, int]):
    width, height = size
    return generate_random_position(width, height)