import time

import numpy as np
from scipy.signal import convolve2d


class Board:
    def __init__(self, rows=19, cols=19):
        self.rows = rows
        self.cols = cols
        self.board = self.create_board(self.rows, self.cols)

    def create_board(self, rows, cols):
        board = np.zeros((rows, cols))
        return board

    def in_bounds(self, y, x):
        return y >= 0 and y < self.rows and x >= 0 and x < self.cols

    def is_empty(self, row, col):
        return self.board[row][col] == 0

    def drop_piece(self, row, col, ply):
        num_representation = 1 if ply % 2 == 0 else 2
        self.board[row][col] = num_representation
        print(self.board)

    def winning_move(self, position):
        player_value = self.get_value(position)
        horizontal_kernel = np.array([[1, 1, 1, 1, 1]])
        vertical_kernel = np.transpose(horizontal_kernel)
        diag1_kernel = np.eye(5, dtype=np.uint8)
        diag2_kernel = np.fliplr(diag1_kernel)
        detection_kernels = [
            horizontal_kernel,
            vertical_kernel,
            diag1_kernel,
            diag2_kernel,
        ]

        for kernel in detection_kernels:
            if (
                convolve2d(self.board == player_value, kernel, mode="valid") == 5
            ).any():
                return True
        return False

    def check_win(self, position):
        return self.winning_move(position)

    def get_board(self):
        return self.board

    def get_value(self, position):
        row, col = position
        return int(self.board[row][col])
