import unittest

from utls import Utls, Card, Person, Team, Jsonable
from game import Game
from pprint import pprint
import json

class TestCardClass(unittest.TestCase):
    def test_card_string_representation_is_as_expected_one(self):
        card = Card('7', 'D')
        card1 = Card('K', 'S')


        self.assertEqual(str(card),'(7,D)')
        self.assertEqual(str(card1),'(K,S)')

    def test_cards_comparison_less_than_works_correctly_for_numbers_cards(self):

        card = Card('7', 'D')
        card1 = Card('8', 'S')
        
        result = card < card1

        self.assertEqual(result, True)

    def test_cards_comparison_less_than_works_correctly_for_non_numbers_cards(self):

        card = Card('Q', 'D')
        card1 = Card('K', 'S')

        result = card < card1

        self.assertEqual(result, True)

    def test_cards_comparison_less_than_works_correctly_for_number_and_non_number_cards(self):

        card = Card('8', 'D')
        card1 = Card('J', 'S')

        result = card < card1
        opposite_result = card1 < card

        self.assertEqual(result, True)
        self.assertEqual(opposite_result, False)

    def test_comparison_greater_than_works_correctly_for_numbers_cards(self):
        
        card = Card('9', 'D')
        card1 = Card('7', 'S')

        result = card > card1

        self.assertEqual(result, True)


    def test_cards_comparison_greater_than_works_correctly_for_non_numbers_cards(self):

        card = Card('K', 'D')
        card1 = Card('J', 'S')
        result = card > card1

        self.assertEqual(result, True)


    def test_cards_comparison_greater_than_works_correctly_for_number_and_non_number_cards(self):

        card = Card('J', 'D')
        card1 = Card('9', 'S')

        result = card > card1
        opposite_result = card1 > card

        self.assertEqual(result, True)
        self.assertEqual(opposite_result, False)

    def test_cards_comparison_less_or_equal_works_correctly_for_numbers_cards_with_equal_cards(self):

        card = Card('7', 'D')
        card1 = Card('7', 'S')
        
        result = card <= card1

        self.assertEqual(result, True)

    def test_cards_comparison_less_or_equal_works_correctly_for_non_numbers_cards_with_equal_cards(self):

        card = Card('Q', 'D')
        card1 = Card('Q', 'S')

        result = card <= card1

        self.assertEqual(result, True)


    def test_cards_comparison_greater_or_equal_works_correctly_for_numbers_cards_with_equal_cards(self):

        card = Card('7', 'D')
        card1 = Card('7', 'S')
        
        result = card >= card1

        self.assertEqual(result, True)

    def test_cards_comparison_greater_or_equal_works_correctly_for_non_numbers_cards_with_equal_cards(self):

        card = Card('Q', 'D')
        card1 = Card('Q', 'S')

        result = card >= card1

        self.assertEqual(result, True)

    def test_cards_comparison_less_or_equal_works_correctly_for_numbers_cards_with_non_equal_cards(self):

        card = Card('7', 'D')
        card1 = Card('8', 'S')
        
        result = card <= card1

        self.assertEqual(result, True)

    def test_cards_comparison_less_or_equal_works_correctly_for_non_numbers_cards_with_non_equal_cards(self):

        card = Card('T', 'D')
        card1 = Card('J', 'S')
        result = card <= card1

        self.assertEqual(result, True)


    def test_cards_comparison_greater_or_equal_works_correctly_for_numbers_cards_with_non_equal_cards(self):

        card = Card('9', 'D')
        card1 = Card('7', 'S')
        
        result = card >= card1

        self.assertEqual(result, True)

    def test_cards_comparison_greater_or_equal_works_correctly_for_non_numbers_cards_with_non_equal_cards(self):

        card = Card('K', 'D')
        card1 = Card('Q', 'S')

        result = card >= card1

        self.assertEqual(result, True)



class TestPersonClass(unittest.TestCase):
    def test_class_Person_instantiates_name_correctly(self):
        exception = None

        try:
            person = Person(123)
        except Exception as err:
            exception = err

        self.assertIsNotNone(exception)
        self.assertEqual(str(exception), 'Name must be string')


class TestTeamClass(unittest.TestCase):
    def test_validating_names_are_string_not_integer(self):
        exception = None

        try:
            person = Team(123, (Person('Ivan'), Person('Gosho')))
            person1 = Team('name', (Person(123), Person('Gosho')))
            person1 = Team('name', (Person('Ivan'), Person(123)))
        except Exception as err:
            exception = err

        self.assertIsNotNone(exception)
        self.assertEqual(str(exception), 'Name must be string')



    def test_teams_string_representation_is_as_expected(self):
        team = Team('Malinka', (Person('Ivan'), Person('Gosho')))
        team2 = Team('Yagodka', (Person('Pesho'), Person('Tosho')))

        self.assertEqual(str(team), 'Teamname: Malinka, teammates: Ivan, Gosho')
        self.assertEqual(str(team2), 'Teamname: Yagodka, teammates: Pesho, Tosho')


class TestUtlsClass(unittest.TestCase):
    def test_shuffle_function_should_return_shuffled_list_of_Card(self):
        cards = [Card(value,paint) for value in [val for val in '789TJQKA'] for paint in [p for p in 'CDHS']]

        shuffled_cards = Utls.shuffle()
        
        self.assertIsNotNone(shuffled_cards)
        self.assertNotEqual(cards, shuffled_cards)

    def test_draw_cards_function_should_draw_Cards_to_teammates(self):
        cards = Utls.shuffle()

        team1 = Team('Malinka', (Person('Ivan'), Person('Gosho')))
        team2 = Team('Yagodka', (Person('Pesho'), Person('Tosho')))

        Utls.draw_cards(team1, team2)

        first_teammate_team1_cards = cards[:8]
        first_teammate_team2_cards = cards[8:16]
        second_teammate_team1_cards = cards[16:24]
        second_teammate_team2_cards = cards[24:]

        self.assertEqual(len(team1.teammates[0].cards), len(first_teammate_team1_cards))
        self.assertEqual(len(team2.teammates[0].cards), len(first_teammate_team2_cards))
        self.assertEqual(len(team1.teammates[1].cards), len(second_teammate_team1_cards))
        self.assertEqual(len(team2.teammates[1].cards), len(second_teammate_team2_cards))


    def test_sorting_cards_should_returns_sorted_list_of_cards(self):
        team1 = Team('Malinka', (Person('Ivan'), Person('Gosho')))

        team1.teammates[0].cards = [Card('9','D'), Card('J','C'),Card('K', 'S'), Card('Q', 'S'),Card('A','H') , Card('7','D'), Card('J','H'), Card('8','C')]

        result = Utls.sort_cards(team1.teammates[0].cards)

        self.assertEqual(str(result), '[8 ♣, 11 ♣, 7 ♦, 9 ♦, 11 ♥, 14 ♥, 12 ♠, 13 ♠]')

    def test_checking_for_belote_function_should_return_list_of_belotes(self):
        team1 = Team('Malinka', (Person('Ivan'), Person('Gosho')))

        team1.teammates[0].cards = [Card('9','D'),Card('Q','D'),Card('K','D') ,Card('Q','C'),Card('K', 'S'), Card('Q', 'S'),Card('A','H') , Card('7','D'), Card('J','H'), Card('8','C')]

        sorted_list = Utls.sort_cards(team1.teammates[0].cards)

        belote_list = Utls.check_if_there_is_belote(sorted_list)

        self.assertEqual(belote_list, [['Belote','D'],['Belote','S']])

    def test_checking_function_if_there_is_tierce_in_the_cards_should_return_list_of_tierces(self):
        team1 = Team('Malinka', (Person('Ivan'), Person('Gosho')))

        team1.teammates[0].cards = [Card('9','D'),Card('Q','D'),Card('K','D') ,Card('Q','C'),Card('8','D'),Card('J', 'D'), Card('Q', 'S'),Card('A','H') , Card('7','D'), Card('J','H'), Card('8','C')]

        sorted_list = Utls.sort_cards(team1.teammates[0].cards)

        tierce_list = Utls.check_if_there_is_tierce(sorted_list)

        self.assertEqual(tierce_list, [['Tierce','D','9'],['Tierce','D', '13']])

    def test_checking_function_if_there_is_quarte_in_the_cards_should_return_list_of_quartes(self):
        team1 = Team('Malinka', (Person('Ivan'), Person('Gosho')))

        team1.teammates[0].cards = [Card('9','D'),Card('Q','D'),Card('K','D'), Card('T', 'D') ,Card('Q','C'),Card('8','D'),Card('K', 'S'), Card('Q', 'S'),Card('A','H') , Card('7','D'), Card('J','H'), Card('8','C')]

        sorted_list = Utls.sort_cards(team1.teammates[0].cards)

        quarte_list = Utls.check_if_there_is_quarte(sorted_list)

        self.assertEqual(quarte_list, [['Quarte','D','10']])

    def test_checking_function_if_there_is_quinte_in_the_cards_should_return_list_of_quintes(self):
        team1 = Team('Malinka', (Person('Ivan'), Person('Gosho')))

        team1.teammates[0].cards = [Card('9','D'),Card('Q','D'),Card('K','D'), Card('T', 'D') ,Card('Q','C'),Card('J', 'D'),Card('8','D'),Card('K', 'S'), Card('Q', 'S'),Card('A','H') , Card('7','D'), Card('J','H'), Card('8','C')]

        sorted_list = Utls.sort_cards(team1.teammates[0].cards)

        quinte_list = Utls.check_if_there_is_quinte(sorted_list)

        self.assertEqual(quinte_list, ['Quinte','D','13'])

    def test_checking_if_there_is_carre_in_the_cards_should_return_list_of_carres(self):
        team1 = Team('Malinka', (Person('Ivan'), Person('Gosho')))

        team1.teammates[0].cards = [Card('9','C'), Card('9','D'), Card('9','H'), Card('9','S'), Card('7','S'), Card('7','D')]

        sorted_list = Utls.sort_cards(team1.teammates[0].cards)

        carres_list = Utls.check_if_there_is_carre(sorted_list)

        self.assertEqual(carres_list, [['Carre','9']])
    
class TestPersonClass(unittest.TestCase):
    pass

class TestTeamClass(unittest.TestCase):
    pass

class TestUtlsClass(unittest.TestCase):
    def test_shuffle_function_should_return_shuffled_list_of_Card(self):
        cards = [Card(value,paint) for value in [val for val in '79TJQKA'] for paint in [p for p in 'CDHS']]

        shuffled_cards = Utls.shuffle()
        
        self.assertIsNotNone(shuffled_cards)
        self.assertNotEqual(cards, shuffled_cards)

    def test_write_result_and_have_winner(self):
        game = Game()
        game.team1 = Team('team1', (Person('p1'), Person('p2')))
        game.team2 = Team('team2', (Person('p3'), Person('p4')))
        game.round = 0

        game.team1.points = 40
        game.team2.points = 20

        game.write_result()

        game.round += 1

        game.team1.new_points = 20
        game.team2.new_points = 0
        game.write_result()

        game.has_winner = True
        game.team1.wins = 1
        game.team2.wins = 0
        game.write_result()


class TestJsonableClass(unittest.TestCase):
    def test_add_to_json_with_1_round_only_returns_new_dict(self):
        game = Game()
        team1 = Team('team1', (Person('p1'), Person('p2')))
        team2 = Team('team2', (Person('p3'), Person('p4')))
        team1.teammates[0].cards = [Card(value, 'C') for value in [val for val in '789TJQKA']]
        team1.teammates[1].cards = [Card(value, 'D') for value in [val for val in '789TJQKA']]
        team2.teammates[0].cards = [Card(value, 'H') for value in [val for val in '789TJQKA']]
        team2.teammates[1].cards = [Card(value, 'S') for value in [val for val in '789TJQKA']]
        game.team1 = team1
        game.team2 = team2
        teams = (team1, team2)

        game.json_history = game.add_to_json()
        expected = {}
        expected['game 1:'] = {'round 1:': {}}
        for i in range(2):
            expected['game 1:']['round 1:'][teams[i].name] = {}
            for j in range(2):
                team = teams[i]
                p = team.teammates[j]
                expected['game 1:']['round 1:'][team.name][p.name] = {}
                expected['game 1:']['round 1:'][team.name][p.name]['cards'] = p.cards
                expected['game 1:']['round 1:'][team.name][p.name]['announcements'] = p.announcements
                expected['game 1:']['round 1:'][team.name][p.name]['points'] = p.points

        self.maxDiff = None
        self.assertEqual(game.json_history, expected)

    def test_add_to_json_with_more_rounds_returns_dict_with_both_new_and_old_data(self):
        game = Game()
        team1 = Team('team1', (Person('p1'), Person('p2')))
        team2 = Team('team2', (Person('p3'), Person('p4')))
        round_ = 0
        expected = {}

        for i in range(2):
            team1.teammates[0].cards = [Card(value, 'C') for value in [val for val in '789TJQKA']]
            team1.teammates[1].cards = [Card(value, 'D') for value in [val for val in '789TJQKA']]
            team2.teammates[0].cards = [Card(value, 'H') for value in [val for val in '789TJQKA']]
            team2.teammates[1].cards = [Card(value, 'S') for value in [val for val in '789TJQKA']]
            game.team1 = team1
            game.team2 = team2
            teams = (team1, team2)

            game.json_history = game.add_to_json()
            expected['game 1:'] = {f'round {round_}:': {}}
            for i in range(2):
                expected['game 1:'][f'round {round_}:'][teams[i].name] = {}
                for j in range(2):
                    team = teams[i]
                    p = team.teammates[j]
                    expected['game 1:'][f'round {round_}:'][team.name][p.name] = {}
                    expected['game 1:'][f'round {round_}:'][team.name][p.name] = {
                        'cards': p.cards,
                        'announcements': p.announcements,
                        'points': p.points
                    }
            round_ += 1

        #self.maxDiff = None
        self.assertEqual(expected, game.json_history)

    def test_to_json_function_returns_in_json_format(self):
        game = Game()
        team1 = Team('team1', (Person('p1'), Person('p2')))
        team2 = Team('team2', (Person('p3'), Person('p4')))
        team1.teammates[0].cards = [Card(value, 'C') for value in [val for val in '789TJQKA']]
        team1.teammates[1].cards = [Card(value, 'D') for value in [val for val in '789TJQKA']]
        team2.teammates[0].cards = [Card(value, 'H') for value in [val for val in '789TJQKA']]
        team2.teammates[1].cards = [Card(value, 'S') for value in [val for val in '789TJQKA']]
        game.team1 = team1
        game.team2 = team2
        teams = (team1, team2)
        game.json_history = game.add_to_json()

        result = game.to_json()
        expected = json.dumps(game.json_history, indent=4)

        self.assertEqual(result, expected)
    
    def test_game_write_json_creates_file_data_json(self):
        game = Game()
        team1 = Team('team1', (Person('p1'), Person('p2')))
        team2 = Team('team2', (Person('p3'), Person('p4')))
        round_ = 0
        expected = {}

        for i in range(2):
            team1.teammates[0].cards = [Card(value, 'C') for value in [val for val in '789TJQKA']]
            team1.teammates[1].cards = [Card(value, 'D') for value in [val for val in '789TJQKA']]
            team2.teammates[0].cards = [Card(value, 'H') for value in [val for val in '789TJQKA']]
            team2.teammates[1].cards = [Card(value, 'S') for value in [val for val in '789TJQKA']]
            game.team1 = team1
            game.team2 = team2
            teams = (team1, team2)

            game.json_history = game.add_to_json()
            expected['game 1:'] = {f'round {round_}:': {}}
            for i in range(2):
                expected['game 1:'][f'round {round_}:'][teams[i].name] = {}
                for j in range(2):
                    team = teams[i]
                    p = team.teammates[j]
                    expected['game 1:'][f'round {round_}:'][team.name][p.name] = {}
                    expected['game 1:'][f'round {round_}:'][team.name][p.name] = {
                        'cards': p.cards,
                        'announcements': p.announcements,
                        'points': p.points
                    }
            game.jsoned = game.to_json()
            game.write_json()
            round_ += 1

        #self.maxDiff = None
        #self.assertEqual(expected, game.json_history)

if __name__ == '__main__':
    unittest.main()