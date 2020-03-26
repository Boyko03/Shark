import sys
from utls import Utls, Card, Person, Team, Jsonable

class Game(Utls, Jsonable):
	def prepare(self):
		self.team1, self.team2 = self.make_teams()
		self.cards = shuffle()
		
		self.team1, self.team2 = self.draw_cards()

	def play(self):
		#Some code

		self.to_json()
		
if __name__ == '__main__':
	main()