import unittest
from GameBoard import GameBoard

class TestGameBoard(unittest.TestCase):
    def test_win_col0(self):
        board = GameBoard([1, 0, 0,
                           1, 0, 0,
                           1, 0, 0])

        self.assertTrue(board.check_win(1))

    def test_win_col1(self):
        board = GameBoard([0, 1, 0,
                           0, 1, 0,
                           0, 1, 0])

        self.assertTrue(board.check_win(1))

    def test_win_col2(self):
        board = GameBoard([0, 0, 1,
                           0, 0, 1,
                           0, 0, 1])

        self.assertTrue(board.check_win(1))

    def test_win_row0(self):
        board = GameBoard([1, 1, 1,
                           0, 0, 0,
                           0, 0, 0])

        self.assertTrue(board.check_win(1))

    def test_win_row1(self):
        board = GameBoard([0, 0, 0,
                           1, 1, 1,
                           0, 0, 0])

        self.assertTrue(board.check_win(1))

    def test_win_row2(self):
        board = GameBoard([0, 0, 0,
                           0, 0, 0,
                           1, 1, 1])

        self.assertTrue(board.check_win(1))

    def test_win_cross0(self):
        board = GameBoard([1, 0, 0,
                           0, 1, 0,
                           0, 0, 1])

        self.assertTrue(board.check_win(1))

    def test_win_cross1(self):
        board = GameBoard([0, 0, 1,
                           0, 1, 0,
                           1, 0, 0])

        self.assertTrue(board.check_win(1))

