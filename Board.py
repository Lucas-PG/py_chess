from pieces import King
from pieces import Queen
from pieces import Rook
from pieces import Bishop
from pieces import Knight
from pieces import Pawn

INITIAL_FEN = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR"
piece_types = {"k": King, "q": Queen, "r": Rook, "b": Bishop, "n": Knight, "p": Pawn}


class Board:
    def __init__(self):
        self.state = [[None] * 8 for _ in range(8)]
        self.turn = 0  # white
        self.pieces = []
        self.legal_moves = []

        rows = INITIAL_FEN.split("/")

        for row_idx, row in enumerate(reversed(rows)):
            col_idx = 0
            for char in row:
                if char.isdigit():
                    col_idx += int(char)
                else:
                    color = "white" if char.isupper() else "black"
                    piece = piece_types[char.lower()](color, row_idx, col_idx, char)
                    self.pieces.append(piece)
                    self.state[row_idx][col_idx] = piece
                    col_idx += 1

    def get_state(self):
        return self.state

    def update_state(self, state):
        self.state = state

    def get_legal_moves(self):
        for piece in self.pieces:
            moves = piece.get_legal_moves(self)
            if moves is None:
                continue

            for move in moves:
                self.legal_moves.append(move)

        print(self.legal_moves)

    def make_move(self, start, end):
        start_col = ord(start[0]) - ord("a")
        start_row = int(start[1]) - 1
        piece = self.state[start_row][start_col]

        if piece is None:
            return False

        if piece.color == "white" != self.turn == 1:
            print("Not your turn!")
            return False

        end_col = ord(end[0]) - ord("a")
        end_row = int(end[1]) - 1

        goal = self.state[end_row][end_col]
        if (end_row, end_col) not in piece.legal_moves:
            print("Not allowed!")
            return False

        if goal is not None:
            if goal.color != piece.color:
                # Take
                self.pieces.remove(goal)
            else:
                return False

        piece.move(self, end_row, end_col)
        self.turn = 1 - self.turn
        return True

    def get_square_name(self, row: int, col: int) -> str:
        return f"{'abcdefgh'[col]}{row + 1}"

    def print_state(self):
        for row in reversed(self.state):
                print([col.code if col is not None else " " for col in row])
