from Board import Board

if __name__ == "__main__":
    board = Board()

    print("Game started:\n")
    board.print_state()
    print("\nLegal Moves:\n")
    print(board.get_all_legal_moves())

    while True:
        start = input("\nPiece to move: ")
        end = input("Where to move: ")
        if board.make_move(start, end):
            board.print_score()
            board.print_state()
        else:
            print(f"Invalid move from {start} to {end}")
