from unittest import TestCase
from game import is_alive
from game import make_character


class TestIsAlive(TestCase):

    def test_is_dead(self):
        is_alive(make_character())
        the_game_printed_this = is_alive(character={'Current HP': 0})
        expected_output = False
        self.assertEqual(expected_output, the_game_printed_this)

    def test_is_alive(self):
        is_alive(make_character())
        the_game_printed_this = is_alive(character={'Current HP': 5})
        expected_output = True
        self.assertEqual(expected_output, the_game_printed_this)