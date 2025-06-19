import pygame

from entities import Player, Enemy
from random import randint

def _default_player_position(surface: pygame.surface.Surface):
    return surface.width // 2, surface.height - 100

def _default_enemy_position(surface: pygame.surface.Surface):
    return randint(0, surface.width), -100

class Game:
    def __init__(self, surface: pygame.surface.Surface) -> None:
        self._surface = surface
        self._enemies = pygame.sprite.Group()
        self._sprites = pygame.sprite.Group()
        self._player = Player(_default_player_position(surface), self._sprites)

    def update(self, surface: pygame.surface.Surface | None = None):
        if surface != None: self._surface = surface
        self._sprites.update(self._surface, self._system_speed())
        if randint(1, 10) == 10: self._spawn_enemy()

    def _system_speed(self) -> tuple[int, int]:
        return self._player.absolute_speed()
    
    def _spawn_enemy(self):
        Enemy(_default_enemy_position(self._surface), self._enemies, self._sprites)
    
    def draw_sprites(self, surface: pygame.surface.Surface):
        self._sprites.draw(surface)