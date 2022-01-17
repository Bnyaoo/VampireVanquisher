import random
from unittest import TestCase

from game import class_board_interaction
from game import make_board


class TestClassBoardInteraction(TestCase):

    def test_class_board_interaction_marauder(self):
        random.seed(3)
        board = make_board(25, 25)
        character = {'X-coordinate': 2, 'Y-coordinate': 2, 'Class': 1, 'Power': 1}
        the_game_printed_this = class_board_interaction(board, character)
        expected_output = {'X-coordinate': 2, 'Y-coordinate': 2, 'Class': 1, 'Power': 1}
        self.assertEqual(expected_output, the_game_printed_this)

    def test_class_board_interaction_alchemist(self):
        random.seed(1)
        board = make_board(25, 25)
        character = {'X-coordinate': 2, 'Y-coordinate': 2, 'Class': 2, 'Power': 1}
        the_game_printed_this = class_board_interaction(board, character)
        expected_output = {'X-coordinate': 2, 'Y-coordinate': 2, 'Class': 2, 'Power': 1}
        self.assertEqual(expected_output, the_game_printed_this)

    def test_class_board_interaction_hunter(self):
        random.seed(5)
        board = make_board(25, 25)
        character = {'X-coordinate': 2, 'Y-coordinate': 2, 'Class': 3, 'Power': 1}
        the_game_printed_this = class_board_interaction(board, character)
        expected_output = {'X-coordinate': 2, 'Y-coordinate': 2, 'Class': 3, 'Power': 1}
        self.assertEqual(expected_output, the_game_printed_this)

    def test_class_board_interaction_tormentor(self):
        random.seed(8)
        board = make_board(25, 25)
        character = {'X-coordinate': 2, 'Y-coordinate': 2, 'Class': 4, 'Power': 1}
        the_game_printed_this = class_board_interaction(board, character)
        expected_output = {'X-coordinate': 2, 'Y-coordinate': 2, 'Class': 4, 'Power': 1}
        self.assertEqual(expected_output, the_game_printed_this)

    def test_class_board_interaction_corridor(self):
        random.seed(9)
        board = make_board(25, 25)
        character = {'X-coordinate': 2, 'Y-coordinate': 2, 'Class': 0, 'Power': 1}
        the_game_printed_this = class_board_interaction(board, character)
        expected_output = {'X-coordinate': 2, 'Y-coordinate': 2, 'Class': 0, 'Power': 1}
        self.assertEqual(expected_output, the_game_printed_this)