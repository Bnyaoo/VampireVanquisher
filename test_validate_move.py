from unittest import TestCase

from game import validate_move
from game import make_character


class TestValidateMove(TestCase):

    def test_moving_east_valid(self):
        actual = validate_move(make_character(), direction="EAST")
        expected_output = True
        self.assertEqual(expected_output, actual)

    def test_moving_west_valid(self):
        actual = validate_move(character={'X-coordinate': 1, 'Y-coordinate': 0}, direction="WEST")
        expected_output = True
        self.assertEqual(expected_output, actual)

    def test_moving_south_valid(self):
        actual = validate_move(make_character(), direction="SOUTH")
        expected_output = True
        self.assertEqual(expected_output, actual)

    def test_moving_north_valid(self):
        actual = validate_move(character={'X-coordinate': 0, 'Y-coordinate': 1}, direction="NORTH")
        expected_output = True
        self.assertEqual(expected_output, actual)

    def test_moving_east_invalid(self):
        actual = validate_move(character={'X-coordinate': 25, 'Y-coordinate': 0}, direction="EAST")
        expected_output = False
        self.assertEqual(expected_output, actual)

    def test_moving_west_invalid(self):
        actual = validate_move(make_character(), direction="WEST")
        expected_output = False
        self.assertEqual(expected_output, actual)

    def test_moving_south_invalid(self):
        actual = validate_move(character={'X-coordinate': 0, 'Y-coordinate': 25}, direction="SOUTH")
        expected_output = False
        self.assertEqual(expected_output, actual)

    def test_moving_north_invalid(self):
        actual = validate_move(make_character(), direction="NORTH")
        expected_output = False
        self.assertEqual(expected_output, actual)

