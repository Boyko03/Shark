import sys
import random

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

class Game:
	def prepare(self):
		self.team1, self.team2 = self.make_teams()
		self.cards = shuffle()
		pass

	def make_teams(self):
		pass

	def shuffle():
		#C - Club
		#D - Diamond
		#H - Heart
		#S - Spade
		pass

	def draw_cards(team1, team2):
		pass

	def play(self):
		#Some code

		self.to_json()

	def to_json(self):
		pass
		
if __name__ == '__main__':
	main()