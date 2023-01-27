import numpy as np

BOARD_SIZE = 19


class Board:
    def __init__(self):
        self.board = self.create_board(BOARD_SIZE)

    def create_board(self, board_size):
        board = np.zeros((board_size, board_size))
        return board
    
    def check_win(self, location):
        pass
