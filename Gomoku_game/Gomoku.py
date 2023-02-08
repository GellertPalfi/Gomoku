import itertools

import pygame
from Board import Board

ROWS = 19
COLS = 19
PADDING = 50


class Colors:
    BLACK = 0, 0, 0
    WHITE = 200, 200, 200
    ORANGE = 255, 127, 80
    BROWN = 205, 128, 0


class Gomoku:
    def __init__(self, size=50, piece_size=20) -> None:
        self.size = size
        self.cols = COLS
        self.rows = ROWS
        self.width = COLS * size
        self.height = ROWS * size
        self.board = Board()
        self.last_player_move = "BLACK"
        self.screen_size_vertical = self.height + PADDING
        self.screen_size_horizontal = self.width + PADDING
        self.piece_size = piece_size
        self.screen = pygame.display.set_mode(
            (self.screen_size_horizontal, self.screen_size_vertical)
        )

    def draw_background(self):
        rect = pygame.Rect(0, 0, self.screen_size_horizontal, self.screen_size_vertical)
        pygame.draw.rect(self.screen, Colors.BROWN, rect)

    # offset lines by 1 so they dont start at the edge of the screen
    def vertical_lines(self):
        for i in range(1, self.cols + 1):
            yield (i * self.size, PADDING), (i * self.size, self.width)

    def horizontal_lines(self):
        for i in range(1, self.rows + 1):
            yield (PADDING, i * self.size), (self.width, i * self.size)

    def draw_lines(self):
        lines = itertools.chain(self.vertical_lines(), self.horizontal_lines())

        for start, end in lines:
            pygame.draw.line(self.screen, Colors.BLACK, start, end, width=2)

    def draw_piece(self, x, y):
        half = self.size // 2
        # by adding half to the x,y  coordinates we ensure that they
        # "snap" into position, so you can click anywhere in a cell
        # and it places the piece on the closest edge
        # -1 is used because of array indexing starting at 0
        x = (x + half) // self.size - 1
        y = (y + half) // self.size - 1

        if self.board.in_bounds(x, y) and self.board.is_empty(x, y):
            # switch x and y, because 2D array indexing takes in the row (y) coordinate first
            # then the column (x)
            self.board.drop_piece(y, x)
            x = x * self.size + PADDING
            y = y * self.size + PADDING

            pygame.draw.circle(self.screen, Colors.BLACK, (x, y), self.piece_size)

    def draw_board(self):
        self.draw_background()
        self.draw_lines()

    def play(self):
        running = True
        self.draw_board()
        pygame.display.set_caption("Gomoku (Connet 5)")

        while running:
            # Did the user click the window close button?
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    self.draw_piece(*pos)
                if event.type == pygame.QUIT:
                    running = False

            pygame.display.update()
