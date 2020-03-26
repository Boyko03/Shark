import unittest
from utls import Utls, Jsonable
from game import Card
from pprint import pprint

class TestUtlsClass(unittest.TestCase):
	def test_shuffle_function_should_return_shuffled_list_of_Card(self):
		cards = [Card(value,paint) for value in [val for val in '79TJQKA'] for paint in [p for p in 'CDHS']]

		shuffled_cards = Utls.shuffle()
		
		self.assertIsNotNone(shuffled_cards)
		self.assertNotEqual(cards, shuffled_cards)

class TestJsonableClass(unittest.TestCase):
	pass

if __name__ == '__main__':
	unittest.main()