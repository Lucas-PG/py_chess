from .Piece import Piece


class Knight(Piece):
    def get_legal_moves(self, board) -> list[str]:
        directions = [
            (+2, +1),
            (+2, -1),
            (-2, +1),
            (-2, -1),
            (+1, +2),
            (+1, -2),
            (-1, +2),
            (-1, -2),
        ]

        return super().get_legal_jumping_moves(board, directions)
