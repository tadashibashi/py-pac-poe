import unittest
from Board import Board

class TestBoard(unittest.TestCase):
    def test_init(self):
        board = Board(3, 3)

        self.assertEqual(len(board.board), 9)

        expected = [0, 0, 0,
                    0, 0, 0,
                    0, 0, 0]
        
        self.assertListEqual(board.board, expected)

    def test_init_list(self):
        board = Board(3, 3, [0, 0, 0,
                             0, 0, 0,
                             0, 0, 0])
        expected = [0, 0, 0,
                    0, 0, 0,
                    0, 0, 0]
        self.assertListEqual(board.board, expected)

    def test_init_list_invalid(self):
        self.assertRaises(ValueError, lambda : Board(3, 4,
                             [0, 0, 0,
                              0, 0, 0,
                              0, 0, 0]))


    def test_set1(self):
        board = Board(3, 3)

        board.set(1, 1, 999)

        expected = [0, 0, 0,
                    0, 999, 0,
                    0, 0, 0]
        
        self.assertListEqual(board.board, expected)

    def test_set2(self):
        board = Board(3, 3)

        board.set(0, 0, 999)
        board.set(1, 2, 999)
        board.set(2, 1, 999)

        expected = [999, 0, 0,
                    0, 0, 999,
                    0, 999, 0]
        
        self.assertListEqual(board.board, expected)
