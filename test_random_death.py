import random
from unittest import TestCase
from unittest.mock import patch

from game import random_death


class TestRandomDeath(TestCase):

    @patch('random.sample')
    def test_random_death_1(self, _):
        random.seed(1)
        expected = 'shivved you in the kidney'
        actual = random_death()
        self.assertEqual(expected, actual)

    @patch('random.sample')
    def test_random_death_2(self, _):
        random.seed(2)
        expected = 'tore your throat out'
        actual = random_death()
        self.assertEqual(expected, actual)

