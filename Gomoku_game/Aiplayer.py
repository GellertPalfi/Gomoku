class Aiplayer:
    def move(self, board, player=2):
    # Create a list of all the possible moves on the board
        moves = []
        for i in range(board.rows):
            for j in range(board.cols):
                if board.is_empty(i, j):
                    moves.append((i, j))

        # Evaluate each possible move and choose the best one
        best_move = None
        best_score = -float('inf')
        for move in moves:
            score = self.evaluate_move(board, move, player)
            if score > best_score:
                best_move = move
                best_score = score

        return best_move


    def evaluate_move(self, board, move, player=2):
        # Make a copy of the board and apply the move
        new_board = board.copy()
        new_board.drop_piece(move[0], move[1], player)

        # Check if the move results in a win for the player
        if new_board.winning_move(move, 1):
            return float('inf')

        # Check if the move results in a loss for the opponent
        opponent = 1 if player == 2 else 2
        if new_board.winning_move(move, opponent):
            return -float('inf')

        # Otherwise, evaluate the move based on how many potential lines it creates for the player
        score = 0
        for i in range(new_board.rows):
            for j in range(new_board.cols):
                if new_board.is_empty(i, j):
                    if new_board.has_potential_line(i, j, player):
                        score += 1

        return score
