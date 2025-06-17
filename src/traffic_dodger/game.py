import pygame

from pygame.sprite import Group
from pygame.surface import Surface
from entities import Player

class Game:
    def __init__(self, player: Player, enemies: Group) -> None:
        self._enemies = enemies
        self._sprites = Group()
        self._sprites.add(player)
        self._sprites.add(enemies)

    def game_over(self) -> bool:
        for sprite in self._sprites.sprites():
            if isinstance(sprite, Player):
                return False
        return True

    def update(self, surface: Surface):
        if self.game_over(): return
        self._sprites.update(surface)

    def draw(self, surface: Surface):
        self._sprites.draw(surface)