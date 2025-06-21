from pygame.sprite import Group
from . import Entity

class Player(Entity):
    def __init__(self, 
                 absolute_position: tuple[int, int], 
                 absolute_direction: float, 
                 absolute_speed: tuple[int, int],
                 *groups: Group) -> None:
        super().__init__(absolute_position, absolute_direction, absolute_speed, "assets/images/car.png", *groups)

    def update(self, system_absolute_position: tuple[int, int], system_absolute_direction: float, rendering_center: tuple[int, int]) -> None:
        super().update(system_absolute_position, system_absolute_direction, rendering_center)
        self._absolute_direction += 0.001