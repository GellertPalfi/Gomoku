import itertools
import time

import pygame
from Aiplayer import Aiplayer
from Board import Board

ROWS = 19
COLS = 19
PADDING = 50


class Colors:
    BLACK = 0, 0, 0
    WHITE = 200, 200, 200
    ORANGE = 255, 127, 80
    BROWN = 205, 128, 0
    GREY = 150, 150, 150


class Gomoku:
    def __init__(self, size=50, piece_size=20) -> None:
        self.size = size
        self.cols = COLS
        self.rows = ROWS
        self.width = COLS * size
        self.height = ROWS * size
        self.board = Board(ROWS, COLS)
        self.ply = 0
        self.screen_size_vertical = self.height + PADDING
        self.screen_size_horizontal = self.width + PADDING
        self.piece_size = piece_size
        self.screen = pygame.display.set_mode(
            (self.screen_size_horizontal, self.screen_size_vertical)
        )
        # Black(1), White(2)
        self.last_player_value = 1
        self.Aiplayer = Aiplayer()
        self.last_move = None

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

        # switch x and y, because 2D array indexing takes in the row (y) coordinate first
        # then the column (x)
        if self.board.in_bounds(x, y) and self.board.is_empty(y, x):
            self.board.drop_piece(y, x, self.ply)
            self.last_move = (y, x)
            x = x * self.size + PADDING
            y = y * self.size + PADDING

            self.last_player_value = 1 if self.ply % 2 == 0 else 2
            color = Colors.BLACK if self.last_player_value == 1 else Colors.WHITE
            pygame.draw.circle(self.screen, color, (x, y), self.piece_size)

            self.ply += 1

    def draw_board(self):
        self.draw_background()
        self.draw_lines()

    def create_ending_textbox(self, text):
        my_font = pygame.font.Font("freesansbold.ttf", 32)
        text_surface = my_font.render(text, False, Colors.WHITE, Colors.BLACK)
        box_x = 300
        box_y = 400
        box_width = 400
        box_height = 150

        # greybox
        pygame.draw.rect(
            self.screen, Colors.GREY, (box_x, box_y, box_width, box_height)
        )
        # black outline
        pygame.draw.rect(
            self.screen,
            Colors.BLACK,
            (box_x + 2, box_y + 2, box_width - 4, box_height - 4),
            2,
        )

        horizontal_ofset = box_width / 3.5
        vertical_ofset = box_height / 4

        self.screen.blit(
            text_surface, (box_x + horizontal_ofset, box_y + vertical_ofset)
        )

    def restart(self):
        time.sleep(2)
        self.draw_board()
        self.board = Board(ROWS, COLS)
        self.ply = 0

    def play(self, aiplayer=None):
        running = True
        game_over = False
        self.draw_board()
        pygame.display.set_caption("Gomoku (Connect 5)")

        while running:
            pygame.display.update()

            if self.ply >= 9:
                someone_won = self.board.winner(self.last_move, self.last_player_value)
                if someone_won:
                    text = "Black Won" if self.ply % 2 == 1 else "White Won"
                    self.create_ending_textbox(text)
                    pygame.display.update()
                    game_over = True

            if self.ply == ROWS * COLS:
                self.create_ending_textbox("Draw")
                pygame.display.update()
                game_over = True

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.display.quit()

                if aiplayer:
                    if self.ply % 2 == 1:
                        move = aiplayer.move(self.board)
                        self.draw_piece(*move)

                if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                    pos = pygame.mouse.get_pos()
                    print(pos)
                    self.draw_piece(*pos)

            if game_over:
                self.restart()
                game_over = False
