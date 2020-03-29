import unittest
from game import Card, Person, Team, Game, Utls

import random


class TestGameClass(unittest.TestCase):
	def test_random_choice_of_suits(self):
		suits = ['clubs', 'diamonds', 'hearts', 'spides', 'no trumps','all trumps']
		result = random.choice(suits)

		self.assertIsNotNone(result)



if __name__ == '__main__':
	unittest.main()