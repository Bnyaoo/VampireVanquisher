import random
from unittest import TestCase
from game import make_board
from unittest.mock import patch


class TestMakeBoard(TestCase):

    @patch('random.sample')
    def test_make_board_lake(self, random_sample_list):
        random.seed(0)
        actual = make_board(1, 1)
        expected = {(0, 0): '\x1b[37mLibrary\x1b[0m'}
        self.assertEqual(expected, actual)

    @patch('random.sample')
    def test_make_board_swamp(self, random_sample_list):
        random.seed(1)
        actual = make_board(1, 1)
        expected = {(0, 0): '\x1b[37mFlaying room\x1b[0m'}
        self.assertEqual(expected, actual)

    @patch('random.sample')
    def test_make_board_plain(self, random_sample_list):
        random.seed(2)
        actual = make_board(1, 1)
        expected = {(0, 0): '\x1b[37mCorridor\x1b[0m'}
        self.assertEqual(expected, actual)

    @patch('random.sample')
    def test_make_board_volcano(self, random_sample_list):
        random.seed(5)
        actual = make_board(1, 1)
        expected = {(0, 0): '\x1b[37mBallroom\x1b[0m'}
        self.assertEqual(expected, actual)

    @patch('random.sample')
    def test_make_board_forest(self, random_sample_list):
        random.seed(7)
        actual = make_board(1, 1)
        expected = {(0, 0): '\x1b[37mSpiraling staircase\x1b[0m'}
        self.assertEqual(expected, actual)

    @patch('random.sample')
    def test_make_board_three_by_three(self, random_sample_list):
        random.seed(7)
        actual = make_board(4, 4)
        expected = {(0, 0): '\x1b[37mSpiraling staircase\x1b[0m', (0, 1): '\x1b[37mFlaying room\x1b[0m', (0, 2):
                    '\x1b[37mLibrary\x1b[0m', (0, 3): '\x1b[37mCorridor\x1b[0m', (1, 0): '\x1b[37mCorridor\x1b[0m',
                    (1, 1): '\x1b[37mBallroom\x1b[0m',
                    (1, 2): '\x1b[37mCorridor\x1b[0m', (1, 3): '\x1b[37mSpiraling staircase\x1b[0m', (2, 0):
                        '\x1b[37mBallroom\x1b[0m',
                    (2, 1): '\x1b[37mCorridor\x1b[0m', (2, 2): '\x1b[37mBallroom\x1b[0m',
                    (2, 3): '\x1b[37mFlaying room\x1b[0m',
                    (3, 0): '\x1b[37mCorridor\x1b[0m', (3, 1): '\x1b[37mCorridor\x1b[0m', (3, 2):
                        '\x1b[37mLibrary\x1b[0m',
                    (3, 3): '\x1b[37mLibrary\x1b[0m'}
        self.assertEqual(expected, actual)

    @patch('random.sample')
    def test_make_board_zero_by_zero(self, random_sample_list):
        actual = make_board(0, 0)
        expected = {}
        self.assertEqual(expected, actual)
