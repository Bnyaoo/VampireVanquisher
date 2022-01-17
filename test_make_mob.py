import random
from unittest import TestCase

from game import make_mob
from game import make_character


class TestMakeMob(TestCase):

    def test_make_vampire(self):
        random.seed(1)
        the_game_printed_this = make_mob(make_character())
        expected_output = {'Current HP': 20, 'Name': 'Vampire', 'Power': 10}
        self.assertEqual(expected_output, the_game_printed_this)

    def test_make_knight(self):
        random.seed(2)
        the_game_printed_this = make_mob(make_character())
        expected_output = {'Current HP': 1, 'Name': 'Knight', 'Power': 5}
        self.assertEqual(expected_output, the_game_printed_this)

    def test_make_a_different_knight(self):
        random.seed(3)
        the_game_printed_this = make_mob(make_character())
        expected_output = {'Current HP': 1, 'Name': 'Knight', 'Power': 2}
        self.assertEqual(expected_output, the_game_printed_this)

    def test_make_bandit(self):
        random.seed(4)
        the_game_printed_this = make_mob(make_character())
        expected_output = {'Current HP': 1, 'Name': 'Bandit', 'Power': 2}
        self.assertEqual(expected_output, the_game_printed_this)

    def test_make_mob_scales_with_character_stats(self):
        random.seed(4)
        character = {'Current HP': 18, 'Power': 10}
        the_game_printed_this = make_mob(character)
        expected_output = {'Current HP': 1, 'Name': 'Bandit', 'Power': 2}
        self.assertEqual(expected_output, the_game_printed_this)

    def test_make_wraith(self):
        random.seed(11)
        the_game_printed_this = make_mob(make_character())
        expected_output = {"Current HP": 999,
                           'Guessing Game': 'Answer correctly and gain tremendous power and vitality',
                           'Name': 'Wraith',
                           'Power': 5}
        self.assertEqual(expected_output, the_game_printed_this)
