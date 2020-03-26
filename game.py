import sys
import random
from utls import Utls, Jsonable

class Card:
	def __init__(self, value, paint):
		self.value = value
		self.paint = paint

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

class Game(Utls, Jsonable):
	def prepare(self):
		self.team1, self.team2 = self.make_teams()
		self.cards = shuffle()
		pass

	def play(self):
		#Some code

		self.to_json()
		
if __name__ == '__main__':
	main()