import random
from unittest import TestCase
from unittest.mock import patch

from game import level_up_2


class TestLevelUp2(TestCase):

    def test_level_up_class_1(self):
        character = {'Current HP': 0, 'Power': 0, 'Class': "1", 'EXP': 21}
        expected = {'Class': '1', 'Current HP': 15, 'EXP': 22, 'Power': 10}
        actual = level_up_2(character=character)
        self.assertEqual(expected, actual)

    def test_level_up_class_2(self):
        character = {'Current HP': 0, 'Power': 0, 'Class': "2", 'EXP': 21}
        expected = {'Class': '2', 'Current HP': 10, 'EXP': 22, 'Power': 15}
        actual = level_up_2(character=character)
        self.assertEqual(expected, actual)

    def test_level_up_class_3(self):
        character = {'Current HP': 0, 'Power': 0, 'Class': "3", 'EXP': 21}
        expected = {'Class': '3', 'Current HP': 12, 'EXP': 22, 'Power': 12}
        actual = level_up_2(character=character)
        self.assertEqual(expected, actual)

    @patch('random.sample')
    def test_level_up_class_4(self, _):
        random.seed(1)
        character = {'Current HP': 0, 'Power': 0, 'Class': "4", 'EXP': 21}
        expected = {'Class': '4', 'Current HP': 9, 'EXP': 22, 'Power': 23}
        actual = level_up_2(character=character)
        self.assertEqual(expected, actual)

    def test_level_up_not_enough_exp(self):
        random.seed(1)
        character = {'Class': '4', 'Current HP': 5, 'EXP': 20, 'Power': 5}
        expected = {'Class': '4', 'Current HP': 5, 'EXP': 20, 'Power': 5}
        actual = level_up_2(character=character)
        self.assertEqual(expected, actual)

    def test_level_up_too_much_exp(self):
        random.seed(1)
        character = {'Class': '4', 'Current HP': 5, 'EXP': 22, 'Power': 11}
        expected = {'Class': '4', 'Current HP': 5, 'EXP': 22, 'Power': 11}
        actual = level_up_2(character=character)
        self.assertEqual(expected, actual)
