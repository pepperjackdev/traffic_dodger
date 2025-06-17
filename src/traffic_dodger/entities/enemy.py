from pygame import Surface
from . import Entity

class Enemy(Entity):
    def __init__(self, center: tuple[int, int]) -> None:
        super().__init__(center, "assets/images/enemy.png")
        self._speedx, self._speedy = (0, 5)
    
    def update(self, surface: Surface) -> None:
        assert self.rect != None
        self.rect.move_ip((self._speedx, self._speedy))
        if self.rect.top > surface.height:
            self.rect.y = 0 - self.rect.height