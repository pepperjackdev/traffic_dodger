from pygame.sprite import Group
from . import Entity

class Enemy(Entity):
    def __init__(self, 
                 absolute_position: tuple[int, int], 
                 absolute_direction: float, 
                 absolute_speed: tuple[int, int], 
                 *groups: Group) -> None:
        super().__init__(absolute_position, absolute_direction, absolute_speed, "assets/images/car.png", *groups)