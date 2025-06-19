import pygame
from entities import Entity, Player, Enemy
from random import randint

class Game:
    def __init__(self, surface: pygame.surface.Surface) -> None:
        self._enemies = pygame.sprite.Group()
        self._sprites = pygame.sprite.Group()
        self._player = Player(surface, None, self._sprites)

    def game_over(self) -> bool:
        return self._player.is_dead()

    def update(self, surface: pygame.surface.Surface):
        if self.game_over(): return
        self._populate_enemies_group(surface)
        self._sprites.update(surface, self._player.speed())
        self._check_for_crashes()

    def player(self) -> Player:
        return self._player

    def _check_for_crashes(self):
        for current in self._sprites:
            collided = pygame.sprite.spritecollideany(current, self._sprites)
            if current != collided:
                if isinstance(current, Entity): current.hit()
                if isinstance(collided, Entity): collided.hit()
    
    def _populate_enemies_group(self, surface: pygame.surface.Surface):
        if randint(100 - len(self._enemies.sprites() * 2), 100) == 100: 
            Enemy(surface, None, self._enemies, self._sprites)

    def draw(self, surface: pygame.surface.Surface):
        self._sprites.draw(surface)