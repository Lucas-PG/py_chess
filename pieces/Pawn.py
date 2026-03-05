from .Piece import Piece


class Pawn(Piece):
    def __init__(self, color, row, col, code):
        super().__init__(color, row, col, code)
        self.has_moved = False

    def move(self, board, row, col):
        super().move(board, row, col)
        self.has_moved = True

    def get_legal_moves(self, board):
        if self.color == "white":
            directions = (+1, +0)
            take_directions = [(+1, +1), (+1, -1)]
        else:
            directions = (-1, 0)
            take_directions = [(-1, +1), (-1, -1)]

        legal_moves = []
        next_row = self.row + directions[0]
        state = board.state

        if not (0 <= next_row <= 7):
            return legal_moves

        if state[next_row][self.col] is None:
            legal_moves.append(board.get_square_name(next_row, self.col))
            self.legal_moves.append((next_row, self.col))

            # If its the first move, allow to jump 2 rows
            if not self.has_moved:
                next_row_two = next_row + directions[0]
                if state[next_row_two][self.col] is None:
                    legal_moves.append(board.get_square_name(next_row_two, self.col))
                    self.legal_moves.append((next_row_two, self.col))

        for direction in take_directions:
            next_row = self.row + direction[0]
            next_col = self.col + direction[1]

            if not (0 <= next_row <= 7) or not (0 <= next_col <= 7):
                continue

            goal_square = state[next_row][next_col]
            goal_pos = board.get_square_name(next_row, next_col)

            if goal_square is None:
                continue
            elif self.color != goal_square.color:
                # Opponent piece
                legal_moves.append(f"x{goal_pos}")
                self.legal_moves.append((next_row, next_col))

        return legal_moves
