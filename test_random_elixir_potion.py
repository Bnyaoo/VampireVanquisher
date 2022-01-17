import random
from unittest import TestCase

from game import random_elixir_potion


class TestRandomElixirPotion(TestCase):

    def test_random_elixir_potion_success(self):
        random.seed(0.11)
        character = {'Current HP': 0, 'Power': 0}
        the_game_printed_this = random_elixir_potion(character)
        expected_output = {'Current HP': 15, 'Power': 15}
        self.assertEqual(expected_output, the_game_printed_this)

    def test_random_elixir_potion_failure(self):
        random.seed(0.09)
        character = {'Current HP': 5, 'Power': 5}
        the_game_printed_this = random_elixir_potion(character)
        expected_output = {'Current HP': 5, 'Power': 5}
        self.assertEqual(expected_output, the_game_printed_this)

    def test_random_elixir_potion_on_percentage_chance_number(self):
        random.seed(0.10)
        character = {'Current HP': 5, 'Power': 5}
        the_game_printed_this = random_elixir_potion(character)
        expected_output = {'Current HP': 5, 'Power': 5}
        self.assertEqual(expected_output, the_game_printed_this)