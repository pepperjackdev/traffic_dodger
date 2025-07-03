import pygame
from pygame.locals import K_a, K_d, K_w, K_s

from . import Entity

from sprites import Sheet

class Player(Entity):
    def __init__(self, center: tuple[int, int], *groups: pygame.sprite.Group) -> None:
        super().__init__(center, 10, (0, -6), Sheet("assets/sprites", "player", {"": 1}), *groups)
        self._score = 0

    @staticmethod
    def _x_variation():
        keys = pygame.key.get_pressed()
        x_variation = 0
        if keys[K_a]: x_variation -= 5
        if keys[K_d]: x_variation += 5
        return x_variation

    @staticmethod
    def _y_variation():
        keys = pygame.key.get_pressed()
        y_variation = 0
        if keys[K_w]: y_variation -= 2
        if keys[K_s]: y_variation += 2
        return y_variation
    
    def score(self):
        return self._score
    
    def update(self, surface: pygame.Surface, system_speed: tuple[int, int]) -> None:
        super().update(surface, system_speed)
        self._score += abs(self.absolute_speed_y())
        self._absolute_speed_y -= 0.001

    def absolute_speed_x(self) -> int:
        return super().absolute_speed_x() + self._x_variation()
    
    def absolute_speed_y(self) -> int:
        return super().absolute_speed_y() + self._y_variation()