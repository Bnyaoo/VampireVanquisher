import io
from unittest import TestCase
from unittest.mock import patch

from game import make_character
from game import guessing_game


class TestGuessingGame(TestCase):

    @patch('builtins.input', side_effect=[5, 5, 5])
    @patch('random.randint', return_value=5)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_guessing_game(self, mock_output, random_number_generator, mock_input):
        guessing_game(make_character())
        the_game_printed_this = mock_output.getvalue()
        expected_output = "You're right!\nThe Wraith grants you... \x1b[35mHP +20  Power +5\x1b[0m\n"""
        self.assertEqual(expected_output, the_game_printed_this)

    @patch('builtins.input', side_effect=[1, 5, 5])
    @patch('random.randint', return_value=5)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_simple_game_too_low(self, mock_output, random_number_generator, mock_input):
        guessing_game(make_character())
        the_game_printed_this = mock_output.getvalue()
        expected_output = "Too low, the number was 5\n"
        self.assertEqual(expected_output, the_game_printed_this)

    @patch('builtins.input', side_effect=[5, 5, 5])
    @patch('random.randint', return_value=4)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_simple_game_too_high(self, mock_output, random_number_generator, mock_input):
        guessing_game(make_character())
        the_game_printed_this = mock_output.getvalue()
        expected_output = "Too high, the number was 4\nThe Wraith drains your life force... d[59 chars]0m\n'"
        self.assertEqual(expected_output, the_game_printed_this)