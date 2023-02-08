import numpy as np


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
        # 1 is black, 2 is white
        num_representation = 1 if ply % 2 == 0 else 2
        self.board[row][col] = num_representation
        print(self.board)
    