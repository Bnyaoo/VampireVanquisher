import random
from unittest import TestCase
from unittest.mock import patch

from game import describe_current_location
from game import make_board
from game import make_character


class TestDescribeCurrentLocation(TestCase):

    @patch('random.sample')
    def test_describe_current_location_swamp(self, random_sample):
        random.seed(1)
        the_game_printed_this = describe_current_location(make_board(1, 1), make_character())
        expected_output = '\x1b[37mFlaying room\x1b[0m'
        self.assertEqual(expected_output, the_game_printed_this)

    @patch('random.sample')
    def test_describe_current_location_island(self, random_sample):
        random.seed(0)
        the_game_printed_this = describe_current_location(make_board(1, 1), make_character())
        expected_output = '\x1b[37mLibrary\x1b[0m'
        self.assertEqual(expected_output, the_game_printed_this)

    @patch('random.sample')
    def test_describe_current_location_plain(self, random_sample):
        random.seed(2)
        the_game_printed_this = describe_current_location(make_board(1, 1), make_character())
        expected_output = '\x1b[37mCorridor\x1b[0m'
        self.assertEqual(expected_output, the_game_printed_this)

    @patch('random.sample')
    def test_describe_current_location_mountain(self, random_sample):
        random.seed(5)
        the_game_printed_this = describe_current_location(make_board(1, 1), make_character())
        expected_output = '\x1b[37mBallroom\x1b[0m'
        self.assertEqual(expected_output, the_game_printed_this)

    @patch('random.sample')
    def test_describe_current_location_forest(self, random_sample):
        random.seed(7)
        the_game_printed_this = describe_current_location(make_board(1, 1), make_character())
        expected_output = '\x1b[37mSpiraling staircase\x1b[0m'
        self.assertEqual(expected_output, the_game_printed_this)