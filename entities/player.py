import pygame
from pygame.locals import K_LEFT, K_RIGHT

from entities.entity import Entity

class Player(Entity):
    def __init__(self, position: tuple[int, int]) -> None:
        super().__init__(position, (5, 0), "assets/images/player.png")

    def update(self, surface: pygame.surface.Surface) -> None:
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0 and pressed_keys[K_LEFT]:
            self.rect.move_ip(-self.x_speed, 0)
        if self.rect.right < surface.get_width() and pressed_keys[K_RIGHT]:
            self.rect.move_ip(self.x_speed, 0)