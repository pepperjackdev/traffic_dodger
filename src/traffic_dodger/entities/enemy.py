from typing import Any
import pygame
from . import Entity
from random import randint

_DEFAULT_ENEMY_MARGIN_FROM_TOP = -100
_DEFAULT_ENEMY_SPEED_Y = 5
_DEFAULT_ENEMY_HEALTH = 1

def _default_enemy_position(surface: pygame.surface.Surface):
    return (randint(0, surface.width), _DEFAULT_ENEMY_MARGIN_FROM_TOP)

class Enemy(Entity):
    def __init__(self, surface: pygame.surface.Surface, center: tuple[int, int] | None, *groups: pygame.sprite.Group) -> None:
        if center == None: center = _default_enemy_position(surface)
        super().__init__(center, _DEFAULT_ENEMY_HEALTH, "assets/images/enemy.png", *groups)
        self._speedy = _DEFAULT_ENEMY_SPEED_Y

    def update(self, surface: pygame.surface.Surface) -> None:
        super().update(surface)
        assert self.rect != None
        if self.rect.top < surface.height: self.rect.move_ip(0, self._speedy)
        else: self.rect.center = _default_enemy_position(surface)