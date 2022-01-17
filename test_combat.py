import random
from unittest import TestCase
from unittest.mock import patch

from game import combat


class TestCombat(TestCase):

    @patch('builtins.input', side_effect=['1'])
    def test_combat_fight(self, _):
        foe = {'Name': 'TESTING', 'Power': 5, 'Current HP': 10}
        character = {'Class': 1, 'Power': 10, 'Current HP': 10, 'EXP': 0}
        the_game_printed_this = combat(character, foe)
        expected_output = 11
        self.assertEqual(expected_output, the_game_printed_this)

    @patch('builtins.input', side_effect=['2'])
    def test_combat_flee_character_takes_damage(self, _):
        random.seed(1)
        foe = {'Name': 'TESTING', 'Power': 5, 'Current HP': 10}
        character = {'Class': 1, 'Power': 10, 'Current HP': 10, 'EXP': 0}
        the_game_printed_this = combat(character, foe)
        expected_output = 5
        self.assertEqual(expected_output, the_game_printed_this)

    @patch('builtins.input', side_effect=['2'])
    def test_combat_flee_character_unscathed(self, _):
        random.seed(2)
        foe = {'Name': 'TESTING', 'Power': 5, 'Current HP': 10}
        character = {'Class': 1, 'Power': 10, 'Current HP': 10, 'EXP': 0}
        the_game_printed_this = combat(character, foe)
        expected_output = 10
        self.assertEqual(expected_output, the_game_printed_this)

    @patch('builtins.input', side_effect=['3'])
    def test_combat_marauder_special_attack(self, _):
        random.seed(2)
        foe = {'Name': 'TESTING', 'Power': 10, 'Current HP': 10}
        character = {'Class': 1, 'Power': 20, 'Current HP': 10, 'EXP': 0}
        the_game_printed_this = combat(character, foe)
        expected_output = 0
        self.assertEqual(expected_output, the_game_printed_this)

    @patch('builtins.input', side_effect=['3'])
    def test_combat_alchemist_special_attack(self, _):
        random.seed(2)
        foe = {'Name': 'TESTING', 'Power': 10, 'Current HP': 10}
        character = {'Class': 2, 'Power': 20, 'Current HP': 10, 'EXP': 0}
        the_game_printed_this = combat(character, foe)
        expected_output = 0
        self.assertEqual(expected_output, the_game_printed_this)

    @patch('builtins.input', side_effect=['3'])
    def test_combat_hunter_special_attack(self, _):
        random.seed(2)
        foe = {'Name': 'TESTING', 'Power': 10, 'Current HP': 10}
        character = {'Class': 3, 'Power': 20, 'Current HP': 10, 'EXP': 0}
        the_game_printed_this = combat(character, foe)
        expected_output = 0
        self.assertEqual(expected_output, the_game_printed_this)

    @patch('builtins.input', side_effect=['3'])
    def test_combat_tormentor_special_attack(self, _):
        random.seed(2)
        foe = {'Name': 'TESTING', 'Power': 10, 'Current HP': 1}
        character = {'Class': 4, 'Power': 20, 'Current HP': 10, 'EXP': 0}
        the_game_printed_this = combat(character, foe)
        expected_output = 0
        self.assertEqual(expected_output, the_game_printed_this)

    @patch('builtins.input', side_effect=['1'])
    def test_combat_character_death(self, _):
        foe = {'Name': 'TESTING', 'Power': 10, 'Current HP': 10}
        character = {'Class': 4, 'Power': 5, 'Current HP': 5, 'EXP': 0}
        the_game_printed_this = combat(character, foe)
        expected_output = -5
        self.assertEqual(expected_output, the_game_printed_this)

    @patch('builtins.input', side_effect=['1'])
    def test_combat_vampire(self, _):
        foe = {'Name': 'Vampire', 'Power': 10, 'Current HP': 20}
        character = {'Class': 4, 'Power': 30, 'Current HP': 20, 'EXP': 0}
        the_game_printed_this = combat(character, foe)
        expected_output = 30
        self.assertEqual(expected_output, the_game_printed_this)