import sys

class Card:
	def __init__(self, value, paint):
		self.value = value
		self.paint = paint

class Person:
	def __init__(self, name):
		self.name = name

class Team:
	def __init__(self, p1, p2):
		self.p1 = p1
		self.p2 = p2

def player_input():
	pass

def shuffle():
	pass

def main():
	team1, team2 = player_input()
	cards = [Card(value, paint) for value, paint in shuffle()]

if __name__ == '__main__':
	main()