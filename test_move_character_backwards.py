from unittest import TestCase

from game import move_character_backwards


class TestMoveCharacter(TestCase):

    def test_move_character_move_north(self):
        character = {'X-coordinate': 0, 'Y-coordinate': 1, 'Current HP': 5}
        move_character_backwards(character, direction="SOUTH")
        expected = {'X-coordinate': 0, 'Y-coordinate': 0, 'Current HP': 5}
        actual = character
        self.assertEqual(expected, actual)

    def test_move_character_move_south(self):
        character = {'X-coordinate': 0, 'Y-coordinate': 0, 'Current HP': 5}
        move_character_backwards(character, direction="NORTH")
        expected = {'X-coordinate': 0, 'Y-coordinate': 1, 'Current HP': 5}
        actual = character
        self.assertEqual(expected, actual)

    def test_move_character_move_east(self):
        character = {'X-coordinate': 0, 'Y-coordinate': 0, 'Current HP': 5}
        move_character_backwards(character, direction="WEST")
        expected = {'X-coordinate': 1, 'Y-coordinate': 0, 'Current HP': 5}
        actual = character
        self.assertEqual(expected, actual)

    def test_move_character_move_west(self):
        character = {'X-coordinate': 1, 'Y-coordinate': 0, 'Current HP': 5}
        move_character_backwards(character, direction="EAST")
        expected = {'X-coordinate': 0, 'Y-coordinate': 0, 'Current HP': 5}
        actual = character
        self.assertEqual(expected, actual)

