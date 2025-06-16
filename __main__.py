import pygame
import sys

from pygame.locals import QUIT
from entities import Player

_WINDOW_WIDTH = 600
_WINDOW_HEIGHT = 600
_WINDOW_SIZE = _WINDOW_WIDTH, _WINDOW_HEIGHT

_FRAMERATE = 60

WHITE = 255, 255, 255

pygame.display.set_mode(_WINDOW_SIZE)
pygame.display.set_caption("Traffic Dodger")

surface = pygame.display.get_surface()
assert surface != None

fps = pygame.time.Clock()

pygame.init()

# tmp
player = Player((300, 300))

while True:
    """ Dispatching events """
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    """ Updating game """

    """ Drawing up the sprites """
    assert player.image != None and player.rect != None
    surface.blit(player.image, player.rect)

    """ Updating the display """
    pygame.display.update()
    fps.tick(_FRAMERATE)