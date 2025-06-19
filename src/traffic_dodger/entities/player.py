import pygame
from pygame.locals import K_w, K_s, K_a, K_d

from . import Entity

_DEFAULT_PLAYER_MARGIN_FROM_BOTTOM = 100
_DEFAULT_PLAYER_ORTOGONAL_SPEED = (5, 9)
_DEFAULT_PLAYER_HEALTH = 3

def _default_player_position(surface: pygame.surface.Surface): 
    return (surface.width // 2, surface.height - _DEFAULT_PLAYER_MARGIN_FROM_BOTTOM)

class Player(Entity):
    def __init__(self, surface: pygame.surface.Surface, center: tuple[int, int] | None, *groups: pygame.sprite.Group) -> None:
        if center == None: center = _default_player_position(surface)
        super().__init__(center, _DEFAULT_PLAYER_HEALTH, "assets/images/player.png", *groups)
        self._ortogonal_x_speed, self._ortogonal_y_speed = _DEFAULT_PLAYER_ORTOGONAL_SPEED

    def speed_x(self):
        speed_x = 0
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[K_d]: speed_x += self._ortogonal_x_speed
        if keys_pressed[K_a]: speed_x -= self._ortogonal_x_speed
        return speed_x
    
    def speed_y(self):
        speed_y = 0
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[K_s]: speed_y += self._ortogonal_y_speed
        if keys_pressed[K_w]: speed_y -= self._ortogonal_y_speed
        return speed_y

    def update(self, surface: pygame.surface.Surface, system_speed: tuple[int, int]) -> None:
        super().update(surface, system_speed)