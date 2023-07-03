import os
import sys
import time
from typing import Any, Callable, Tuple

import math

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

        self.computer = players == 1

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
                write("thinking")
                flush()

                c_move = self._get_computer_move()
                self.board.set(c_move[0], c_move[1], SYM_O)

                for i in range(3):
                    time.sleep(.15)
                    write(". ")
                    flush()
                time.sleep(.5)
                write("\n")
            else:
                while True:
                    move = self._get_player_move()
                    if self.board.get(move[0], move[1]) == 0:
                        break
                    write("There is already a piece there!\n")

                self.board.set(move[0], move[1], self.turn)
        else:
            while True:
                move = self._get_player_move()

                if self.board.get(move[0], move[1]) == 0:
                    break
                write("There is already a piece there!\n")

            self.board.set(move[0], move[1], self.turn)

        self.turn = SYM_O if self.turn == SYM_X else SYM_X
        clear()
        self._process_win()


    def _get_sym_str_at(self, row: int, col: int) -> str:
        return sym_to_str(self.board.get(row, col))

    @staticmethod
    def _get_optimal(board: GameBoard, sym: int) -> Tuple[Tuple[int, int], float]:
        """
        Gets the next best move for a particular player
        :param board: the board to check
        :param sym: the symbol of the player
        :return: tuple with the next best move at [0], and rating at [1]
        """
        highest = -math.inf
        position = None
        for row in range(board.rows):
            for col in range(board.cols):
                rating = board.rate_cell(row, col, sym)
                if rating > highest:
                    position = (row, col)
                    highest = rating
        return position, highest

    # assumes board is not full
    def _get_computer_move(self, p_sym=SYM_X, c_sym=SYM_O) -> Tuple[int, int]:
        """
        Gets the computer's next move.
        Compares against player's next move. Selects the highest rated position.
        """
        # get optimal positions
        player_move = self._get_optimal(self.board, p_sym)
        comp_move = self._get_optimal(self.board, c_sym)

        return comp_move[0] if comp_move[1] >= player_move[1] else player_move[0]

    def _process_win(self):
        end_game = False
        winner = None

        if self.board.check_win(SYM_X):
            end_game = True
            winner = SYM_X
        elif self.board.check_win(SYM_O):
            end_game = True
            winner = SYM_O
        elif self.board.is_full():
            end_game = True
            winner = SYM_NONE

        if end_game:
            self._render_board()
            write("----------------------\n")
            if winner == SYM_NONE:
                write("It's a cats game!\n")
            else:
                write("Player " + ("X" if winner == SYM_X else "O") + " is the winner!\n")
            write("----------------------\n")
            write("\n")
            flush()
            response = input_ex("Play again? y=yes, n=no: > ",
                     lambda s: s,
                     lambda s: s.lower() == "n" or s.lower() == "y")
            clear()

            if response.lower() == "y":
                self.reset()
            else:
                self._render_exit()
                self.quit()



    def _render_board(self):
        sym = self._get_sym_str_at
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


