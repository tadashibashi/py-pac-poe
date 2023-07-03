from typing import List

class Board:
    board: List[int]
    rows: int
    cols: int

    def __init__(self, rows: int, cols: int, board: List[int] = None):
        if board is None:
            board = []
            for i in range(rows * cols):
                board.append(0)
            self.board = board
        else:
            if len(board) != rows * cols:
                print("[Board.__init__]: rows * cols must match provided list length!")
                raise ValueError
            self.board = board[:]

        self.rows = rows
        self.cols = cols

    def get(self, row: int, col: int) -> int:
        return self.board[row * self.cols + col]
    
    def set(self, row: int, col: int, val: int):
        self.board[row * self.cols + col] = val

    # copy to track state
    def copy(self):
        return Board(self.rows, self.cols, self.board)
