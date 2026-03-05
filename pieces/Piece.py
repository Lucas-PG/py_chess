class Piece:
    def __init__(self, color, row, col, code):
        self.color = color
        self.row = row
        self.col = col
        self.code = code
        self.directions = None
        self.legal_moves = []

    def move(self, board, row, col):
        state = board.state
        state[self.row][self.col] = None
        self.row = row
        self.col = col
        state[self.row][self.col] = self

    def get_legal_moves(self, board):
        raise NotImplementedError

    def get_legal_sliding_moves(self, board, directions: list[tuple[int, int]]):
        legal_moves = []
        state = board.state

        for dr, dc in directions:
            next_row, next_col = self.row + dr, self.col + dc
            while 0 <= next_row <= 7 and 0 <= next_col <= 7:
                goal_square = state[next_row][next_col]
                goal_pos = board.get_square_name(next_row, next_col)

                if goal_square is None:
                    legal_moves.append(f"{self.code}{goal_pos}")
                elif self.color != goal_square.color:
                    # Opponent piece
                    legal_moves.append(f"{self.code}x{goal_pos}")
                    break
                else:
                    break

                next_row += dr
                next_col += dc

        return legal_moves

    def get_legal_jumping_moves(self, board, directions: list[tuple[int, int]]):
        legal_moves = []
        state = board.state

        for dr, dc in directions:
            next_row, next_col = self.row + dr, self.col + dc

            # Check board bounds
            if not (0 <= next_row <= 7) or not (0 <= next_col <= 7):
                continue

            goal_square = state[next_row][next_col]
            goal_pos = board.get_square_name(next_row, next_col)

            if goal_square is None:
                legal_moves.append(f"{self.code}{goal_pos}")
            elif self.color != goal_square.color:
                # Opponent piece
                legal_moves.append(f"{self.code}x{goal_pos}")

        return legal_moves
