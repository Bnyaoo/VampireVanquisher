from unittest import TestCase
from unittest.mock import patch

from game import user_name


class TestUserName(TestCase):

    @patch('builtins.input', side_effect=['Benny'])
    def test_user_name(self, _):
        character = {'Name': ''}
        the_game_printed_this = user_name(character)
        expected_output = {'Name': 'Benny'}
        self.assertEqual(expected_output, the_game_printed_this)

    @patch('builtins.input', side_effect=['1232144'])
    def test_user_name_numbers(self, _):
        character = {'Name': ''}
        the_game_printed_this = user_name(character)
        expected_output = {'Name': '1232144'}
        self.assertEqual(expected_output, the_game_printed_this)

    @patch('builtins.input', side_effect=['#^#@&^#^'])
    def test_user_name_special_characters(self, _):
        character = {'Name': ''}
        the_game_printed_this = user_name(character)
        expected_output = {'Name': '#^#@&^#^'}
        self.assertEqual(expected_output, the_game_printed_this)

    @patch('builtins.input', side_effect=['#H@__121_344SD*'])
    def test_user_name_combination_of_all_three(self, _):
        character = {'Name': ''}
        the_game_printed_this = user_name(character)
        expected_output = {'Name': '#H@__121_344SD*'}
        self.assertEqual(expected_output, the_game_printed_this)


