import pygame
import sys

from pygame.locals import QUIT
from entities import Player
from game import Game

_WINDOW_WIDTH = 600
_WINDOW_HEIGHT = 600
_WINDOW_SIZE = _WINDOW_WIDTH, _WINDOW_HEIGHT

_PLAYER_MARGIN_FROM_BOTTOM = 100
_PLAYER_START_X = _WINDOW_WIDTH // 2
_PLAYER_START_Y = _WINDOW_HEIGHT - _PLAYER_MARGIN_FROM_BOTTOM
_PLAYER_START_POS = _PLAYER_START_X, _PLAYER_START_Y

_FRAMERATE = 60

_BACKGROUND_COLOR = 200, 200, 200

def main():
    """ Pygame configs """
    pygame.display.set_mode(_WINDOW_SIZE)
    pygame.display.set_caption("Traffic Dodger")

    surface = pygame.display.get_surface()
    assert surface != None

    fps = pygame.time.Clock()

    """ Game setup """
    sprites = pygame.sprite.Group()
    sprites.add(Player(_PLAYER_START_POS))
    game = Game(sprites)

    pygame.init()

    """ Mainloop """
    while True:

        """ Dispatching events """
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        """ Updating game """
        game.update(surface)

        """ Clearning up """
        surface.fill(_BACKGROUND_COLOR)

        """ Drawing sprites """
        game.draw(surface)

        """ Updating the display """
        pygame.display.update()
        fps.tick(_FRAMERATE)

if __name__ == "__main__":
    main()