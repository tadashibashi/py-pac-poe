from GameBoard import GameBoard

# Constants
SYM_NONE: int = 0
SYM_X: int = 1
SYM_O: int = 2

def sym_to_str(val: int):
    if val == SYM_X:
        return "X"
    elif val == SYM_O:
        return "O"
    else:
        return " "


class PyPacPoe:
    board: GameBoard
    turn: int
    computer: bool

    def __init__(self):
        self.board = GameBoard()
        self.computer = True
        self.turn = SYM_O

        self.render_title()
        self.render()


    def reset(self):
        self.board.clear()
        self.turn = SYM_O

    def loop(self):
        pass

    def _get_sym(self, row: int, col: int) -> str:
        return sym_to_str(self.board.get(row, col))

    def render(self):
        get_sym = self._get_sym
        print("   A   B   C")
        print("1) " + get_sym(0, 0) + " | " + get_sym(0, 1) + " | " + get_sym(0, 2))
        print("  -----------")
        print("2) " + get_sym(1, 0) + " | " + get_sym(1, 1) + " | " + get_sym(1, 2))
        print("  -----------")
        print("3) " + get_sym(2, 0) + " | " + get_sym(2, 1) + " | " + get_sym(2, 2))

    @staticmethod
    def render_title():
        print("----------------------")
        print("Let's play Py-Pac-Poe!")
        print("----------------------")