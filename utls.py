from game import (Team, Person)
import sys

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
		pass

	def draw_cards(team1, team2):
		pass

class Jsonable:
	def to_json(self):
		pass