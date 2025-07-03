from pygame import Surface
from pygame.sprite import Group
from entities import Entity

from sprites import Sheet

class Explosion(Entity):
    def __init__(self, position: tuple[int, int], *groups: Group) -> None:
        super().__init__(position, 30, (0, 0), Sheet("assets/sprites/explosion", "explosion", {"": 7}), *groups)

    def hit(self):
        pass # explosions are invulnerable

    def _cound_down_step(self):
        self._health -= 1

    def update(self, surface: Surface, system_speed: tuple[int, int]) -> None:
        super().update(surface, system_speed)
        self._cound_down_step()