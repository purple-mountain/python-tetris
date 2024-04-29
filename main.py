import pygame
import sys
from grid import Grid

pygame.init()

dimensions = (450, 900)

screen = pygame.display.set_mode(dimensions)
pygame.display.set_caption("Tetris")

clock = pygame.time.Clock()

game_grid = Grid()
game_grid.grid[0][1] = 1
game_grid.grid[0][0] = 1
game_grid.grid[19][2] = 7
game_grid.print_grid()

run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    game_grid.draw(screen)
    # updating the game (redrawing)
    pygame.display.update()

    # fps
    clock.tick(30)
