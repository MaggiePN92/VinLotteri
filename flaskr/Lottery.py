from flaskr.Player import Player
import random

class Lottery:
    def __init__(self):
        self.list_of_players   = []
        self.total_tickets     = 0
        self.lottery_dict      = {}

    def handle_form_data(self, immutable_multi_dict):
        '''
        Reads and adds player name and tickets to lottery.
        The dict is used for data_table.html.
        :param immutable_multi_dict:
        '''
        form_dict = immutable_multi_dict.to_dict()
        #print(form_dict)
        for i in range(1,7):
            name       = form_dict.get("Navn"+str(i))
            if name == '': break
            nr_tickets = int(form_dict.get("lodd"+str(i)))
            self._add_player_to_lottery(name, nr_tickets)
            self._add_to_lottery_dict(name,nr_tickets)

    def _add_player_to_lottery(self, name, nr_tickets):
        new_player       = Player(name, nr_tickets, self.total_tickets)
        self.list_of_players.append(new_player)
        self.total_tickets += nr_tickets

    def _read_form_dict(self, immutable_multi_dict):
        form_dict  = immutable_multi_dict.to_dict()
        name       = form_dict['Navn']
        nr_tickets = form_dict['Antall lodd']
        return name, nr_tickets

    def _find_winner(self, winning_ticket:int)->str:
        for player in self.list_of_players:
            if player.has_won(winning_ticket):
                return player.get_name()

    def _pick_winning_ticket(self)->int:
        winning_ticket = random.randint(1, self.total_tickets)
        return winning_ticket

    def pick_winner(self):
        winning_ticket = self._pick_winning_ticket()
        winning_player = self._find_winner(winning_ticket)
        return winning_player

    def display_players_w_tickets(self):
        for player in self.list_of_players:
            print(player.get_name(),"har loddene:", player.get_player_tickets())

    def get_list_of_players(self):
        return self.list_of_players

    def _add_to_lottery_dict(self, name_of_player, tickets):
        self.lottery_dict.update({name_of_player : tickets})

    def get_lottery_dict(self):
        return self.lottery_dict