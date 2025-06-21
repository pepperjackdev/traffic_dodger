import pygame
from math import pi

from entities import Player, Enemy

class Game:
    def __init__(self, surface: pygame.surface.Surface) -> None:
        self._surface = surface
        self._enemies = pygame.sprite.Group()
        self._sprites = pygame.sprite.Group()
        self._player = Player((0, 0), 0, (0, 0), self._sprites)
        Enemy((100, 100), 0, (0, 0), self._sprites, self._enemies)

    def update(self, surface: pygame.surface.Surface | None = None):
        if surface != None: self._surface = surface
        self._sprites.update(self._player.absolute_position(), self._player.absolute_direction(), (300, 300))
                
    def draw(self, surface: pygame.surface.Surface):
        self._sprites.draw(surface)