import pygame

class Entity(pygame.sprite.Sprite):
   def __init__(self, center: tuple[int, int], health: int, image: str, *groups: pygame.sprite.Group) -> None:
      super().__init__(*groups)
      self.image = pygame.image.load(image)
      self.rect = self.image.get_rect()
      self.rect.center = center
      self._health = health

   def speed_x(self) -> int: ...   
   def speed_y(self) -> int: ...
   def speed(self) -> tuple[int, int]: 
      return self.speed_x(), self.speed_y()

   def update(self, surface: pygame.surface.Surface, system_speed: tuple[int, int]) -> None:
      if self.is_dead(): self.kill()

   def is_alive(self) -> bool:
      return self._health > 0
   
   def is_dead(self) -> bool:
      return not self.is_alive()
   
   def health(self) -> int:
      return self._health

   def hit(self, damage: int = 1):
      if self.is_alive(): self._health -= damage