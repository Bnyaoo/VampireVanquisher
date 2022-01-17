import random
from unittest import TestCase

from game import flee_penalty


class TestFleePenalty(TestCase):

    def test_flee_penalty_unsuccessful_escape(self):
        random.seed(0.26)
        character = {'Current HP': 10}
        foe = {'Power': 5}
        the_game_printed_this = flee_penalty(character, foe)
        expected_output = {'Current HP': 5}
        self.assertEqual(expected_output, the_game_printed_this)

    def test_flee_penalty_successful_escape(self):
        random.seed(0.27)
        character = {'Current HP': 5}
        foe = {'Power': 5}
        the_game_printed_this = flee_penalty(character, foe)
        expected_output = {'Current HP': 5}
        self.assertEqual(expected_output, the_game_printed_this)

    def test_flee_penalty_on_percentage_chance_number(self):
        random.seed(0.25)
        character = {'Current HP': 5}
        foe = {'Power': 5}
        the_game_printed_this = flee_penalty(character, foe)
        expected_output = {'Current HP': 5}
        self.assertEqual(expected_output, the_game_printed_this)
