from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from Board import Board


class Piece:
    def __init__(self, color: str, row: int, col: int, code: str) -> None:
        self.color = color
        self.row = row
        self.col = col
        self.code = code
        self.legal_moves: list[tuple[int, int]] = []

    def move(self, board: Board, row: int, col: int) -> None:
        state = board.state
        state[self.row][self.col] = None
        self.row = row
        self.col = col
        state[self.row][self.col] = self

    def get_legal_moves(self, board: Board) -> list[str]:
        """Template method: resets state, delegates to subclass, returns notation list."""
        self.legal_moves = []
        return self._compute_legal_moves(board)

    def _compute_legal_moves(self, board: Board) -> list[str]:
        raise NotImplementedError

    def get_legal_sliding_moves(
        self, board: Board, directions: list[tuple[int, int]]
    ) -> list[str]:
        legal_moves: list[str] = []
        state = board.state

        for dr, dc in directions:
            next_row, next_col = self.row + dr, self.col + dc
            while 0 <= next_row <= 7 and 0 <= next_col <= 7:
                goal_square = state[next_row][next_col]
                goal_pos = board.get_square_name(next_row, next_col)

                if goal_square is None:
                    legal_moves.append(f"{self.code}{goal_pos}")
                    self.legal_moves.append((next_row, next_col))
                elif self.color != goal_square.color:
                    legal_moves.append(f"{self.code}x{goal_pos}")
                    self.legal_moves.append((next_row, next_col))
                    break
                else:
                    break

                next_row += dr
                next_col += dc

        return legal_moves

    def get_legal_jumping_moves(
        self, board: Board, directions: list[tuple[int, int]]
    ) -> list[str]:
        legal_moves: list[str] = []
        state = board.state

        for dr, dc in directions:
            next_row, next_col = self.row + dr, self.col + dc

            if not (0 <= next_row <= 7) or not (0 <= next_col <= 7):
                continue

            goal_square = state[next_row][next_col]
            goal_pos = board.get_square_name(next_row, next_col)

            if goal_square is None:
                legal_moves.append(f"{self.code}{goal_pos}")
                self.legal_moves.append((next_row, next_col))
            elif self.color != goal_square.color:
                legal_moves.append(f"{self.code}x{goal_pos}")
                self.legal_moves.append((next_row, next_col))

        return legal_moves
