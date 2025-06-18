import pygame

class Entity(pygame.sprite.Sprite):
     def __init__(self, center: tuple[int, int], image: str, *groups: pygame.sprite.Group) -> None:
        super().__init__(*groups)
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.center = center