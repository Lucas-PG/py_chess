from typing import TYPE_CHECKING

from .Piece import Piece

if TYPE_CHECKING:
    from Board import Board

DIRECTIONS = [
    (+2, +1), (+2, -1), (-2, +1), (-2, -1),
    (+1, +2), (+1, -2), (-1, +2), (-1, -2),
]


class Knight(Piece):
    def _compute_legal_moves(self, board: Board) -> list[str]:
        return self.get_legal_jumping_moves(board, DIRECTIONS)
