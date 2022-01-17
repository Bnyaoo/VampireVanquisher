from unittest import TestCase
from game import final_boss


class TestFinalBoss(TestCase):

    def test_final_boss(self):
        the_game_printed_this = final_boss()
        expected_output = {'Name': 'Alukah, the first vampire', 'Current HP': 200, 'Power': 22}
        self.assertEqual(expected_output, the_game_printed_this)
