import sys
import random
from utls import Utls, Card, Person, Team, Jsonable

class Game(Utls, Jsonable):
	def __init__(self):
		self.json_history = {}
		self.round = 0
		self.game = 0
		self.has_winner = False
		self.jsoned = ''

	def prepare(self):
		self.team1, self.team2 = self.make_teams()
		self.players_order = [self.team1.teammates[0], self.team2.teammates[0], self.team1.teammates[1], self.team2.teammates[1]]


	def announce_contracts():
		contracts = ['C', 'D', 'H', 'S', 'no trumps','all trumps']
		return random.choice(contracts)

	def check_if_belote_is_possible(contract, belote_paint):
		if contract == 'no trumps':
			return False
		if contract == 'all trumps':
			return True
		if contract == belote_paint:
			return True
		return False

	def rotate_players_order(players_order):
		first = players_order[0]
		players_order.remove(first)
		players_order.append(first)

		return players_order

	def check_carres_points(carre):
		if carre[1] == 'K' or carre[1] == '13' or carre[1] == 'A' or carre[1] == '14' or carre[1] == 'Q' or carre[1] == '12' or carre[1] == 'T' or carre[1] == '10' :
			return 100
		if carre[1] == '9':
			return 150
		if carre[1] == 'J' or carre[1] == '11':
			return 200
		return 0

	def take_player_annoucements(player):
		annoucements = []

		carre_list = Utls.check_if_there_is_carre(player.cards)
		if len(carre_list) != 0:
			annoucements += carre_list
		quinte_list = Utls.check_if_there_is_quinte(player.cards)
		if len(quinte_list) != 0 and len(carre_list) == 0:
			annoucements.append(quinte_list)
		quarte_list = Utls.check_if_there_is_quarte(player.cards)
		if len(quinte_list) == 0 and len(carre_list) == 0:
			annoucements += quarte_list
		elif len(quinte_list) == 0 and len(carre_list) != 0:
			for i in range(len(quarte_list)):
				for j in range(len(carre_list)):
					if (abs(int(quarte_list[i][2]) - int(carre_list[j][1]))) > 4:
						annoucements.append(quarte_list[i])
		tierce_list = Utls.check_if_there_is_tierce(player.cards)
		if (tierce_list) != 0:
			if len(quinte_list) == 0 and len(quarte_list) == 0 and len(carre_list) == 0:
				annoucements += tierce_list
			elif len(quinte_list) == 0 and len(quarte_list) == 0 and len(carre_list) != 0:
				for i in range(len(carre_list)):
					for j in range(len(tierce_list)):
						if (abs(int(tierce_list[i][2]) - int(carre_list[j][1]))) > 3:
							annoucements.append(tierce_list[i])
			elif len(quinte_list) != 0 and len(quarte_list) == 0 and len(carre_list) == 0:
				for i in range(len(quinte_list)):
					for j in range(len(tierce_list)):
						if quinte_list[i][1] != tierce_list[j][1]:
							annoucements += tierce_list[j]
			elif len(quinte_list) != 0 and len(quarte_list) == 0 and len(carre_list) != 0:
				for i in range(len(quinte_list)):
					for j in range(len(tierce_list)):
						for k in range(len(carre_list)):
							if quinte_list[i][1] != tierce_list[j][1] and (abs(int(tierce_list[i][2]) - int(carre_list[k][1]))) > 3:
								annoucements += tierce_list[j]
			elif len(quinte_list) == 0 and len(quarte_list) != 0 and len(carre_list) == 0:
				for i in range(len(quarte_list)):
					for j in range(len(tierce_list)):
						if quarte_list[i][1] == tierce_list[j][1] and abs(int(quarte_list[i][2]) - int(tierce_list[j][2])) > 3:
							annoucements.append(tierce_list[j])
			elif len(quinte_list) == 0 and len(quarte_list) != 0 and len(carre_list) != 0:
				for i in range(len(quarte_list)):
					for j in range(len(tierce_list)):
						for k in range(len(carre_list)):
							if (quarte_list[i][1] == tierce_list[j][1]) and ((abs(int(quarte_list[i][2])-int(tierce_list[j][2]))) > 3) and ((abs(int(tierce_list[i][2]) - int(carre_list[k][1]))) > 3):
								annoucements.append(tierce_list[j])
		
		belot_list = Utls.check_if_there_is_belote(player.cards)
		if len(belot_list) != 0:
			annoucements += belot_list

		return annoucements

	def check_consecutive_cards_points(announcement):
		if announcement[0] == 'Tierce':
			return 20
		if announcement[0] == 'Quarte':
			return 50
		if announcement[0] == 'Quinte':
			return 100
		if announcement[0] == 'Carre':
			return Game.check_carres_points(announcement)

	def get_player_announcements_ploints(contract, player):
		player_announcements = Game.take_player_annoucements(player)
		
		if len(player_announcements) == 0:
			return 0
		
		points = 0
		
		if contract == 'no trumps':
			for announcement in player_announcements:
				if announcement == ['Carre', 'A'] or announcement == ['Carre', '14']:
					points += 100

		elif contract == 'all trumps':
			for announcements in player_announcements:
				if announcements[0] != 'Belote':
					points += Game.check_consecutive_cards_points(announcements)
				else:
					points += 20
		else:
			for announcements in player_announcements:
				if announcements[0] != 'Belote':
					points += Game.check_consecutive_cards_points(announcements)
				else:
					if Game.check_if_belote_is_possible(contract, announcements[1]):
						points += 20
		return points



	def play(self):

		while self.team1.wins < 2 and self.team2.wins < 2:
			while self.team1.points < 150 and self.team2.points < 150 or self.team1.points == self.team2.points:
				self.team1, self.team2 = Utls.draw_cards()
				contract = announce_contracts()
				for player in players_order:
					pass

				players_order = rotate_players_order(players_order)
				
				self.json_history = self.add_to_json()
				self.jsoned = self.to_json()
				self.write_json()
				self.write_result()
				self.round += 1

			self.has_winner = True
			self.write_result()
			self.has_winner = False
			self.game += 1
			self.round = 0
		
if __name__ == '__main__':
	main()