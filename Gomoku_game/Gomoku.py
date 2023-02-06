import itertools

import pygame

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

    def drop_piece(self, position):
        pygame.draw.circle(self.screen, Colors.BLACK, position, self.piece_size)

    def draw_board(self):
        self.draw_background()
        self.draw_lines()

    def play(self):
        running = True
        self.draw_board()
        while running:
            # Did the user click the window close button?
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    self.drop_piece(pos)
                if event.type == pygame.QUIT:
                    running = False

            pygame.display.update()
