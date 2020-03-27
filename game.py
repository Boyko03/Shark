import sys
from utls import Utls, Card, Person, Team, Jsonable

class Game(Utls, Jsonable):
	def __init__(self):
		self.json_history = {}
		self.round = 0
		self.game = 0

	def prepare(self):
		self.team1, self.team2 = self.make_teams()
		self.cards = shuffle()
		
		self.team1, self.team2 = self.draw_cards()

	def play(self):
		while self.team1.wins < 2 and self.team2.wins < 2:
			while self.team1.points < 150 and self.team2.points < 150 or self.team1.points == self.team2.points:
				self.json_history = self.add_to_json()
				self.round += 1

			self.game += 1
			self.round = 0

			self.jsoned = self.to_json()
			self.write_json()
		
if __name__ == '__main__':
	main()