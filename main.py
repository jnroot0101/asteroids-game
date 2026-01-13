import pygame

from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state
from player import Player


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x, y)

    while True:
        log_state()

        delta_time = clock.tick(60) / 1000
        dt += delta_time

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        player.update(dt)

        screen.fill("black")
        player.draw(screen)
        pygame.display.flip()


if __name__ == "__main__":
    main()
