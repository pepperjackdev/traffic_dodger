from typing import Any
import pygame
from . import Entity
from random import randint

def _default_enemy_position(surface: pygame.surface.Surface):
    return (randint(0, surface.width), 0 - 100)

class Enemy(Entity):
    def __init__(self, surface: pygame.surface.Surface, center: tuple[int, int] | None, *groups: pygame.sprite.Group) -> None:
        if center == None: center = _default_enemy_position(surface)
        super().__init__(center, "assets/images/enemy.png", *groups)