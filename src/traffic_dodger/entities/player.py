import pygame
from pygame.locals import K_LEFT, K_RIGHT

from . import Entity

_DEFAULT_PLAYER_MARGIN_FROM_BOTTOM = 100
_DEFAULT_PLAYER_ORTOGONAL_SPEED_X = 5
_DEFAULT_PLAYER_HEALTH = 3

def _default_player_position(surface: pygame.surface.Surface): 
    return (surface.width // 2, surface.height - _DEFAULT_PLAYER_MARGIN_FROM_BOTTOM)

class Player(Entity):
    def __init__(self, surface: pygame.surface.Surface, center: tuple[int, int] | None, *groups: pygame.sprite.Group) -> None:
        if center == None: center = _default_player_position(surface)
        super().__init__(center, _DEFAULT_PLAYER_HEALTH, "assets/images/player.png", *groups)
        self._ortogonal_speed_x = _DEFAULT_PLAYER_ORTOGONAL_SPEED_X

    def update(self, surface: pygame.surface.Surface) -> None:
        super().update(surface)
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_LEFT]: self._move_left()
        if pressed_keys[K_RIGHT]: self._move_right(surface)

    def _move_left(self):
        assert self.rect != None
        if self.rect.left > 0: 
            self.rect.move_ip(-self._ortogonal_speed_x, 0)

    def _move_right(self, surface: pygame.surface.Surface):
        assert self.rect != None
        if self.rect.right < surface.width: 
            self.rect.move_ip(self._ortogonal_speed_x, 0)