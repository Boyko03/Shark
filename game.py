import sys
import random
from utls import Utls, Jsonable

class Card:
	def __init__(self, value, paint):
		self.value = value
		self.paint = paint


	def __str__(self):
		return f'({self.value},{self.paint})'

	def __repr__(self):
		return f'Card {self}'

	def __lt__(self, other):
		return self.value < other.value

	def __gt__(self, other):
		return self.value > other.value

	def __le__(self,other):
		return self.value <= other.value

	def __ge__(self, other):
		return self.value >= other.value


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

class Game(Utls, Jsonable):
	def prepare(self):
		self.team1, self.team2 = self.make_teams(name, teammates)
		self.cards = shuffle()
		draw_cards(team1, team2)
		pass

	def play(self):
		#Some code

		self.to_json()
		
if __name__ == '__main__':
	main()