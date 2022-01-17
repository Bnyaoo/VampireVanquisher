from unittest import TestCase
from game import check_if_goal_attained
from game import make_character


class TestCheckIfGoalAttained(TestCase):

    def test_goal_attained(self):
        check_if_goal_attained(make_character())
        the_game_printed_this = check_if_goal_attained(character={'X-coordinate': 3, 'Y-coordinate': 3})
        expected_output = True
        self.assertEqual(expected_output, the_game_printed_this)

    def test_goal_not_yet_attained(self):
        check_if_goal_attained(make_character())
        the_game_printed_this = check_if_goal_attained(character={'X-coordinate': 2, 'Y-coordinate': 3})
        expected_output = False
        self.assertEqual(expected_output, the_game_printed_this)

    def test_missing_key_value(self):
        check_if_goal_attained(make_character())
        the_game_printed_this = check_if_goal_attained(character={'X-coordinate': 3})
        expected_output = False
        self.assertEqual(expected_output, the_game_printed_this)

