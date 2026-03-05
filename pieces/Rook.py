from typing import TYPE_CHECKING

from .Piece import Piece

if TYPE_CHECKING:
    from Board import Board

DIRECTIONS = [(+0, +1), (+0, -1), (+1, +0), (-1, +0)]


class Rook(Piece):
    def _compute_legal_moves(self, board: Board) -> list[str]:
        return self.get_legal_sliding_moves(board, DIRECTIONS)
