import os
import sys
import time
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

def write(message: str):
    sys.stdout.write(message)

def flush():
    sys.stdout.flush()

def clear():
    # for Windows
    if os.name == "nt":
        os.system("cls")

    # for Linux / Mac OS
    else:
        os.system("clear")

def input_ex(message: str, caster: Callable[[str], Any], validator: Callable[[str], bool]):
    data = None

    while True:
        try:
            data = input(message)
            data = caster(data)

            if not validator(data):
                continue
            break
        except Exception:
            pass

    return data


class PyPacPoe(Game):
    board: GameBoard
    turn: int
    computer: bool
    state: State

    def _init(self) -> bool:
        clear()
        self.board = GameBoard()
        self.computer = True
        self.turn = SYM_X
        self.state = State.Select

        self._render_title()
        self._render_board()

        return True


    def reset(self):
        clear()
        self.board.clear()
        self.turn = SYM_X
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
        write("\n")
        write("How many players?\n")
        write("    '1' for player vs. computer\n")
        write("    '2' for player vs. player\n")
        players = input_ex("> ",
                 lambda d: int(d),
                 lambda d: d == 1 or d == 2)
        clear()

        if players == 1:
            self.computer = True

        self.state = State.Game


    def _get_player_move(self):
        move_str = input_ex("Choose your move (e.g. B3): ",
                            lambda s: s,
                            lambda s: (s[0].isalpha() and s[1:].isnumeric() and
                                      0 <= ord(s[0]) - ord('A') < self.board.cols and
                                      0 < int(s[1:]) <= self.board.rows) )
        return int(move_str[1:]) - 1, ord(move_str[0]) - ord('A')

    def _state_game(self):
        self._render_board()
        write("\n")
        write("Player " + ("O" if self.turn == SYM_O else "X") + "'s turn" +
              (" (computer)" if self.turn == SYM_O and self.computer else "") + "\n")

        if self.turn == SYM_O:
            if self.computer:
                if self.turn == SYM_O:
                    write("thinking")
                    flush()

                    for i in range(3):
                        time.sleep(.25)
                        write(". ")
                        flush()
                    time.sleep(1)
                    write("\n")
                    write("computer did turn!\n")
                else:
                    move = self._get_player_move()
                    self.board.set(move[0], move[1], self.turn)
        else:
            move = self._get_player_move()
            self.board.set(move[0], move[1], self.turn)

        if self.turn == SYM_O:
            self.turn = SYM_X
        else:
            self.turn = SYM_O

        clear()


    def _state_result(self):
        pass

    def _get_sym(self, row: int, col: int) -> str:
        return sym_to_str(self.board.get(row, col))

    # assumes board is not full
    def _get_computer_move(self):
        move = None

        # if player is going to win, block


        # if opportunity to win, try
            # find area with most connecting pieces with opportunity to win (no opponent pieces in row/col/diag)

        # else
            # place piece in first open area
        pass

    def _render_board(self):
        sym = self._get_sym
        write("   A   B   C\n")
        write("1) " + sym(0, 0) + " | " + sym(0, 1) + " | " + sym(0, 2) + "\n")
        write("  -----------\n")
        write("2) " + sym(1, 0) + " | " + sym(1, 1) + " | " + sym(1, 2) + "\n")
        write("  -----------\n")
        write("3) " + sym(2, 0) + " | " + sym(2, 1) + " | " + sym(2, 2) + "\n")

    @staticmethod
    def _render_title():
        write("----------------------\n")
        write("Let's play Py-Pac-Poe!\n")
        write("----------------------\n")

    def _render_exit(self):
        self._render_board()
        write("----------------------\n")
        write("  See you next time!\n")
        write("----------------------\n")


