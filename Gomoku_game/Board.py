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
        player_value = 1 if ply % 2 == 0 else 2
        self.board[row][col] = player_value
        print(self.board)

    def winning_move(self, position, player_value):
        row, col = position
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

        row_start = max(row - 4, 0)
        row_end = min(row + 4, self.rows - 4)
        col_start = max(col - 4, 0)
        col_end = min(col + 4, self.cols - 4)
        subboard = self.board[row_start : row_end + 1, col_start : col_end + 1]
        
        for kernel in detection_kernels:
            # Check if the kernel matches around the last move
            if (convolve2d(subboard == player_value, kernel) == 5).any():
                return True
        return False

    def winner(self, position, player_value):
        return self.winning_move(position, player_value)

    def get_board(self):
        return self.board

    def get_value(self, position):
        row, col = position
        return int(self.board[row][col])

    def copy(self):
        new_board = Board(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                new_board.board[i][j] = self.board[i][j]
        return new_board
