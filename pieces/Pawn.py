from typing import TYPE_CHECKING

from .Piece import Piece

if TYPE_CHECKING:
    from Board import Board


class Pawn(Piece):
    def __init__(self, color: str, row: int, col: int, code: str, value: int) -> None:
        super().__init__(color, row, col, code, value)
        self.has_moved = False

    def move(self, board: Board, row: int, col: int) -> None:
        super().move(board, row, col)
        self.has_moved = True

    def _compute_legal_moves(self, board: Board) -> list[str]:
        direction = +1 if self.color == "white" else -1
        take_directions = [(direction, +1), (direction, -1)]

        legal_moves: list[str] = []
        state = board.state
        next_row = self.row + direction

        if not (0 <= next_row <= 7):
            return legal_moves

        # Forward one square
        if state[next_row][self.col] is None:
            legal_moves.append(board.get_square_name(next_row, self.col))
            self.legal_moves.append((next_row, self.col))

            # Forward two squares on first move
            if not self.has_moved:
                next_row_two = next_row + direction
                if 0 <= next_row_two <= 7 and state[next_row_two][self.col] is None:
                    legal_moves.append(board.get_square_name(next_row_two, self.col))
                    self.legal_moves.append((next_row_two, self.col))

        # Diagonal captures
        for dr, dc in take_directions:
            cap_row, cap_col = self.row + dr, self.col + dc

            if not (0 <= cap_row <= 7) or not (0 <= cap_col <= 7):
                continue

            target = state[cap_row][cap_col]
            if target is not None and target.color != self.color:
                legal_moves.append(f"x{board.get_square_name(cap_row, cap_col)}")
                self.legal_moves.append((cap_row, cap_col))

        return legal_moves
