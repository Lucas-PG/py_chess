from .Piece import Piece


class Queen(Piece):
    def get_legal_moves(self, board) -> list[str]:
        directions = [
            (+1, +1),
            (+1, -1),
            (-1, -1),
            (-1, +1),
            (+0, +1),
            (+1, +0),
            (+0, -1),
            (-1, +0),
        ]

        return super().get_legal_sliding_moves(board, directions)
