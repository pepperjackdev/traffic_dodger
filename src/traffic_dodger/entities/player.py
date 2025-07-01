from pygame.sprite import Group
from . import Entity

class Player(Entity):
    def __init__(self, speed: tuple[int, int], *groups: Group) -> None:
        super().__init__(speed, "assets/images/car.png", *groups) 