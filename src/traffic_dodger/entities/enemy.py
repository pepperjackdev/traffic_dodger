import pygame

from . import Entity
from random import randint

from sprites import Sheet

class Enemy(Entity):
    def __init__(self, center: tuple[int, int], limits: tuple[int, int, int, int], *groups: pygame.sprite.Group) -> None:
        self._min_speed_x, self._max_speed_x, self._min_speed_y, self._max_speed_y = limits
        super().__init__(center, 1, self._compute_speed(), Sheet("assets/sprites/enemy", "enemy", {"": 20}), *groups)

    def _compute_speed(self) -> tuple[int, int]:
        return self._compute_speed_x(), self._compute_speed_y()
    
    def _compute_speed_x(self) -> int:
        return randint(self._min_speed_x, self._max_speed_x)
    
    def _compute_speed_y(self) -> int:
        return randint(self._min_speed_y, self._max_speed_y)
    
    def update(self, surface: pygame.Surface, system_speed: tuple[int, int]) -> None:
        super().update(surface, system_speed)
        if randint(0, 100) == 0: self._absolute_speed_x, self._absolute_speed_y = self._compute_speed()