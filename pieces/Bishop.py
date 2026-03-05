from .Piece import Piece


class Bishop(Piece):
    def get_legal_moves(self, board) -> list[str]:
        directions = [
            (+1, +1),
            (+1, -1),
            (-1, -1),
            (-1, +1),
        ]

        return super().get_legal_sliding_moves(board, directions)
