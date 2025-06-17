import pygame
from . import Entity
from pygame.locals import K_LEFT, K_RIGHT

class Player(Entity):
    def __init__(self, center: tuple[int, int]) -> None:
        super().__init__(center, "assets/images/player.png")

    def update(self, surface: pygame.surface.Surface) -> None:
        pressed_keys = pygame.key.get_pressed()
        assert self.rect != None
        if pressed_keys[K_LEFT] and self.rect.left > 0:
            self.rect.move_ip((-5, 0))
        if pressed_keys[K_RIGHT] and self.rect.right < surface.width:
            self.rect.move_ip((5, 0))