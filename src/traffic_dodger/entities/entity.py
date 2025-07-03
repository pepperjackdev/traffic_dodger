import pygame
from sprites import Sheet

class Entity(pygame.sprite.Sprite):
   def __init__(self, position: tuple[int, int], health: int, speed: tuple[float, float], sheet: Sheet, *groups: pygame.sprite.Group) -> None:
      super().__init__(*groups)
      self._absolute_speed_x, self._absolute_speed_y = speed
      self._sheet = sheet
      self.image = self._sheet.get()
      self.rect = self.image.get_rect(center=position)
      self._health = health

   def _update_image(self):
      assert self.image != None
      self.image = self._sheet.get()

   def absolute_speed_x(self) -> int: 
      return int(self._absolute_speed_x)
   
   def absolute_speed_y(self) -> int:
      return int(self._absolute_speed_y)

   def absolute_speed(self) -> tuple[int, int]:
      return self.absolute_speed_x(), self.absolute_speed_y()

   def relative_speed_x(self, system_speed_x: int):
      return self.absolute_speed_x() - system_speed_x
   
   def relative_speed_y(self, system_speed_y: int):
      return self.absolute_speed_y() - system_speed_y
   
   def relative_speed(self, system_speed: tuple[int, int]):
      system_speed_x, system_speed_y = system_speed
      return self.relative_speed_x(system_speed_x), self.relative_speed_y(system_speed_y)

   def update(self, surface: pygame.surface.Surface, system_speed: tuple[int, int]) -> None:
      if self.dead(): self.kill()
      self._move(system_speed)
      self._update_image()

   def hit(self):
      self._health -= 1

   def dead(self):
      return self._health <= 0

   def _move(self, system_speed):
      system_speed_x, system_speed_y = system_speed
      self._move_x(self.relative_speed_x(system_speed_x))
      self._move_y(self.relative_speed_y(system_speed_y))
         
   def _move_x(self, delta_x):
      assert self.rect != None
      self.rect.move_ip(delta_x, 0)
   
   def _move_y(self, delta_y):
      assert self.rect != None
      self.rect.move_ip(0, delta_y)