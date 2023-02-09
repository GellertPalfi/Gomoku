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
        num_representation = 1 if ply % 2 == 0 else 2
        self.board[row][col] = num_representation
        print(self.board)
    
    def check_win(self, last_player_value):
        # check for horizontal win
        for c in range(self.cols - 4):
            for r in range(self.rows):
                if np.all(self.board[r, c:c+5] == last_player_value):
                    return True

        # check for vertical win
        for c in range(self.cols):
            for r in range(self.rows - 4):
                if np.all(self.board[r:r+5, c] == last_player_value):
                    return True

        # check for positively sloped diagonal wih
        for c in range(self.cols - 4):
            for r in range(4, self.rows):
                if (
                    self.board[r, c] == last_player_value
                    and self.board[r-1, c+1] == last_player_value
                    and self.board[r-2, c+2] == last_player_value
                    and self.board[r-3, c+3] == last_player_value
                    and self.board[r-4, c+4] == last_player_value
                ):
                    return True

        # check for negatively sloped diagonal win
        for c in range(self.cols - 4):
            for r in range(self.rows - 4):
                if (
                    self.board[r, c] == last_player_value
                    and self.board[r+1, c+1] == last_player_value
                    and self.board[r+2, c+2] == last_player_value
                    and self.board[r+3, c+3] == last_player_value
                    and self.board[r+4, c+4] == last_player_value
                ):
                    return True

        return False