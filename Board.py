from pieces import Bishop, King, Knight, Pawn, Queen, Rook
from pieces.Piece import Piece

# https://www.chess.com/terms/fen-chess
INITIAL_FEN = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR"

PIECE_TYPES: dict[str, type[Piece]] = {
    "k": King,
    "q": Queen,
    "r": Rook,
    "b": Bishop,
    "n": Knight,
    "p": Pawn,
}

COLS = "abcdefgh"

PIECE_VALUES: dict[type[Piece], int] = {
    King: 0,
    Queen: 9,
    Rook: 5,
    Bishop: 3,
    Knight: 3,
    Pawn: 1,
}


class Board:
    def __init__(self) -> None:
        self.state: list[list[Piece | None]] = [[None] * 8 for _ in range(8)]
        self.turn = 0  # 0 = white, 1 = black
        self.pieces: list[Piece] = []

        for row_idx, row in enumerate(reversed(INITIAL_FEN.split("/"))):
            col_idx = 0
            for char in row:
                if char.isdigit():
                    col_idx += int(char)
                else:
                    color = "white" if char.isupper() else "black"

                    piece_type = PIECE_TYPES[char.lower()]
                    value = PIECE_VALUES[piece_type]

                    piece = piece_type(color, row_idx, col_idx, char, value)
                    self.pieces.append(piece)
                    self.state[row_idx][col_idx] = piece
                    col_idx += 1

        self.get_current_score()

    def get_square_name(self, row: int, col: int) -> str:
        return f"{COLS[col]}{row + 1}"

    def get_all_legal_moves(self) -> list[str]:
        return [move for piece in self.pieces for move in piece.get_legal_moves(self)]

    def make_move(self, start: str, end: str) -> bool:
        start_col = ord(start[0]) - ord("a")
        start_row = int(start[1]) - 1
        piece = self.state[start_row][start_col]

        if piece is None:
            return False

        if (piece.color == "white") != (self.turn == 0):
            print("Not your turn!")
            return False

        piece.get_legal_moves(self)

        end_col = ord(end[0]) - ord("a")
        end_row = int(end[1]) - 1

        if (end_row, end_col) not in piece.legal_moves:
            print("Not allowed!")
            return False

        target = self.state[end_row][end_col]
        if target is not None:
            if target.color != piece.color:
                self.pieces.remove(target)
            else:
                return False

        piece.move(self, end_row, end_col)
        self.turn = 1 - self.turn
        return True

    def get_current_score(self):
        white_score = black_score = 0
        for piece in self.pieces:
            if piece.color == "white":
                white_score += piece.value
            else:
                black_score += piece.value

        return (white_score, black_score)


    def print_score(self) -> None:
        white_score, black_score = self.get_current_score()

        print("Current Score: \n")
        print(f"\tWhite: {white_score}")
        print(f"\tBlack: {black_score}")

    def print_state(self) -> None:
        print("\n\t  +---+---+---+---+---+---+---+---+")
        for rank in range(7, -1, -1):
            row = self.state[rank]
            cells = " | ".join(piece.code if piece else " " for piece in row)
            print(f"\t{rank + 1} | {cells} |")
            print("\t  +---+---+---+---+---+---+---+---+")
        print("\t    a   b   c   d   e   f   g   h")
