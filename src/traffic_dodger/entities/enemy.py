import pygame

from . import Entity

class Enemy(Entity):
    def __init__(self, center: tuple[int, int], *groups: pygame.sprite.Group) -> None:
        super().__init__(center, (0, 5), "assets/images/enemy.png", *groups)