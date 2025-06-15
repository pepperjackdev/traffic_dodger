import pygame
import sys
import time

from entity import Entity
from player import Player
from enemy import Enemy
from pygame.locals import QUIT
from locals import get_score

_WINDOW_WIDTH = _WINDOW_HEIGHT = 600
_WINDOW_SIZE = (_WINDOW_WIDTH, _WINDOW_HEIGHT)
_FPS = 15

def main():
    pygame.init()
    fps = pygame.time.Clock()
    surface = pygame.display.set_mode(_WINDOW_SIZE)
    pygame.display.set_caption("Traffic Dodger")
    
    # fonts
    big_font = pygame.font.SysFont("Bauhaus 93", 60)
    small_font = pygame.font.SysFont("Bauhaus 93", 20)

    # game over
    game_over = big_font.render("Ops... game over.", True, (255, 255, 255))
    game_over_rect = game_over.get_rect()
    game_over_rect.center = (_WINDOW_WIDTH // 2, _WINDOW_HEIGHT // 2)

    # background
    background = pygame.image.load("assets/images/road.png")

    # creating entities
    player = Player((300, 500))
    enemy = Enemy((300, 0))

    # creating groups
    enemies = pygame.sprite.Group()
    enemies.add(enemy)

    all_sprites = pygame.sprite.Group()
    all_sprites.add(player)
    all_sprites.add(enemies)

    # user event
    INCREASE_SPEED = pygame.USEREVENT + 1
    pygame.time.set_timer(INCREASE_SPEED, 1000)

    while True:
        # dispatching events
        for event in pygame.event.get():
            # speed increase event
            if event.type == INCREASE_SPEED:
                for enemy in enemies.sprites():
                    if isinstance(enemy, Enemy): # type check
                        enemy.increase_speed()

            # quit event
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        # clearning up the window
        surface.blit(background, (0, 0))
        scores = small_font.render(f"Score: {get_score()}", True, (0xFF, 0xFF, 0xFF))
        surface.blit(scores, (10, 10))

        # drawing and updating
        for entity in all_sprites:
            if isinstance(entity, Entity):
                surface.blit(entity.image, entity.rect)
                entity.update(surface)

        # checking for player collision
        if pygame.sprite.spritecollideany(player, enemies): #type: ignore
            pygame.mixer.Sound("assets/sounds/crash.wav").play()
            surface.fill((255, 0, 0)) # filling with red
            surface.blit(game_over, game_over_rect)
            surface.blit(scores, (10, 10))
            pygame.display.update()
            for entity in all_sprites:
                if isinstance(entity, Entity):
                    entity.kill()
                
            # finalizing
            time.sleep(3) # waiting...
            pygame.quit()
            sys.exit()

        # display update
        pygame.display.update()
        fps.tick(_FPS)

if __name__ == "__main__":
    main()