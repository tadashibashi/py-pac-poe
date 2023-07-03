from typing import Tuple

from Board import Board

_ROWS = 3
_COLS = 3
_NULL = 0

class GameBoard(Board):
    def __init__(self, board=None):
        super().__init__(_ROWS, _COLS, board)

    def is_full(self):
        for row in range(self.rows):
            for col in range(self.cols):
                if self.get(row, col) == _NULL:
                    return False
        return True

    def check_win(self, symbol: int) -> bool:
        """
        Check the board for a winning combination for symbol.
        :param symbol: the symbol to check.
        :return: whether winning combo exists.
        """
        # check rows
        for row in range(self.rows):
            won = True
            for col in range(self.cols):
                if self.get(row, col) != symbol:
                    won = False
                    break
            
            if won:
                return True
        
        # check cols
        for col in range(self.cols):
            won = True
            for row in range(self.rows):
                if self.get(row, col) != symbol:
                    won = False
                    break
            
            if won:
                return True
        
        # check diagonal (must be square grid)
        if self.cols != self.rows:
            return False

        # top-left to bottom-right
        won = True
        for i in range(self.rows):
            if self.get(i, i) != symbol:
                won = False
                break
        
        if won:
            return True

        # bottom-left to top-right
        won = True
        for i in range(self.rows):
            if self.get(self.rows-1-i, i) != symbol:
                won = False
                break
        
        return won


    def rate_cell(self, row: int, col: int, sym: int) -> int:
        """
        Gets the rating for a given cell position representing most optimal next play position.
        Does not take into account blocking an opponent, make sure to check for this
        before using this function, or compare opponent sym's optimal position to this sym's
        Assumes a valid row and column was given.
        Safe to call if cell is occupied–it will efficiently return 0.
        :param row: row to check
        :param col: column to check
        :param sym: symbol to check with
        :return: rating for placement at cell. Higher means greater optimization.
        Compare with other cells for optimal play.
        """
        if self.get(row, col) != 0: return 0

        rating = 0

        # check row
        temp = 0
        for i in range(self.cols):
            cur = sym if i == col else self.get(row, i)

            if cur == sym:  # own piece, increase viability
                temp = (temp + 1) * self.cols
            elif cur != 0:  # opposing piece, bad row
                temp = 0
                break
        rating += temp

        # check col
        temp = 0
        for i in range(self.rows):
            cur = sym if i == row else self.get(i, col)

            if cur == sym:  # own piece, increase viability
                temp = (temp + 1) * self.rows
            elif cur != 0:  # opposing piece, bad row
                temp = 0
                break
        rating += temp

        # check diags

        # done if board not a square
        if self.rows != self.cols: return rating

        # check if in diag top-left, bottom-right
        if row == col:
            temp = 0
            for i in range(self.rows):
                cur = sym if (i == row) else self.get(i, i)

                if cur == sym:
                    temp = (temp + 1) * self.rows
                elif cur != 0:
                    temp = 0
                    break
            rating += temp

        # check if in diag bottom-left, top-right
        if self.rows-1-row == col:
            temp = 0
            for i in range(self.rows):
                cur_row = self.rows-1-i
                cur = sym if (cur_row == row and i == col) else self.get(cur_row, i)

                if cur == sym:
                    temp = (temp + 1) * self.rows
                elif cur != 0:
                    temp = 0
                    break
            rating += temp

        return rating




    def will_win(self, sym: int) -> Tuple[int, int] or None:
        if sym == 0: return None  # sym must be a player symbol


        # check rows
        for row in range(self.rows):
            rating = 0
            temp_pos = None
            for col in range(self.cols):
                current_sym = self.get(row, col)
                if current_sym == 0:
                    temp_pos = (row, col)
                elif current_sym == sym:
                    rating += 1

            if rating == 2 and temp_pos is not None:
                return temp_pos

        # check cols
        for col in range(self.cols):
            rating = 0
            temp_pos = None
            for row in range(self.rows):
                current_sym = self.get(row, col)
                if current_sym == 0:
                    temp_pos = (row, col)
                elif current_sym == sym:
                    rating += 1

                if rating == 2 and temp_pos is not None:
                    return temp_pos

        # check diagonals

        if self.rows != self.cols: # must be square...
            return None

        # top-left to bottom-right
        rating = 0
        temp_pos = None
        for i in range(self.rows):
            current_sym = self.get(i, i)
            if current_sym == 0:
                temp_pos = (i, i)
            else:
                rating += 1

            if rating == 2 and temp_pos is not None:
                return temp_pos

        # bottom-left to top-right
        rating = 0
        temp_pos = None
        for i in range(self.rows):
            current_sym = self.get(self.rows-1-i, i)
            if current_sym == 0:
                temp_pos = (self.rows-1-i, i)
            else:
                rating += 1

            if rating == 2 and temp_pos is not None:
                return temp_pos

        return None
