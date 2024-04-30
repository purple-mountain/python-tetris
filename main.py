import pygame
import sys
from game import Game
from colors import Colors

pygame.init()

title_font = pygame.font.Font(None, 40)
score_surface = title_font.render("Score", True, Colors.white)
next_surface = title_font.render("Next", True, Colors.white)
game_over_surface = title_font.render("Game Over", True, Colors.white)

final_project_surface = title_font.render("Final Project", True, Colors.white)
by_word_surface = title_font.render("By", True, Colors.white)

author_name_surface = title_font.render("Davranbek", True, Colors.white)
author_surname_surface = title_font.render("Jenisbaev", True, Colors.white)
course_code_surface = title_font.render("COSC 2110", True, Colors.white)

score_rect = pygame.Rect(535, 95, 170, 60)
next_rect = pygame.Rect(535, 255, 170, 180)

dimensions = (750, 950)

screen = pygame.display.set_mode(dimensions)
pygame.display.set_caption("Tetris")

clock = pygame.time.Clock()

game = Game()
game_update = pygame.USEREVENT
pygame.time.set_timer(game_update, 200)

run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if game.game_over:
                game.game_over = False
                game.reset()
            if (
                event.key == pygame.K_LEFT or event.key == pygame.K_a
            ) and not game.game_over:
                game.move_left()
            if (
                event.key == pygame.K_RIGHT or event.key == pygame.K_d
            ) and not game.game_over:
                game.move_right()
            if (
                event.key == pygame.K_DOWN or event.key == pygame.K_s
            ) and not game.game_over:
                game.move_down()
                game.update_score(0, 1)
            if (
                event.key == pygame.K_UP or event.key == pygame.K_w
            ) and not game.game_over:
                game.rotate()
        if event.type == game_update and not game.game_over:
            game.move_down()
            game.grid.print_grid()

    score_value_surface = title_font.render(str(game.score), True, Colors.white)

    screen.blit(score_surface, (580, 40, 50, 50))
    screen.blit(next_surface, (590, 200, 50, 50))

    screen.blit(final_project_surface, (530, 600, 50, 50))
    screen.blit(by_word_surface, (590, 640, 50, 50))
    screen.blit(author_name_surface, (540, 680, 50, 50))
    screen.blit(author_surname_surface, (540, 720, 50, 50))
    screen.blit(course_code_surface, (540, 760, 50, 50))

    if game.game_over:
        screen.blit(game_over_surface, (535, 470, 50, 50))

    pygame.draw.rect(screen, Colors.light_blue, score_rect, 0, 10)
    screen.blit(
        score_value_surface,
        score_value_surface.get_rect(
            centerx=score_rect.centerx, centery=score_rect.centery
        ),
    )
    pygame.draw.rect(screen, Colors.light_blue, next_rect, 0, 10)
    game.draw(screen)

    # updating the game (redrawing)
    pygame.display.update()

    # fps
    clock.tick(60)
