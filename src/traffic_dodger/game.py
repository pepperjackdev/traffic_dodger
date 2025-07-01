import pygame

from entities import Player

class Game:
    def __init__(self, surface: pygame.surface.Surface) -> None:
        self._surface = surface
        self._sprites = pygame.sprite.Group()
        self._enemies = pygame.sprite.Group()
        self._player = Player((0, -5), self._sprites)

    def update(self):
        self._sprites.update(self._surface.get_rect().center, self._player.speed())

    def draw(self):
        self._sprites.draw(self._surface)