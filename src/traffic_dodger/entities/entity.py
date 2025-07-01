import pygame

class Entity(pygame.sprite.Sprite):
    def __init__(self, speed: tuple[int, int], image: str, *groups: pygame.sprite.Group) -> None:
        super().__init__(*groups)
        self._speed_x, self._speed_y = speed
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()

    def speed(self):
        return self._speed_x, self._speed_y
    
    def _relative_speed(self, player_speed):
        player_speed_x, player_speed_y = player_speed
        return self._speed_x - player_speed_x, self._speed_y - player_speed_y

    def update(self, rendering_center, player_speed) -> None:
        super().update()
        self._update_position(player_speed)

    def _update_position(self, player_speed):
        assert self.rect != None
        self.rect.move_ip(self._relative_speed(player_speed))