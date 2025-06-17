import pygame
import sys

from pygame.locals import QUIT
from entities import Player, Enemy
from game import Game

def main():
    pygame.display.set_caption("Traffic Dodger")
    pygame.display.set_mode((600, 600))

    surface = pygame.display.get_surface()
    assert surface != None

    fps = pygame.time.Clock()

    # populating _enemies
    enemies = pygame.sprite.Group()
    enemies.add(Enemy((300, 100)))
    game = Game(Player((300, 500)), enemies)

    pygame.init()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        game.update(surface)

        surface.fill((100, 100, 100))

        game.draw(surface)

        pygame.display.update()
        fps.tick(60)

if __name__ == "__main__":
    main()