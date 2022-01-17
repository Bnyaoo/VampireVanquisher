from unittest import TestCase
import random

from game import check_for_foes


class TestCheckForFoes(TestCase):

    def test_check_for_foes_encountered(self):
        random.seed(0.24)
        the_game_printed_this = check_for_foes()
        expected_output = True
        self.assertEqual(expected_output, the_game_printed_this)

    def test_check_for_foes_evaded(self):
        random.seed(0.25)
        the_game_printed_this = check_for_foes()
        expected_output = False
        self.assertEqual(expected_output, the_game_printed_this)

    def test_check_for_foes_zero_not_in_range_of_random(self):
        random.seed(0)
        the_game_printed_this = check_for_foes()
        expected_output = False
        self.assertEqual(expected_output, the_game_printed_this)

    def test_check_for_foes_greater_than_not_in_range_of_random(self):
        random.seed(0.28)
        the_game_printed_this = check_for_foes()
        expected_output = False
        self.assertEqual(expected_output, the_game_printed_this)