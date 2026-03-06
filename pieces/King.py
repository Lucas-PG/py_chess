from typing import TYPE_CHECKING

from .Piece import Piece

if TYPE_CHECKING:
    from Board import Board

DIRECTIONS = [
    (+1, +0), (-1, +0), (+0, +1), (+0, -1),
    (+1, +1), (+1, -1), (-1, +1), (-1, -1),
]


class King(Piece):
    def __init__(self, color: str, row: int, col: int, code: str, value: int) -> None:
        super().__init__(color, row, col, code, value)
        self.has_moved = False

    def move(self, board: Board, row: int, col: int) -> None:
        super().move(board, row, col)
        self.has_moved = True

    def _compute_legal_moves(self, board: Board) -> list[str]:
        return self.get_legal_jumping_moves(board, DIRECTIONS)
