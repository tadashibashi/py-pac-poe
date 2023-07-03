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


