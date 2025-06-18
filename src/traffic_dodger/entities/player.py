import pygame
from . import Entity

_DEFAULT_PLAYER_MARGIN_FROM_BOTTOM = 100

def _default_player_position(surface: pygame.surface.Surface): 
    return (surface.width // 2, surface.height - _DEFAULT_PLAYER_MARGIN_FROM_BOTTOM)

class Player(Entity):
    def __init__(self, surface: pygame.surface.Surface, center: tuple[int, int] | None, *groups: pygame.sprite.Group) -> None:
        if center == None: center = _default_player_position(surface)
        super().__init__(center, "assets/images/player.png", *groups)