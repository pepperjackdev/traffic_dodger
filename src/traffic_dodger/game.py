import pygame

from entities import Player, Enemy, Explosion
from random import randint

def _default_player_position(surface: pygame.surface.Surface):
    return surface.width // 2, surface.height - 100

def _default_enemy_position(surface: pygame.surface.Surface):
    return randint(0, surface.width), -100

class Game:
    def __init__(self, surface: pygame.surface.Surface, spawn_rate: int) -> None:
        self._surface = surface
        self._enemies = pygame.sprite.Group()
        self._sprites = pygame.sprite.Group()
        self._characters = pygame.sprite.Group()
        self.player = Player(_default_player_position(surface), self._sprites, self._characters)
        self._enemies_spawn_rate = spawn_rate
        self._paused = False

    def update(self, surface: pygame.surface.Surface | None = None):
        if self._paused: return
        if self.game_over(): return
        self._collisions()
        if surface != None: self._surface = surface
        self._sprites.update(self._surface, self._system_speed())
        if randint(0, 100 - self._enemies_spawn_rate) == 0: self._spawn_enemy()

    def game_over(self) -> bool:
        return self.player.dead()
    
    def pause_replay(self):
        self._paused = not self._paused

    def paused(self) -> bool:
        return self._paused

    def _system_speed(self) -> tuple[int, int]:
        return self.player.absolute_speed()
    
    def _spawn_enemy(self):
        Enemy(_default_enemy_position(self._surface), (-3, 3, 4, 6), self._enemies, self._characters, self._sprites)

    def _collisions(self):
        for sprite in self._characters.sprites():
            if (collided := pygame.sprite.spritecollideany(sprite, self._characters)) != None:
                if sprite != collided:
                    sprite.hit()
                    collided.hit()
                    sx, sy, cx, cy = sprite.rect.center + collided.rect.center
                    Explosion(((sx + cx) // 2, (sy + cy) // 2), self._sprites)
                    
    
    def draw(self, surface: pygame.surface.Surface):
        self._sprites.draw(surface)