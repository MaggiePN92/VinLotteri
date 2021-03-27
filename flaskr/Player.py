class Player:
    def __init__(self, name:str, nr_tickets:int, total_tickets:int):
        self.name            = name
        self.list_of_tickets = self._make_list_of_tickets(nr_tickets, total_tickets)

    def _make_list_of_tickets(self, nr_tickets:int, total_tickets:int)->list:
        list_of_tickets = list(
            range(
                total_tickets + 1,
                total_tickets + 1 + nr_tickets
            )
        )
        return list_of_tickets

    def get_player_tickets(self):
        return self.list_of_tickets

    def has_won(self, winning_ticket:int):
        if winning_ticket in self.list_of_tickets:
            return True

    def get_name(self):
        return self.name