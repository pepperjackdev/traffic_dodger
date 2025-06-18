import pygame
from entities import Player, Enemy

class Game:
    def __init__(self, surface: pygame.surface.Surface) -> None:
        self._enemies = pygame.sprite.Group()
        self._sprites = pygame.sprite.Group()

        Player(surface, None, self._sprites)
        Enemy(surface, None, self._enemies, self._sprites)

    def game_over(self) -> bool:
        for sprite in self._sprites.sprites():
            if isinstance(sprite, Player):
                return False
        return True

    def update(self, surface: pygame.surface.Surface):
        if self.game_over(): return
        self._sprites.update(surface)

    def draw(self, surface: pygame.surface.Surface):
        self._sprites.draw(surface)