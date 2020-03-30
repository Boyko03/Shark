import unittest
from game import Card, Person, Team, Game, Utls
import random

class TestGameClass(unittest.TestCase):
    def test_random_choice_of_contracts(self):
        contracts = ['clubs', 'diamonds', 'hearts', 'spides', 'no trumps','all trumps']
        result = random.choice(contracts)

        self.assertIsNotNone(result)

    def test_checking_if_belote_is_possible_works_correctly(self):

        belote = Game.check_if_belote_is_possible('all trumps', 'C')
        belote1 = Game.check_if_belote_is_possible('D', 'D')
        belote2 = Game.check_if_belote_is_possible('S', 'H')
        belote3 = Game.check_if_belote_is_possible('no trumps','S')

        self.assertTrue(belote)
        self.assertTrue(belote1)
        self.assertFalse(belote2)
        self.assertFalse(belote3)

    def test_rotating_order_of_players_works_correctly(self):
        team1 = Team('Malinka', (Person('Ivan'), Person('Gosho')))
        team2 = Team('Yagodka', (Person('Pesho'), Person('Tosho')))

        players_order = [team1.teammates[0], team2.teammates[0], team1.teammates[1], team2.teammates[1]]

        result = Game.rotate_players_order(players_order)

        self.assertEqual(result, [team2.teammates[0], team1.teammates[1], team2.teammates[1], team1.teammates[0]])

        result2 = Game.rotate_players_order(result)

        self.assertEqual(result2,[team1.teammates[1], team2.teammates[1], team1.teammates[0], team2.teammates[0]])

    def test_check_carres_points_function_should_return_points_of_carre(self):
        carre = ['Carre','A']
        carre2 = ['Carre','9']
        carre3 = ['Carre','11'] #J

        result = Game.check_carres_points(carre)
        result2 = Game.check_carres_points(carre2)
        result3 = Game.check_carres_points(carre3)

        self.assertEqual(result, 100)
        self.assertEqual(result2, 150)
        self.assertEqual(result3, 200)


    def test_announcements_list_of_player_returns_expected_consecutive_cards_and_belotes(self):
        team1 = Team('Malinka', (Person('Ivan'), Person('Gosho')))
        team2 = Team('Yagodka', (Person('Pesho'), Person('Tosho')))
        team3 = Team('Kapinka', (Person('Panda'), Person('Panda2')))

        team1.teammates[0].cards = [Card('K','S'), Card('Q','S'), Card('J','S'), Card('A', 'S')] #quarte and belot
        team1.teammates[0].cards = Utls.sort_cards(team1.teammates[0].cards)

        team1.teammates[1].cards = [Card('K','S'), Card('Q','S'), Card('J','S'), Card('A', 'S'), Card('T','S')]
        team1.teammates[1].cards = Utls.sort_cards(team1.teammates[1].cards)

        team2.teammates[0].cards = [Card('K','S'), Card('Q','S'), Card('J','S'), Card('A', 'S'), Card('T','S'), Card('9','S')]
        team2.teammates[0].cards = Utls.sort_cards(team2.teammates[0].cards)

        team2.teammates[1].cards = [Card('K','S'), Card('Q','S'), Card('J','S'), Card('A','S'), Card('7','S'), Card('8','S'), Card('9','S')]
        team2.teammates[1].cards = Utls.sort_cards(team2.teammates[1].cards)

        team3.teammates[0].cards = [Card('K','S'), Card('Q','S'), Card('J','S'), Card('A', 'S'), Card('7','D'),Card('8','D'), Card('9','D'),Card('T','D')]
        team3.teammates[0].cards = Utls.sort_cards(team3.teammates[0].cards)

        team3.teammates[1].cards = [Card('K','S'), Card('Q','S'), Card('J','S'), Card('A','S'), Card('9','S'), Card('9','D'), Card('9','H'), Card('9','C')]
        team3.teammates[1].cards = Utls.sort_cards(team3.teammates[1].cards)

        result = Game.take_player_annoucements(team1.teammates[0])
        result2 = Game.take_player_annoucements(team1.teammates[1])
        result3 = Game.take_player_annoucements(team2.teammates[0])
        result4 = Game.take_player_annoucements(team2.teammates[1])
        result5 = Game.take_player_annoucements(team3.teammates[0])
        result6 = Game.take_player_annoucements(team3.teammates[1])


        self.assertEqual(result, [['Quarte','S','14'],['Belote', 'S']])
        self.assertEqual(result2, [['Quinte','S','14'],['Belote', 'S']])
        self.assertEqual(result3, [['Quinte','S','14'],['Belote', 'S']])
        self.assertEqual(result4, [['Quarte','S','14'],['Tierce','S','9'],['Belote', 'S']])
        self.assertEqual(result5, [['Quarte','D','10'],['Quarte','S','14'],['Belote', 'S']])
        self.assertEqual(result6, [['Carre','9'], ['Quarte', 'S', '14'], ['Belote', 'S']])

    def test_check_consecutive_cards_points_function_returns_correct_points(self):
        announcement = ['Tierce', 'S', '9']
        announcement2 = ['Quarte', 'D', '10']
        announcement3 = ['Quinte', 'H', 'A']
        announcement4 = ['Carre', '9']

        result = Game.check_consecutive_cards_points(announcement)
        result2 = Game.check_consecutive_cards_points(announcement2)
        result3 = Game.check_consecutive_cards_points(announcement3)
        result4 = Game.check_consecutive_cards_points(announcement4)

        self.assertEqual(result, 20)
        self.assertEqual(result2, 50)
        self.assertEqual(result3, 100)
        self.assertEqual(result4, 150)

    def test_get_player_announcements_point_function_should_return_addition_of_announcements_points(self):
        team2 = Team('Yagodka', (Person('Pesho'), Person('Tosho')))

        team2.teammates[1].cards = [Card('K','S'), Card('Q','S'), Card('J','S'), Card('A','S'), Card('7','S'), Card('8','S'), Card('9','S')]
        team2.teammates[1].cards = Utls.sort_cards(team2.teammates[1].cards)

        contracts = 'all trumps'

        result = Game.get_player_announcements_ploints(contracts, team2.teammates[1])

        contracts = 'no trumps'

        result2 = Game.get_player_announcements_ploints(contracts, team2.teammates[1])

        contracts = 'S'

        result3 = Game.get_player_announcements_ploints(contracts, team2.teammates[1])

        contracts = 'H'

        result4 = Game.get_player_announcements_ploints(contracts, team2.teammates[1])

        self.assertEqual(result, 90)
        self.assertEqual(result2, 0)
        self.assertEqual(result3, 90)
        self.assertEqual(result4, 70)


if __name__ == '__main__':
    unittest.main()