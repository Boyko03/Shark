import random
from pprint import pprint

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
		return f'{self.value} {paints[self.paint]}'

class Person:
	def __init__(self, name):
		self.name = name
		self.cards = []
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
	def to_json(self):
		pass