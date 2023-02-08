import numpy as np

BOARD_SIZE = 19


class Board:
    def __init__(self):
        self.board = self.create_board(BOARD_SIZE)

    def create_board(self, board_size):
        board = np.zeros((board_size, board_size))
        return board

    def in_bounds(self, y, x):
        return y >= 0 and y < BOARD_SIZE and x >= 0 and x < BOARD_SIZE

    def is_empty(self, row, col):
        return self.board[row][col] == 0

