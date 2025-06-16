import pygame

from entities import Entity
from random import randint
from locals import MARGIN, inc_score

class Enemy(Entity):
    def __init__(self, position: tuple[int, int]) -> None:
        super().__init__(position, (0, 10), "assets/images/enemy.png")

    def increase_speed(self):
        self.y_speed += 1

    def update(self, surface: pygame.surface.Surface) -> None:
        self.rect.move_ip(self.speed())
        if self.rect.bottom > surface.get_height():
            self.rect.top = 0
            self.rect.center = (randint(MARGIN, surface.get_width() - MARGIN), 0)
            inc_score()