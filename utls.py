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

	def __check_card_value(self):
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

		return self.value


	def __lt__(self, other):
		self.__check_card_value()
		other.__check_card_value()

		return int(self.value) < int(other.value)

	def __gt__(self, other):
		self.__check_card_value()
		other.__check_card_value()
		
		return int(self.value) > int(other.value)


	def __le__(self,other):
		self.__check_card_value()
		other.__check_card_value()
		
		return int(self.value) <= int(other.value)


	def __ge__(self, other):
		self.__check_card_value()
		other.__check_card_value()
		
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
		first_team_name = input('Team 1 Name: ')
		second_team_name = input('Team 2 Name: ')
		print(first_team_name, end=' ')
		teammates_team1 = input('players: ')
		print(second_team_name, end=' ')
		teammates_team2 = input('players: ')

		first_teammate_team1 = teammates_team1.split(', ')[0]
		second_teammate_team1 = teammates_team1.split(', ')[1]

		first_teammate_team2 = teammates_team2.split(', ')[0]
		second_teammate_team2 = teammates_team2.split(', ')[1]
		

		team1 = Team(first_team_name, (Person(first_teammate_team1), Person(second_teammate_team1)))
		team2 = Team(second_team_name, (Person(first_teammate_team2), Person(second_teammate_team2)))

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


	def sort_cards(cards):
		clubs_list = []
		diamonds_list = []
		hearts_list = []
		spades_list = []

		for card in cards: #sorting by paint
			if card.paint == 'C':
				clubs_list.append(card)
			if card.paint == 'D':
				diamonds_list.append(card)
			if card.paint == 'H':
				hearts_list.append(card)
			if card.paint == 'S':
				spades_list.append(card)

		if len(clubs_list) != 0: #sorting by value
			clubs_list = sorted(clubs_list)
		if len(diamonds_list) != 0:
			diamonds_list = sorted(diamonds_list)
		if len(hearts_list) != 0:
			hearts_list = sorted(hearts_list)
		if len(spades_list) != 0:
			spades_list = sorted(spades_list)

		temp = []

		temp = clubs_list + diamonds_list + hearts_list + spades_list

		return temp 

	def draw_cards(team1, team2):
		cards_list = Utls.shuffle()

		team1.teammates[0].cards = cards_list[:8]
		team2.teammates[0].cards = cards_list[8:16]
		team1.teammates[1].cards = cards_list[16:24]
		team2.teammates[1].cards = cards_list[24:]

		team1.teammates[0].cards = Utls.sort_cards(team1.teammates[0].cards)		
		team1.teammates[1].cards = Utls.sort_cards(team1.teammates[1].cards)		
		team2.teammates[0].cards = Utls.sort_cards(team2.teammates[0].cards)		
		team2.teammates[1].cards = Utls.sort_cards(team2.teammates[1].cards)		

		return team1.teammates[0].cards, team2.teammates[0].cards, team1.teammates[1].cards, team2.teammates[1].cards

	def check_if_there_is_belote(cards):
		belote_list = []
		for i in range(len(cards)-1):
			if cards[i].value == 12:
				if cards[i+1].value == 13:
					if cards[i].paint == cards[i+1].paint:
						belote_list.append([str('Belote'), str(cards[i].paint)])

		return belote_list

	def check_if_there_is_tierce(cards):
		tierce_list = []
		for i in range(len(cards)-2):
			if int(cards[i].value) == int(cards[i+1].value) - 1:
				if int(cards[i+1].value) == int(cards[i+2].value) - 1:
					if cards[i].paint == cards[i+1].paint and cards[i+1].paint == cards[i+2].paint:
						tierce_list.append([str('Tierce'),str(cards[i].paint),str(cards[i+2].value)])

		return tierce_list

	def check_if_there_is_quarte(cards):
		quarte_list = []
		for i in range(len(cards)-3):
			if int(cards[i].value) == int(cards[i+1].value) - 1:
				if int(cards[i+1].value) == int(cards[i+2].value) - 1:
					if int(cards[i+2].value) == int(cards[i+3].value) - 1:
						if cards[i].paint == cards[i+1].paint and cards[i+1].paint == cards[i+2].paint and cards[i+2].paint == cards[i+3].paint :
							quarte_list.append([str('Quarte'),str(cards[i].paint),str(cards[i+3].value)])

		return quarte_list

	def check_if_there_is_quinte(cards):
		quinte_list = []
		for i in range(len(cards)-4):
			if int(cards[i].value) == int(cards[i+1].value) - 1:
				if int(cards[i+1].value) == int(cards[i+2].value) - 1:
					if int(cards[i+2].value) == int(cards[i+3].value) - 1:
						if int(cards[i+3].value) == int(cards[i+4].value) - 1:
							if cards[i].paint == cards[i+1].paint and cards[i+1].paint == cards[i+2].paint and cards[i+2].paint == cards[i+3].paint and cards[i+3].paint == cards[i+4].paint:
								quinte_list.append([str('Quinte'),str(cards[i].paint),str(cards[i+4].value)])

		return quinte_list	

	#helper function
	def count_cards_value(cards, value):
		count = 0
		for c in cards:
			if c.value == value:
				count += 1
		return count

	def check_if_there_is_carre(cards):
		carre_list = []
		d={}
		for card in cards:
			if card.value not in d:
				x = Utls.count_cards_value(cards, card.value)
				d.update({card.value: x})

		for key, value in d.items():
			if value == 4:
				k = key
				carre_list.append(['Carre', str(key)])

		return carre_list
		

class Jsonable:

	def to_json(self):
		pass

if __name__ == '__main__':
	main()