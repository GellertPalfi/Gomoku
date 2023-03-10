import numpy as np

from Board import Board


class Aiplayer:
    def __init__(self) -> None:
        pass

    def evaluate(self, board: Board, enemy_player_value=2):
        for c in range(board.cols - 4):
            for r in range(board.rows):
                if np.all(board.board[r, c : c + 4] == enemy_player_value):
                    return -100

        for c in range(board.cols):
            for r in range(board.rows - 4):
                if np.all(board.board[r : r + 4, c] == enemy_player_value):
                    return -100

        # check for positively sloped diagonal wih
        for c in range(board.cols - 4):
            for r in range(4, board.rows):
                if (
                    board.board[r, c] == enemy_player_value
                    and board.board[r - 1, c + 1] == enemy_player_value
                    and board.board[r - 2, c + 2] == enemy_player_value
                    and board.board[r - 3, c + 3] == enemy_player_value
                ):
                    return (r - 4, c + 4)

        # check for negatively sloped diagonal win
        for c in range(board.cols - 4):
            for r in range(board.rows - 4):
                if (
                    board.board[r, c] == enemy_player_value
                    and board.board[r + 1, c + 1] == enemy_player_value
                    and board.board[r + 2, c + 2] == enemy_player_value
                    and board.board[r + 3, c + 3] == enemy_player_value
                ):
                    return (r + 4, c + 4)

        return (50, 50)

    def get_move(self):
        return (50, 50)
