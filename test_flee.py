from unittest import TestCase
from unittest.mock import patch

from game import flee


class TestFlee(TestCase):

    @patch('builtins.input', side_effect=['1'])
    def test_choose_to_fight(self, _):
        foe = {'Name': 'TEST_GHOUL'}
        the_game_printed_this = flee(foe)
        expected_output = True
        self.assertEqual(expected_output, the_game_printed_this)

    @patch('builtins.input', side_effect=['2'])
    def test_choose_to_flee(self, _):
        foe = {'Name': 'TEST_GHOUL'}
        the_game_printed_this = flee(foe)
        expected_output = False
        self.assertEqual(expected_output, the_game_printed_this)
