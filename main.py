from GameBoard import GameBoard

# Constants
SYM_NONE: int = 0
SYM_X: int = 1
SYM_O: int = 2

turn: int = SYM_O

board = GameBoard()

def sym_to_str(val: int):
    if val == SYM_X:
        return "X"
    elif val == SYM_O:
        return "O"
    else:
        return " "

def get_sym(row: int, col: int) -> str:
    return sym_to_str(board.get(row, col))

def reset():
    board.clear()

def loop():

    pass

def render():
    print("   A   B   C")
    print("1) " + get_sym(0, 0) + " | " + get_sym(0, 1) + " | " + get_sym(0, 2))
    print("  -----------")
    print("2) " + get_sym(1, 0) + " | " + get_sym(1, 1) + " | " + get_sym(1, 2))
    print("  -----------")
    print("3) " + get_sym(2, 0) + " | " + get_sym(2, 1) + " | " + get_sym(2, 2))

def main():
    print("----------------------")
    print("Let's play Py-Pac-Poe!")
    print("----------------------")

    render()



if __name__ == "__main__":
    main()
