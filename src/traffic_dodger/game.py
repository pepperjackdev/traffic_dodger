from pygame.sprite import Sprite, Group
from pygame.surface import Surface
from entities import Entity, Player, Enemy

class Game:
    def __init__(self, sprites: Group[Sprite]) -> None:
        self._sprites = sprites

    def update(self, surface: Surface):
        for sprite in self._sprites:
            if isinstance(sprite, Entity):
                sprite.update(surface)

    def kill(self, sprite: Sprite):
        self._sprites.remove(sprite)

    def draw(self, surface: Surface):
        for sprite in self._sprites:
            assert sprite.image != None
            assert sprite.rect != None
            surface.blit(sprite.image, sprite.rect)

    def game_over(self) -> bool:
        for sprite in self._sprites:
            if isinstance(sprite, Player):
                return False
        return True