from pygame.sprite import AbstractGroup
from . import Entity

class Player(Entity):
    def __init__(self, pos: tuple[int, int], *groups: AbstractGroup) -> None:
        super().__init__(pos, "assets/images/car.png", *groups)