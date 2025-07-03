import pygame
import sys

from pygame.locals import QUIT, K_RETURN, K_UP, K_DOWN, K_LSHIFT, K_SPACE
from game import Game

_WINDOW_TITLE = "Traffic Dodger"

_WINDOW_WIDTH = 600
_WINDOW_HEIGHT = 600
_WINDOW_SIZE = _WINDOW_WIDTH, _WINDOW_HEIGHT

_WINDOW_CENTER = _WINDOW_WIDTH // 2, _WINDOW_HEIGHT // 2

_FRAMERATE = 60

_BACKGROUND = (100, 100, 100)
_GAME_OVER_BACKGROUND = (100, 0, 0)

_BLACK = (0, 0, 0)
_WHITE = (255, 255, 255)

pygame.init()

_VERY_LITTLE_FONT = pygame.font.SysFont("Verdana", 15)
_LITTLE_FONT = pygame.font.Font("assets/fonts/pixelify_sans_variable.ttf", 20)
_MEDIUM_FONT = pygame.font.Font("assets/fonts/pixelify_sans_variable.ttf", 30)
_BIG_FONT = pygame.font.Font("assets/fonts/pixelify_sans_variable.ttf", 60)

# configs
spawn_rate = 10

def draw_start_ui(surface: pygame.surface.Surface):
    surface.fill(_BLACK)

    title = _BIG_FONT.render(_WINDOW_TITLE, True, _WHITE)
    surface.blit(title, title.get_rect(center=(_WINDOW_WIDTH // 2, 100)))

    subtitle = _LITTLE_FONT.render("To start the game, press Enter.", True, _WHITE)
    surface.blit(subtitle, subtitle.get_rect(center=(_WINDOW_WIDTH // 2, 150)))

    spawn_rate_indicator = _MEDIUM_FONT.render(f"Spawn rate: {spawn_rate}%", True, _WHITE)
    surface.blit(spawn_rate_indicator, spawn_rate_indicator.get_rect(center=(_WINDOW_WIDTH // 2, 300)))

    spawn_rate_edit_instructions = _VERY_LITTLE_FONT.render("Use <ArrowUp> or <ArrowDown> to adjust the enemies' spawn rate;", True, _WHITE)
    surface.blit(spawn_rate_edit_instructions, spawn_rate_edit_instructions.get_rect(center=(_WINDOW_WIDTH // 2, _WINDOW_HEIGHT - 60)))

    game_instructions = _VERY_LITTLE_FONT.render("a/d: lef/right; w/s: speed/slow; space: pause; enter: this.", True, _WHITE)
    surface.blit(game_instructions, game_instructions.get_rect(center=(_WINDOW_WIDTH // 2, _WINDOW_HEIGHT - 45)))

def main():
    global spawn_rate

    pygame.display.set_caption(_WINDOW_TITLE)
    pygame.display.set_mode(_WINDOW_SIZE)

    surface = pygame.display.get_surface()
    assert surface != None
    fps = pygame.time.Clock()

    game = None
    
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        keys_just_pressed = pygame.key.get_just_pressed()
        keys_pressed = pygame.key.get_pressed()    
            
        if game == None:
            if keys_just_pressed[K_RETURN]:
                game = Game(surface, spawn_rate)

            if keys_just_pressed[K_UP]:
                spawn_rate += 1 if not keys_pressed[K_LSHIFT] else 10
                if spawn_rate > 100:
                    spawn_rate = 100
            
            if keys_just_pressed[K_DOWN]:
                spawn_rate -= 1 if not keys_pressed[K_LSHIFT] else 10
                if spawn_rate < 0:
                    spawn_rate = 0
        else:
            if keys_just_pressed[K_RETURN]:
                game = None

            if keys_just_pressed[K_SPACE]:
                assert game != None
                game.pause_replay()

        if game == None:
            draw_start_ui(surface)
        else:
            game.update()

            surface.fill(_BACKGROUND)
            game.draw(surface)

            if game.game_over():
                surface.fill(_GAME_OVER_BACKGROUND)
                game_over = _BIG_FONT.render("Ops. Game Over.", True, _WHITE)
                surface.blit(game_over, game_over.get_rect(center=_WINDOW_CENTER))
            
            if game.paused():
                pause_info = _BIG_FONT.render("Pause", True, _WHITE)
                surface.blit(pause_info, pause_info.get_rect(center=_WINDOW_CENTER))

            score = _MEDIUM_FONT.render(f"Score: {game.player.score()}", True, _WHITE)
            surface.blit(score, (0, 10))

            health = _MEDIUM_FONT.render(f"Health: {game.player._health}", True, _WHITE)
            surface.blit(health, (0, 40))

            speed = _MEDIUM_FONT.render(f"Speed: {-game.player.absolute_speed_y()}", True, _WHITE)
            surface.blit(speed, (0, 70))
    
        pygame.display.update()
        fps.tick(_FRAMERATE)

if __name__ == "__main__":
    main()