from unittest import TestCase

from game import game_map


class TestGameMap(TestCase):

    def test_moving_east_valid(self):
        actual = game_map(direction="EAST")
        expected_output = "[['|  |', '|  |', '|  |'], ['|  |', '|  |', '|🧑|'], ['|  |', '|  |', '|  |']]"
        self.assertEqual(expected_output, actual)

    def test_moving_west_valid(self):
        actual = game_map(direction="WEST")
        expected_output = "[['|  |', '|  |', '|  |'], ['|🧑|', '|  |', '|  |'], ['|  |', '|  |', '|  |']]"
        self.assertEqual(expected_output, actual)

    def test_moving_north_valid(self):
        actual = game_map(direction="NORTH")
        expected_output = "[['|  |', '|🧑|', '|  |'], ['|  |', '|  |', '|  |'], ['|  |', '|  |', '|  |']]"
        self.assertEqual(expected_output, actual)

    def test_moving_south_valid(self):
        actual = game_map(direction="SOUTH")
        expected_output = "[['|  |', '|  |', '|  |'], ['|  |', '|  |', '|  |'], ['|  |', '|🧑|', '|  |']]"
        self.assertEqual(expected_output, actual)

    def test_moving_invalid_input(self):
        actual = game_map(direction='sdsa')
        expected_output = "[['|  |', '|  |', '|  |'], ['|  |', '|🧑|', '|  |'], ['|  |', '|  |', '|  |']]"
        self.assertEqual(expected_output, actual)