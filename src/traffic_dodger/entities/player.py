import pygame
from pygame.locals import K_LEFT, K_RIGHT

from . import Entity
from locals import PLAYER_IMAGE

_DEFAULT_POTENTIAL_PLAYER_X_SPEED = 5
_DEFAULT_POTENTIAL_PLAYER_Y_SPEED = 0
_DEFAULT_POTENTIAL_PLAYER_SPEED = _DEFAULT_POTENTIAL_PLAYER_X_SPEED, _DEFAULT_POTENTIAL_PLAYER_Y_SPEED

class Player(Entity):
    def __init__(self, pos: tuple[int, int]) -> None:
        super().__init__(pos, _DEFAULT_POTENTIAL_PLAYER_SPEED, PLAYER_IMAGE)

    def update(self, surface: pygame.surface.Surface) -> None:
        keys = pygame.key.get_pressed()

        assert self.rect != None
        if keys[K_LEFT]:
            if self.rect.left > 0:
                self.rect.move_ip((-self._x_speed, 0))
        
        if keys[K_RIGHT]:
            if self.rect.right < surface.width:
                self.rect.move_ip((self._x_speed, 0))