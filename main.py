from Board import Board

if __name__ == "__main__":
    board = Board()

    print("Game started: \n")
    board.print_state()
    print("\nLegal Moves: \n")
    board.get_legal_moves()
    while True:
        start = input("Piece to move: \n")
        end = input("Where to move: \n")
        if not board.make_move(start, end):
            print(f"\nInvalid move from {start} to {end}\n")
        board.print_state()
    # white_move = input("White move: ")
