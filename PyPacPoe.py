from typing import Any, Callable

from Game import Game
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

from enum import Enum

class State(Enum):
    Select=0
    Game=1
    Result=2

def input_ex(message: str, caster: Callable[[str], Any]):
    did_raise = True
    data = None

    while did_raise:
        try:
            data = input(message)
            data = caster(data)
            did_raise = False
        except Exception:
            did_raise = True

    return data


class PyPacPoe(Game):
    board: GameBoard
    turn: int
    computer: bool
    state: State

    def _init(self) -> bool:
        self.board = GameBoard()
        self.computer = True
        self.turn = SYM_O
        self.state = State.Select

        self._render_title()
        self._render()

        return True


    def reset(self):
        self.board.clear()
        self.turn = SYM_O
        self.state = State.Select

    def _loop(self):
        match self.state:
            case State.Select:
                self._state_select()
            case State.Game:
                self._state_game()
            case State.Result:
                self._state_result()
            case _:
                pass

    def _state_select(self):
        pass

    def _state_game(self):
        pass

    def _state_result(self):
        pass

    def _get_sym(self, row: int, col: int) -> str:
        return sym_to_str(self.board.get(row, col))

    def _render(self):
        sym = self._get_sym
        print("   A   B   C")
        print("1) " + sym(0, 0) + " | " + sym(0, 1) + " | " + sym(0, 2))
        print("  -----------")
        print("2) " + sym(1, 0) + " | " + sym(1, 1) + " | " + sym(1, 2))
        print("  -----------")
        print("3) " + sym(2, 0) + " | " + sym(2, 1) + " | " + sym(2, 2))

    @staticmethod
    def _render_title():
        print("----------------------")
        print("Let's play Py-Pac-Poe!")
        print("----------------------")
