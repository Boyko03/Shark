import unittest
from utls import Utls, Card, Person, Team, Jsonable
from game import Card
from pprint import pprint


class TestCardClass(unittest.TestCase):
	def test_card_string_representation_is_as_expected_one(self):
		card = Card('7', 'D')
		card1 = Card('K', 'S')


		self.assertEqual(str(card),'(7,D)')
		self.assertEqual(str(card1),'(K,S)')

	def test_cards_comparison_less_than_works_correctly_for_numbers_cards(self):

		card = Card('7', 'D')
		card1 = Card('8', 'S')
		
		result = card < card1

		self.assertEqual(result, True)

	def test_cards_comparison_less_than_works_correctly_for_non_numbers_cards(self):

		card = Card('Q', 'D')
		card1 = Card('K', 'S')

		result = card < card1

		self.assertEqual(result, True)

	def test_cards_comparison_less_than_works_correctly_for_number_and_non_number_cards(self):

		card = Card('9', 'D')
		card1 = Card('J', 'S')

		result = card < card1
		opposite_result = card1 < card

		self.assertEqual(result, True)
		self.assertEqual(opposite_result, False)

	def test_comparison_greater_than_works_correctly_for_numbers_cards(self):
		
		card = Card('9', 'D')
		card1 = Card('7', 'S')

		result = card > card1

		self.assertEqual(result, True)


	def test_cards_comparison_greater_than_works_correctly_for_non_numbers_cards(self):

		card = Card('K', 'D')
		card1 = Card('J', 'S')
		result = card > card1

		self.assertEqual(result, True)


	def test_cards_comparison_greater_than_works_correctly_for_number_and_non_number_cards(self):

		card = Card('J', 'D')
		card1 = Card('9', 'S')

		result = card > card1
		opposite_result = card1 > card

		self.assertEqual(result, True)
		self.assertEqual(opposite_result, False)

	def test_cards_comparison_less_or_equal_works_correctly_for_numbers_cards_with_equal_cards(self):

		card = Card('7', 'D')
		card1 = Card('7', 'S')
		
		result = card <= card1

		self.assertEqual(result, True)

	def test_cards_comparison_less_or_equal_works_correctly_for_non_numbers_cards_with_equal_cards(self):

		card = Card('Q', 'D')
		card1 = Card('Q', 'S')

		result = card <= card1

		self.assertEqual(result, True)


	def test_cards_comparison_greater_or_equal_works_correctly_for_numbers_cards_with_equal_cards(self):

		card = Card('7', 'D')
		card1 = Card('7', 'S')
		
		result = card >= card1

		self.assertEqual(result, True)

	def test_cards_comparison_greater_or_equal_works_correctly_for_non_numbers_cards_with_equal_cards(self):

		card = Card('Q', 'D')
		card1 = Card('Q', 'S')

		result = card >= card1

		self.assertEqual(result, True)

	def test_cards_comparison_less_or_equal_works_correctly_for_numbers_cards_with_non_equal_cards(self):

		card = Card('7', 'D')
		card1 = Card('8', 'S')
		
		result = card <= card1

		self.assertEqual(result, True)

	def test_cards_comparison_less_or_equal_works_correctly_for_non_numbers_cards_with_non_equal_cards(self):

		card = Card('T', 'D')
		card1 = Card('J', 'S')
		result = card <= card1

		self.assertEqual(result, True)


	def test_cards_comparison_greater_or_equal_works_correctly_for_numbers_cards_with_non_equal_cards(self):

		card = Card('9', 'D')
		card1 = Card('7', 'S')
		
		result = card >= card1

		self.assertEqual(result, True)

	def test_cards_comparison_greater_or_equal_works_correctly_for_non_numbers_cards_with_non_equal_cards(self):

		card = Card('K', 'D')
		card1 = Card('Q', 'S')

		result = card >= card1

		self.assertEqual(result, True)



class TestPersonClass(unittest.TestCase):
	def test_class_Person_instantiates_name_correctly(self):
		exception = None

		try:
			person = Person(123)
		except Exception as err:
			exception = err

		self.assertIsNotNone(exception)
		self.assertEqual(str(exception), 'Name must be string')


class TestTeamClass(unittest.TestCase):
	def test_validating_names_are_string_not_integer(self):
		exception = None

		try:
			person = Team(123, (Person('Ivan'), Person('Gosho')))
			person1 = Team('name', (Person(123), Person('Gosho')))
			person1 = Team('name', (Person('Ivan'), Person(123)))
		except Exception as err:
			exception = err

		self.assertIsNotNone(exception)
		self.assertEqual(str(exception), 'Name must be string')



	def test_teams_string_representation_is_as_expected(self):
		team = Team('Malinka', (Person('Ivan'), Person('Gosho')))
		team2 = Team('Yagodka', (Person('Pesho'), Person('Tosho')))

		self.assertEqual(str(team), 'Teamname: Malinka, teammates: Ivan, Gosho')
		self.assertEqual(str(team2), 'Teamname: Yagodka, teammates: Pesho, Tosho')


class TestUtlsClass(unittest.TestCase):
	def test_shuffle_function_should_return_shuffled_list_of_Card(self):
		cards = [Card(value,paint) for value in [val for val in '79TJQKA'] for paint in [p for p in 'CDHS']]

		shuffled_cards = Utls.shuffle()
		
		self.assertIsNotNone(shuffled_cards)
		self.assertNotEqual(cards, shuffled_cards)

	def test_draw_cards_function_should_draw_Cards_to_teammates(self):
		cards = Utls.shuffle()

		team1 = Team('Malinka', (Person('Ivan'), Person('Gosho')))
		team2 = Team('Yagodka', (Person('Pesho'), Person('Tosho')))

		Utls.draw_cards(team1, team2)

		first_teammate_team1_cards = cards[:8]
		first_teammate_team2_cards = cards[8:16]
		second_teammate_team1_cards = cards[16:24]
		second_teammate_team2_cards = cards[24:]

		self.assertEqual(len(team1.teammates[0].cards), len(first_teammate_team1_cards))
		self.assertEqual(len(team2.teammates[0].cards), len(first_teammate_team2_cards))
		self.assertEqual(len(team1.teammates[1].cards), len(second_teammate_team1_cards))
		self.assertEqual(len(team2.teammates[1].cards), len(second_teammate_team2_cards))


class TestJsonableClass(unittest.TestCase):
	pass


if __name__ == '__main__':
	unittest.main()