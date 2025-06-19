import pygame
from . import Entity
from random import randint

_DEFAULT_ENEMY_MARGIN_FROM_TOP = -100
_DEFAULT_ENEMY_SPEED = (0, 5)
_DEFAULT_ENEMY_HEALTH = 1

def _default_enemy_position(surface: pygame.surface.Surface):
    return (randint(0, surface.width), _DEFAULT_ENEMY_MARGIN_FROM_TOP)

def _default_enemy_speed():
    return randint(-3, 3), randint(5, 6)

class Enemy(Entity):
    def __init__(self, surface: pygame.surface.Surface, center: tuple[int, int] | None, *groups: pygame.sprite.Group) -> None:
        if center == None: center = _default_enemy_position(surface)
        super().__init__(center, _DEFAULT_ENEMY_HEALTH, "assets/images/enemy.png", *groups)
        self._speed_x, self._speed_y = _default_enemy_speed()

    def update(self, surface: pygame.surface.Surface, system_speed: tuple[int, int]) -> None:
        super().update(surface, system_speed)
        system_speed_x, system_speed_y = system_speed
        assert self.rect != None
        self.rect.move_ip(self._speed_x - system_speed_x, self._speed_y - system_speed_y)
        if self.rect.top > surface.height: 
            self.rect.center = _default_enemy_position(surface)
            self._speed_x, self._speed_y = _default_enemy_speed()