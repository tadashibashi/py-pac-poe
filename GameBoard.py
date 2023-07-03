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
