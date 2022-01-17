from unittest import TestCase
from game import make_character


class TestMakeCharacter(TestCase):

    def test_make_character(self):
        make_character()
        the_game_printed_this = make_character()
        expected_output = {'Class': 0,
                           'Current HP': 20,
                           'EXP': 0,
                           'Power': 1,
                           'X-coordinate': 0,
                           'Y-coordinate': 0}
        self.assertEqual(expected_output, the_game_printed_this)
