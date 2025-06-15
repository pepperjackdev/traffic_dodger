import pygame

class Entity(pygame.sprite.Sprite):
    def __init__(self, position: tuple[int, int], speed: tuple[int, int], image: str) -> None:
        super().__init__()
        self.x_speed, self.y_speed = speed
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.center = position

    def update(self, surface: pygame.surface.Surface) -> None:
        raise NotImplementedError("Not implemented yet")
    
    def speed(self) -> tuple[int, int]:
        return self.x_speed, self.y_speed
    
    def draw(self, surface: pygame.surface.Surface) -> None:
        surface.blit(self.image, self.rect)