import pygame
import sys

from pygame.locals import QUIT
from game import Game

_WINDOW_TITLE = "Traffic Dodger"

_WINDOW_WIDTH = 600
_WINDOW_HEIGHT = 600
_WINDOW_SIZE = _WINDOW_WIDTH, _WINDOW_HEIGHT

_WINDOW_CENTER_X = _WINDOW_WIDTH // 2
_WINDOW_CENTER_Y = _WINDOW_HEIGHT // 2
_WINDOW_CENTER = _WINDOW_CENTER_X, _WINDOW_CENTER_Y

_FRAMERATE = 60

_BACKGROUND = (100, 100, 100)

def main():
    pygame.display.set_caption(_WINDOW_TITLE)
    pygame.display.set_mode(_WINDOW_SIZE)

    surface = pygame.display.get_surface()
    assert surface != None
    fps = pygame.time.Clock()
    
    game = Game(surface)
    
    pygame.init()
    
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
    
        game.update()
    
        surface.fill(_BACKGROUND)
        game.draw(surface)
    
        pygame.display.update()
        fps.tick(_FRAMERATE)

if __name__ == "__main__":
    main()