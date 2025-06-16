from typing import Any
import pygame

class Entity(pygame.sprite.Sprite):
    def __init__(self, pos: tuple[int, int], speed: tuple[int, int], image: str) -> None:
        super().__init__()
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self._x_speed, self._y_speed = speed

    def update(self, surface: pygame.surface.Surface) -> None:
        return super().update()