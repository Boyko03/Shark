import random
from pprint import pprint

class Card:
	def __init__(self, value, paint):
		self.value = value
		self.paint = paint


	def __str__(self):
		return f'({self.value},{self.paint})'

	def __repr__(self):
		paints = {
			'C': '♣',
			'D': '♦',
			'H': '♥',
			'S': '♠'
		}
		return f'{self.value} {paints[self.paint]}'


	def __lt__(self, other):
		if self.value == 'T':
			self.value = 10
		if self.value == 'J':
			self.value = 11
		if self.value == 'Q':
			self.value = 12
		if self.value == 'K':
			self.value = 13
		if self.value == 'A':
			self.value = 14

		if other.value == 'T':
			other.value = 10
		if other.value == 'J':
			other.value = 11
		if other.value == 'Q':
			other.value = 12
		if other.value == 'K':
			other.value = 13
		if other.value == 'A':
			other.value = 14
		
		return int(self.value) < int(other.value)

	def __gt__(self, other):
		if self.value == 'T':
			self.value = 10
		if self.value == 'J':
			self.value = 11
		if self.value == 'Q':
			self.value = 12
		if self.value == 'K':
			self.value = 13
		if self.value == 'A':
			self.value = 14

		if other.value == 'T':
			other.value = 10
		if other.value == 'J':
			other.value = 11
		if other.value == 'Q':
			other.value = 12
		if other.value == 'K':
			other.value = 13
		if other.value == 'A':
			other.value = 14
		
		return int(self.value) > int(other.value)


	def __le__(self,other):
		if self.value == 'T':
			self.value = 10
		if self.value == 'J':
			self.value = 11
		if self.value == 'Q':
			self.value = 12
		if self.value == 'K':
			self.value = 13
		if self.value == 'A':
			self.value = 14

		if other.value == 'T':
			other.value = 10
		if other.value == 'J':
			other.value = 11
		if other.value == 'Q':
			other.value = 12
		if other.value == 'K':
			other.value = 13
		if other.value == 'A':
			other.value = 14
		
		return int(self.value) <= int(other.value)


	def __ge__(self, other):
		if self.value == 'T':
			self.value = 10
		if self.value == 'J':
			self.value = 11
		if self.value == 'Q':
			self.value = 12
		if self.value == 'K':
			self.value = 13
		if self.value == 'A':
			self.value = 14

		if other.value == 'T':
			other.value = 10
		if other.value == 'J':
			other.value = 11
		if other.value == 'Q':
			other.value = 12
		if other.value == 'K':
			other.value = 13
		if other.value == 'A':
			other.value = 14
		
		return int(self.value) >= int(other.value)


class Person:
	def __init__(self, name):
		if type(name) is not str:
			raise ValueError('Name must be string')

		self.name = name
		self.cards = []
		#cards = [Card, Card, ...]

	def __str__(self):
		return f'{self.name}'

	def __repr__(self):
		return f'Person {self}'


class Team:
	def __init__(self, name, teammates):
		if type(name) is not str:
			raise ValueError('Name must be string')
		
		self.name = name
		self.teammates = teammates
		# teammates = (Person, Person)
		self.wins = 0
		self.points = 0

	def __str__(self):
		return f'Teamname: {self.name}, teammates: {self.teammates[0].name}, {self.teammates[1].name}'


class Utls:	

	def make_teams(self):	
		team1 = Team(sys.argv[1], (Person(sys.argv[2]), Person(sys.argv[3])))
		team2 = Team(sys.argv[4], (Person(sys.argv[5]), Person(sys.argv[6])))

		return Team(team1), Team(team2)

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

	def draw_cards(team1, team2):
		cards_list = Utls.shuffle()

		team1.teammates[0].cards = cards_list[:8]
		team2.teammates[0].cards = cards_list[8:16]
		team1.teammates[1].cards = cards_list[16:24]
		team2.teammates[1].cards = cards_list[24:]

		return team1.teammates[0].cards, team2.teammates[0].cards, team1.teammates[1].cards, team2.teammates[1].cards

		

class Jsonable:

	def to_json(self):
		pass

if __name__ == '__main__':
	main()