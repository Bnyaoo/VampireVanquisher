import random

from unittest import TestCase
from unittest.mock import patch

from game import character_class
from game import make_character


class TestCharacterClass(TestCase):

    @patch('builtins.input', side_effect=['1'])
    def test_character_class_marauder(self, _):
        the_game_printed_this = character_class(make_character())
        expected_output = {'Class': '1',
                           'Current HP': 35,
                           'EXP': 0,
                           'Power': 1,
                           'X-coordinate': 0,
                           'Y-coordinate': 0}
        self.assertEqual(expected_output, the_game_printed_this)

    @patch('builtins.input', side_effect=['2'])
    def test_character_class_alchemist(self, _):
        the_game_printed_this = character_class(make_character())
        expected_output = {'Class': '2',
                           'Current HP': 15,
                           'EXP': 0,
                           'Power': 15,
                           'X-coordinate': 0,
                           'Y-coordinate': 0}
        self.assertEqual(expected_output, the_game_printed_this)

    @patch('builtins.input', side_effect=['3'])
    def test_character_class_hunter(self, _):
        the_game_printed_this = character_class(make_character())
        expected_output = {'Class': '3',
                           'Current HP': 25,
                           'EXP': 0,
                           'Power': 5,
                           'Tamed Foe': 0,
                           'X-coordinate': 0,
                           'Y-coordinate': 0}
        self.assertEqual(expected_output, the_game_printed_this)

    @patch('builtins.input', side_effect=['4'])
    def test_character_class_tormentor(self, _):
        random.seed(1)
        the_game_printed_this = character_class(make_character())
        expected_output = {'Class': '4',
                           'Current HP': 19,
                           'EXP': 0,
                           'Power': 6,
                           'X-coordinate': 0,
                           'Y-coordinate': 0}
        self.assertEqual(expected_output, the_game_printed_this)