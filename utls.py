import random
import json

class Card:
	def __init__(self, value, paint):
		self.value = value
		self.paint = paint

	def __repr__(self):
		paints = {
			'C': '♣',
			'D': '♦',
			'H': '♥',
			'S': '♠'
		}
		return f'{self.value}{paints[self.paint]}'

class Person:
	def __init__(self, name):
		self.name = name
		self.cards = []
		self.announcements = []
		self.points = 0
		#cards = [Card, Card, ...]

class Team:
	def __init__(self, name, teammates):
		self.name = name
		self.teammates = teammates
		# teammates = (Person, Person)
		self.wins = 0
		self.points = 0

class Utls:
	def make_teams(self):
		pass

	def shuffle():
		#C - Club
		#D - Diamond
		#H - Heart
		#S - Spade

		suits = [suit for suit in 'CDHS']
		values = [val for val in '789TJQKA']

		cards = [Card(val, suit) for val in values for suit in suits]

		random.shuffle(cards)

		return cards

	def draw_cards(self, team1, team2):
		pass

	def write_result(self, team1, team2):
		pass

class Jsonable:
	def to_json(self, indent=4):
		teams = (self.team1, self.team2)
		for game in range(self.game + 1):
			for round_ in range(self.round + 1):
				for team in teams:
					for p in team.teammates:
						tmp = self.json_history[f'game {game+1}:'][f'round {round_+1}:'][team.name][p.name]['cards'] = [str(card) for card in p.cards]

		return json.dumps(self.json_history, indent=indent)


	def add_to_json(self):
		game = f'game {self.game + 1}:'
		g_round = f'round {self.round + 1}:'
		if self.json_history == {}:
			self.json_history = {game: {}}

		self.json_history[game][g_round] = {}
		teams = (self.team1, self.team2)

		for i in range(2):
			self.json_history[game][g_round][teams[i].name] = {}
			for j in range(2):
				self.json_history[game][g_round][teams[i].name][teams[i].teammates[j].name] = {
					"cards": teams[i].teammates[j].cards,
					"announcements": teams[i].teammates[j].announcements,
					"points": teams[i].teammates[j].points
				}

		return self.json_history

	def write_json(self):
		with open('data.json', 'a') as f:
			f.write(self.jsoned)