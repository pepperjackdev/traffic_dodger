import pygame
    
class Sheet:
    def __init__(self, folder, name, variants: dict[str, int]) -> None:
        self._sprite_images = dict[str, list]()
        self._load(folder, name, variants)
        self._default_variant = ""
        self._default_index = 0.0
        self._current_variant = self._default_variant
        self._current_index = self._default_index
        self._animation_speed = 0.2

    def _load(self, folder, name, variants: dict[str, int]):
        for variant in variants.keys():
            for index in range(variants[variant]):
                image = pygame.image.load(f"{folder}/{name}{variant}{index}.png")
                if self._sprite_images.get(variant) == None:
                    self._sprite_images[variant] = list()
                self._sprite_images[variant].append(image)

    def get(self) -> pygame.surface.Surface:
        self._step()
        return self._sprite_images[self._current_variant][int(self._current_index)]
        
    def _step(self):
        if self._current_index + self._animation_speed < len(self._sprite_images[self._current_variant]):
            self._current_index += self._animation_speed
        else:
            self._current_variant = self._default_variant
            self._current_index = 0.0
    
    def variant(self, variant: str = "base"):
        self._current_variant = variant
        self._current_index = -self._animation_speed