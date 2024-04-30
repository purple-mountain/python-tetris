import pygame
from colors import Colors


class Grid:
    def __init__(self) -> None:
        self.num_rows = 20
        self.num_columns = 10
        self.cell_size = 45
        self.grid = [[0 for j in range(self.num_columns)] for i in range(self.num_rows)]
        self.colors = Colors.get_cell_colors()

    def print_grid(self):
        for row in range(self.num_rows):
            for column in range(self.num_columns):
                print(self.grid[row][column], end=" ")
            print("")

    def is_empty(self, row, column):
        return self.grid[row][column] == 0

    def is_inside(self, row, column):
        is_row_inside = row >= 0 and row < self.num_rows
        is_column_inside = column >= 0 and column < self.num_columns

        return is_row_inside and is_column_inside

    def is_row_full(self, row):
        for column in range(self.num_columns):
            if self.grid[row][column] == 0:
                return False
        return True

    def reset(self):
        self.grid = [[0 for j in range(self.num_columns)] for i in range(self.num_rows)]

    def clear_row(self, row):
        for column in range(self.num_columns):
            self.grid[row][column] = 0

    def move_rown_down(self, row, num_rows):
        for column in range(self.num_columns):
            self.grid[row + num_rows][column] = self.grid[row][column]
            self.grid[row][column] = 0

    def clear_full_rows(self):
        completed = 0
        for row in range(self.num_rows - 1, 0, -1):
            if self.is_row_full(row):
                self.clear_row(row)
                completed += 1
            elif completed > 0:
                self.move_rown_down(row, completed)
        return completed

    def draw(self, screen):
        for row in range(self.num_rows):
            for column in range(self.num_columns):
                cell_value = self.grid[row][column]
                cell_rect = pygame.Rect(
                    column * self.cell_size + 26,
                    row * self.cell_size + 26,
                    self.cell_size - 1,
                    self.cell_size - 1,
                )
                pygame.draw.rect(screen, self.colors[cell_value], cell_rect)
