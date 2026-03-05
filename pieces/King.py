from .Piece import Piece


class King(Piece):
    def __init__(self, color, row, col, code):
        super().__init__(color, row, col, code)
        self.has_moved = False

    def move(self, board, row, col):
        super().move(board, row, col)
        self.has_moved = True

    def get_legal_moves(self, board) -> list[str]:
        directions = [
            (+1, +0),
            (-1, +0),
            (+0, +1),
            (+0, -1),
            (+1, +1),
            (+1, -1),
            (-1, +1),
            (-1, -1),
        ]

        return super().get_legal_jumping_moves(board, directions)
