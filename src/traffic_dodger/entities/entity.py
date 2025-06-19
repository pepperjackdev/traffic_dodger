import pygame

class Entity(pygame.sprite.Sprite):
   def __init__(self, center: tuple[int, int], speed: tuple[int, int], image: str, *groups: pygame.sprite.Group) -> None:
      super().__init__(*groups)
      self._absolute_speed_x, self._absolute_speed_y = speed
      self.image = pygame.image.load(image)
      self.rect = self.image.get_rect()
      self.rect.center = center

   def absolute_speed_x(self) -> int:
      return self._absolute_speed_x
   
   def absolute_speed_y(self) -> int:
      return self._absolute_speed_y

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
      system_speed_x, system_speed_y = system_speed
      assert self.rect != None
      self.rect.move_ip(self.relative_speed_x(system_speed_x), self.relative_speed_y(system_speed_y))