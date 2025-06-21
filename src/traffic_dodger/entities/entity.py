from typing import Any
import pygame

from math import sin, cos, degrees

class Entity(pygame.sprite.Sprite):
   def __init__(self, 
                absolute_position: tuple[int, int],
                absolute_direction: float,
                absolute_speed: tuple[int, int],
                image: str, *groups: pygame.sprite.Group) -> None:
      super().__init__(*groups)
      self._absolute_position_x, self._absolute_position_y = absolute_position
      self._absolute_direction = absolute_direction
      self._absolute_speed_x, self._absolute_speed_y = absolute_speed
      self._original_image = pygame.image.load(image)
      self.image = self._original_image.copy()
      self.rect = self.image.get_rect()

   def absolute_position(self) -> tuple[int, int]:
      return self._absolute_position_x, self._absolute_position_y
   
   def absolute_direction(self) -> float:
      return self._absolute_direction
   
   def absolute_speed(self) -> tuple[int, int]:
      return self._absolute_speed_x, self._absolute_position_y
      
   def relative_position(self, system_absolute_position: tuple[int, int], system_absolute_direction: float) -> tuple[int, int]:
      relative_direction = self.relative_direction(system_absolute_direction)
      system_absolute_x, system_absolute_y = system_absolute_position
      return (self._relative_position_x(system_absolute_x, relative_direction), 
              self._relative_position_y(system_absolute_y, relative_direction))
   
   def _relative_position_x(self, system_absolute_x: int, relative_direction: float):
      return round(cos(relative_direction) * self._absolute_position_x + sin(relative_direction) * self._absolute_position_y - system_absolute_x)
   
   def _relative_position_y(self, system_absolute_y: int, relative_direction: float):
      return round(-sin(relative_direction) * self._absolute_position_x + cos(relative_direction) * self._absolute_position_y - system_absolute_y)

   def relative_direction(self, system_absolute_direction: float) -> float:
      return self._absolute_direction - system_absolute_direction

   def update(self, system_absolute_position: tuple[int, int], system_absolute_direction: float, rendering_center: tuple[int, int]) -> None:
      self._perform_translation()
      self._update_rendering_on_surface(system_absolute_position, system_absolute_direction, rendering_center)

   def _perform_translation(self):
      self._absolute_position_x += self._absolute_speed_x
      self._absolute_position_y += self._absolute_speed_y

   def _update_rendering_on_surface(self, system_absolute_position: tuple[int, int], system_absolute_direction: float, rendering_center: tuple[int, int]):
      self._update_position_on_surface(system_absolute_position, system_absolute_direction, rendering_center)
      self._update_direction_on_surface(system_absolute_direction)

   def _update_position_on_surface(self, system_absolute_position: tuple[int, int], system_absolute_direction: float, rendering_center: tuple[int, int]) -> None:
      assert self.rect != None
      self.rect.center = self._relative_position_on_screen(system_absolute_position, system_absolute_direction, rendering_center)

   def _relative_position_on_screen(self, system_absolute_position: tuple[int, int], system_absolute_direction: float, rendering_center: tuple[int, int]) -> tuple[int, int]:
      relative_x, relative_y = self.relative_position(system_absolute_position, system_absolute_direction)
      rendering_center_x, rendering_center_y = rendering_center
      return relative_x + rendering_center_x, -(relative_y) + rendering_center_y
   
   def _update_direction_on_surface(self, system_absolute_direction: float):
      assert self.image != None and self.rect != None
      rotation = self.relative_direction(system_absolute_direction)
      self.image = pygame.transform.rotate(self._original_image.copy(), degrees(rotation))
      self.rect = self.image.get_rect(center=self.rect.center)