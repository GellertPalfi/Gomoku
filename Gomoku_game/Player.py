class Player:
    def __init__(self, color) -> None:
        self.color = color
        self.num_representation = 1 if self.color == "BLACK" else 0

    def drop_piece(self, board, row, col):
        board[row][col] = self.num_representation
        print(board)
