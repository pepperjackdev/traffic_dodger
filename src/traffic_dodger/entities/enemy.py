from pygame.sprite import AbstractGroup
from . import Entity
from locals import ENEMY_IMAGE

_DEFAULT_POTENTIAL_ENEMY_X_SPEED = 5
_DEFAULT_POTENTIAL_ENEMY_Y_SPEED = 0
_DEFAULT_POTENTIAL_ENEMY_SPEED = _DEFAULT_POTENTIAL_ENEMY_X_SPEED, _DEFAULT_POTENTIAL_ENEMY_Y_SPEED

class Enemy(Entity):
    def __init__(self, pos: tuple[int, int]) -> None:
        super().__init__(pos, _DEFAULT_POTENTIAL_ENEMY_SPEED, ENEMY_IMAGE)