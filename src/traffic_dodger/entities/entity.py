import pygame

class Entity(pygame.sprite.Sprite):
    def __init__(self, pos: tuple[int, int], image: str, *groups: pygame.sprite.AbstractGroup) -> None:
        super().__init__(*groups)
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.center = pos
