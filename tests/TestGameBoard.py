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

    def test_will_win_zero_ignored(self):
        board = GameBoard([0, 0, 0,
                           0, 0, 0,
                           0, 0, 0])
        self.assertEqual(board.will_win(0), None)
    def test_will_win_row0(self):
        board = GameBoard([1, 1, 0,
                           0, 0, 0,
                           0, 0, 0])
        self.assertEqual(board.will_win(1), (0, 2))
    def test_will_win_row0_win(self):
        board = GameBoard([1, 1, 1,
                           0, 0, 0,
                           0, 0, 0])
        self.assertEqual(board.will_win(1), None)

    def test_will_win_row0_blocking(self):
        board = GameBoard([1, 1, 2,
                           0, 0, 0,
                           0, 0, 0])
        self.assertEqual(board.will_win(1), None)

    def test_will_win_row1(self):
        board = GameBoard([0, 0, 0,
                           1, 0, 1,
                           0, 0, 0])
        self.assertEqual(board.will_win(1), (1, 1))

    def test_will_win_row1_win(self):
        board = GameBoard([0, 0, 0,
                           1, 1, 1,
                           0, 0, 0])
        self.assertEqual(board.will_win(1), None)

    def test_will_win_row1_blocking(self):
        board = GameBoard([0, 0, 0,
                           1, 3, 1,
                           0, 0, 0])
        self.assertEqual(board.will_win(1), None)
        self.assertEqual(board.will_win(3), None)

    def test_will_win_row2(self):
        board = GameBoard([0, 0, 0,
                           0, 0, 0,
                           0, 1, 1])
        self.assertEqual(board.will_win(1), (2, 0))

    def test_will_win_row2_win(self):
        board = GameBoard([0, 0, 0,
                           0, 0, 0,
                           1, 1, 1])
        self.assertEqual(board.will_win(1), None)

    def test_will_win_row2_blocking(self):
        board = GameBoard([0, 0, 0,
                           0, 0, 0,
                           2, 1, 1])
        self.assertEqual(board.will_win(1), None)
        self.assertEqual(board.will_win(2), None)

    def test_will_win_col0(self):
        board = GameBoard([1, 0, 0,
                           0, 0, 0,
                           1, 0, 0])
        self.assertEqual(board.will_win(1), (1, 0))

    def test_will_win_col0_win(self):
        board = GameBoard([1, 0, 0,
                           1, 0, 0,
                           1, 0, 0])
        self.assertEqual(board.will_win(1), None)

    def test_will_win_col0_blocking(self):
        board = GameBoard([1, 0, 0,
                           2, 0, 0,
                           1, 0, 0])
        self.assertEqual(board.will_win(1), None)
        self.assertEqual(board.will_win(2), None)

    def test_will_win_col1(self):
        board = GameBoard([0, 1, 0,
                           0, 1, 0,
                           0, 0, 0])
        self.assertEqual(board.will_win(1), (2, 1))

    def test_will_win_col1_win(self):
        board = GameBoard([0, 1, 0,
                           0, 1, 0,
                           0, 1, 0])
        self.assertEqual(board.will_win(1), None)

    def test_will_win_col1_blocking(self):
        board = GameBoard([0, 1, 0,
                           0, 1, 0,
                           0, 2, 0])
        self.assertEqual(board.will_win(1), None)
        self.assertEqual(board.will_win(2), None)

    def test_will_win_col2(self):
        board = GameBoard([0, 0, 0,
                           0, 0, 1,
                           0, 0, 1])
        self.assertEqual(board.will_win(1), (0, 2))

    def test_will_win_col2_win(self):
        board = GameBoard([0, 0, 1,
                           0, 0, 1,
                           0, 0, 1])
        self.assertEqual(board.will_win(1), None)

    def test_will_win_col2_blocking(self):
        board = GameBoard([0, 0, 2,
                           0, 0, 1,
                           0, 0, 1])
        self.assertEqual(board.will_win(1), None)
        self.assertEqual(board.will_win(2), None)

    def test_will_win_diag0(self):
        board = GameBoard([1, 0, 0,
                           0, 1, 0,
                           0, 0, 0])
        self.assertEqual(board.will_win(1), (2, 2))

    def test_will_win_diag0_win(self):
        board = GameBoard([1, 0, 0,
                           0, 1, 0,
                           0, 0, 1])
        self.assertEqual(board.will_win(1), None)

    def test_will_win_diag0_blocking(self):
        board = GameBoard([1, 0, 0,
                           0, 1, 0,
                           0, 0, 2])
        self.assertEqual(board.will_win(1), None)
        self.assertEqual(board.will_win(2), None)

    def test_will_win_diag1(self):
        board = GameBoard([0, 0, 1,
                           0, 1, 0,
                           0, 0, 0])
        self.assertEqual(board.will_win(1), (2, 0))

    def test_will_win_diag1_win(self):
        board = GameBoard([0, 0, 1,
                           0, 1, 0,
                           1, 0, 0])
        self.assertEqual(board.will_win(1), None)

    def test_will_win_diag1_blocking(self):
        board = GameBoard([0, 0, 1,
                           0, 1, 0,
                           2, 0, 0])
        self.assertEqual(board.will_win(1), None)
        self.assertEqual(board.will_win(2), None)

    def test_rate_cell0(self):
        board = GameBoard([0, 0, 0,
                           0, 0, 0,
                           0, 0, 0])
        self.assertEqual(board.rate_cell(0, 0, 1), 9)
        self.assertEqual(board.rate_cell(1, 1, 1), 12)

    def test_rate_cell1(self):
        board = GameBoard([0, 0, 0,
                           0, 1, 0,
                           0, 0, 0])
        self.assertEqual(board.rate_cell(0, 0, 1), 18)

    def test_rate_cell2(self):
        board = GameBoard([1, 0, 0,
                           0, 0, 0,
                           0, 0, 0])
        self.assertEqual(board.rate_cell(1, 1, 1), 21)

    def test_rate_cell3_blocked(self):
        board = GameBoard([1, 0, 0,
                           0, 0, 0,
                           0, 0, 2])
        self.assertEqual(board.rate_cell(1, 1, 1), 9)
    def test_rate_cell4(self):
        board = GameBoard([1, 2, 1,
                           2, 0, 0,
                           0, 0, 0])
        self.assertEqual(board.rate_cell(2, 2, 1), 27)
        self.assertEqual(board.rate_cell(1, 1, 1), 24)

