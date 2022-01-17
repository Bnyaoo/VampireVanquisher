import io
from unittest import TestCase
from unittest.mock import patch
from game import get_user_choice


class TestGetUserChoice(TestCase):
    @patch('builtins.input', side_effect=['1'])
    def test_get_user_choice_north(self, _):
        self.assertEqual('NORTH', get_user_choice())

    @patch('builtins.input', side_effect=['2'])
    def test_get_user_choice_east(self, _):
        self.assertEqual('EAST', get_user_choice())

    @patch('builtins.input', side_effect=['3'])
    def test_get_user_choice_south(self, _):
        self.assertEqual('SOUTH', get_user_choice())

    @patch('builtins.input', side_effect=['4'])
    def test_get_user_choice_west(self, _):
        self.assertEqual('WEST', get_user_choice())

    @patch('builtins.input', side_effect=['r', '2'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_get_user_choice_correcting_input(self, mock_output, _):
        get_user_choice()
        expected = 'Invalid input, try again.\n'
        self.assertEqual(expected, mock_output.getvalue())

    @patch('builtins.input', side_effect=['r', '10', '4'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_get_user_choice_consecutive_invalid_input_recovery(self, mock_output, _):
        get_user_choice()
        expected = 'Invalid input, try again.\n' \
                   'Invalid input, try again.\n'
        self.assertEqual(expected, mock_output.getvalue())
