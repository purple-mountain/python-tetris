import pygame
from grid import Grid
from blocks import *
import random


class Game:
    def __init__(self):
        self.grid = Grid()
        self.blocks = [
            IBlock(),
            JBlock(),
            OBlock(),
            TBlock(),
            ZBlock(),
            LBlock(),
            SBlock(),
        ]
        self.rotate_sound = pygame.mixer.Sound("./Sounds/rotate.ogg")
        self.clear_sound = pygame.mixer.Sound("./Sounds/clear.ogg")
        self.current_block = self.get_random_block()
        self.next_block = self.get_random_block()
        self.game_over = False
        self.score = 0
        pygame.mixer.music.load("./Sounds/Soviet_National_Anthem.ogg")
        pygame.mixer.music.play(-1)

    def update_score(self, lines_cleared, move_down_points):
        if lines_cleared == 1:
            self.score += 100
        elif lines_cleared == 2:
            self.score += 300
        elif lines_cleared == 3:
            self.score += 500
        self.score += move_down_points

    def draw(self, screen):
        self.grid.draw(screen)
        self.current_block.draw(screen, 26, 26)

        if self.next_block.id == 3:
            self.next_block.draw(screen, 390, 320)
        elif self.next_block.id == 4:
            self.next_block.draw(screen, 405, 310)
        else:
            self.next_block.draw(screen, 420, 300)

    def get_random_block(self):
        if len(self.blocks) == 0:
            self.blocks = [
                IBlock(),
                JBlock(),
                OBlock(),
                TBlock(),
                ZBlock(),
                LBlock(),
                SBlock(),
            ]

        block = random.choice(self.blocks)
        self.blocks.remove(block)
        return block

    def block_inside(self):
        tiles = self.current_block.get_cell_positions()
        for tile in tiles:
            if not self.grid.is_inside(tile.row, tile.column):
                return False
        return True

    def block_fits(self):
        tiles = self.current_block.get_cell_positions()
        for tile in tiles:
            if not self.grid.is_empty(tile.row, tile.column):
                return False
        return True

    def move_left(self):
        self.current_block.move(0, -1)
        if not self.block_inside() or not self.block_fits():
            self.current_block.move(0, 1)

    def move_right(self):
        self.current_block.move(0, 1)
        if not self.block_inside() or not self.block_fits():
            self.current_block.move(0, -1)

    def reset(self):
        self.grid.reset()
        self.blocks = [
            IBlock(),
            JBlock(),
            OBlock(),
            TBlock(),
            ZBlock(),
            LBlock(),
            SBlock(),
        ]
        self.current_block = self.get_random_block()
        self.next_block = self.get_random_block()
        self.score = 0

    def rotate(self):
        self.current_block.rotate()
        if not self.block_inside() or not self.block_fits():
            self.current_block.undo_rotation()
        else:
            self.rotate_sound.play()

    def move_down(self):
        self.current_block.move(1, 0)
        if not self.block_inside() or not self.block_fits():
            self.current_block.move(-1, 0)
            self.lock_block()

    def lock_block(self):
        tiles = self.current_block.get_cell_positions()
        for position in tiles:
            self.grid.grid[position.row][position.column] = self.current_block.id
        self.current_block = self.next_block
        self.next_block = self.get_random_block()
        rows_cleared = self.grid.clear_full_rows()
        if rows_cleared > 0:
            self.clear_sound.play()
            self.update_score(rows_cleared, 0)
        if not self.block_fits():
            self.game_over = True
