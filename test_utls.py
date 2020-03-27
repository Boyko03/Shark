import unittest
from utls import Utls, Jsonable
from game import Game, Team, Card, Person
from pprint import pprint
import json

class TestCardClass(unittest.TestCase):
	pass

class TestPersonClass(unittest.TestCase):
	pass

class TestTeamClass(unittest.TestCase):
	pass

class TestUtlsClass(unittest.TestCase):
	def test_shuffle_function_should_return_shuffled_list_of_Card(self):
		cards = [Card(value,paint) for value in [val for val in '79TJQKA'] for paint in [p for p in 'CDHS']]

		shuffled_cards = Utls.shuffle()
		
		self.assertIsNotNone(shuffled_cards)
		self.assertNotEqual(cards, shuffled_cards)

class TestJsonableClass(unittest.TestCase):
	def test_add_to_json_with_1_round_only_returns_new_dict(self):
		game = Game()
		team1 = Team('team1', (Person('p1'), Person('p2')))
		team2 = Team('team2', (Person('p3'), Person('p4')))
		team1.teammates[0].cards = [Card(value, 'C') for value in [val for val in '789TJQKA']]
		team1.teammates[1].cards = [Card(value, 'D') for value in [val for val in '789TJQKA']]
		team2.teammates[0].cards = [Card(value, 'H') for value in [val for val in '789TJQKA']]
		team2.teammates[1].cards = [Card(value, 'S') for value in [val for val in '789TJQKA']]
		game.team1 = team1
		game.team2 = team2
		teams = (team1, team2)

		game.json_history = game.add_to_json()
		expected = {}
		expected['game 1:'] = {'round 1:': {}}
		for i in range(2):
			expected['game 1:']['round 1:'][teams[i].name] = {}
			for j in range(2):
				team = teams[i]
				p = team.teammates[j]
				expected['game 1:']['round 1:'][team.name][p.name] = {}
				expected['game 1:']['round 1:'][team.name][p.name]['cards'] = p.cards
				expected['game 1:']['round 1:'][team.name][p.name]['announcements'] = p.announcements
				expected['game 1:']['round 1:'][team.name][p.name]['points'] = p.points

		self.maxDiff = None
		self.assertEqual(game.json_history, expected)

	def test_add_to_json_with_more_rounds_returns_dict_with_both_new_and_old_data(self):
		game = Game()
		team1 = Team('team1', (Person('p1'), Person('p2')))
		team2 = Team('team2', (Person('p3'), Person('p4')))
		round_ = 1
		expected = {}

		for i in range(2):
			team1.teammates[0].cards = [Card(value, 'C') for value in [val for val in '789TJQKA']]
			team1.teammates[1].cards = [Card(value, 'D') for value in [val for val in '789TJQKA']]
			team2.teammates[0].cards = [Card(value, 'H') for value in [val for val in '789TJQKA']]
			team2.teammates[1].cards = [Card(value, 'S') for value in [val for val in '789TJQKA']]
			game.team1 = team1
			game.team2 = team2
			teams = (team1, team2)

			game.json_history = game.add_to_json()
			expected['game 1:'] = {f'round {round_}:': {}}
			for i in range(2):
				expected['game 1:'][f'round {round_}:'][teams[i].name] = {}
				for j in range(2):
					team = teams[i]
					p = team.teammates[j]
					expected['game 1:'][f'round {round_}:'][team.name][p.name] = {}
					expected['game 1:'][f'round {round_}:'][team.name][p.name] = {
						'cards': p.cards,
						'announcements': p.announcements,
						'points': p.points
					}
			round_ += 1

	def test_to_json_function_returns_in_json_format(self):
		game = Game()
		team1 = Team('team1', (Person('p1'), Person('p2')))
		team2 = Team('team2', (Person('p3'), Person('p4')))
		team1.teammates[0].cards = [Card(value, 'C') for value in [val for val in '789TJQKA']]
		team1.teammates[1].cards = [Card(value, 'D') for value in [val for val in '789TJQKA']]
		team2.teammates[0].cards = [Card(value, 'H') for value in [val for val in '789TJQKA']]
		team2.teammates[1].cards = [Card(value, 'S') for value in [val for val in '789TJQKA']]
		game.team1 = team1
		game.team2 = team2
		teams = (team1, team2)
		game.json_history = game.add_to_json()

		result = game.to_json()
		expected = json.dumps(game.json_history, indent=4)

		self.assertEqual(result, expected)
		

if __name__ == '__main__':
	unittest.main()