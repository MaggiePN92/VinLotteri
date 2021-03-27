import random
import time

class Lotteri:

    def __init__(self):
        self.deltaker_dict    = {}
        self.antall_deltakere = 0
        self.sum_lodd         = 0
        self.brukte_lodd      = []
        self.spill()

    def spill(self):
        while True:
            state = self.get_meny()
            self.tolk_feedback(state)

    def tolk_feedback(self, state):
        if state.lower() == "x":
            print("Takk for nå.")
            quit()
        #add more players
        elif state == "1":
            deltaker, lodd_list = self.add_deltaker()
            self.deltaker_dict[deltaker] = lodd_list
            self.legg_til_flere()
        #pick winner
        elif state == "2":
            self.trekk_vinner()
        #print spillere
        elif state == '3':
            self.get_dict()
        #fjern spiller
        elif state == '4':
            self.fjern_spiller()
        #catch all statement
        else:
            print("Skjønte ikke kommando, prøv på nytt.")
        self.spill()

    def get_meny(self):
        return  input("""
        **MENY**
        Trykk 1 for å legge til spiller
        Trykk 2 for å trekke vinner
        Trykk 3 for å se oversikt over lodd
        Trykk 4 for å fjerne spiller
        Trykk X for å avslutte
        """)

    def add_to_dict(self, deltaker, lodd_list):
        self.deltaker_dict[deltaker] = lodd_list

    def legg_til_flere(self):
        while True:
            self.state = input("Ønsker du å legge til flere deltakere?").lower()
            if self.state != 'ja':
                break
            else:
                deltaker, lodd_list = self.add_deltaker()
                self.add_to_dict(deltaker,lodd_list)

    def spiller_input(self):
        deltaker = input("Deltakernavn: ")
        ant_lodd = input("Antall lodd:")
        ant_lodd = int(ant_lodd)
        return deltaker, ant_lodd

    def make_lodd_list(self, ant_lodd):
        lodd_list = list(
            range(
                self.sum_lodd + 1,
                ant_lodd + 1 + self.sum_lodd
            )
        )
        return lodd_list

    def add_deltaker(self):
        deltaker, ant_lodd = self.spiller_input()
        lodd_list = self.make_lodd_list(ant_lodd)

        self.one_plus_ant_deltakere()
        self.n_pluss_ant_lodd(ant_lodd)

        return deltaker, lodd_list

    def get_dict(self):
        for k,v in self.deltaker_dict.items():
            print(k.capitalize(), " sine lodd er følgende: ", v, ".", sep="")

    def velg_tall(self):
        self.trukket_tall = random.randint(1,self.sum_lodd)
        if self.is_brukt(self.trukket_tall):
            self.trukket_tall = self.velg_tall()
        else: print("Lodd nummer", self.trukket_tall, "ble trukket.")
        return self.trukket_tall

    def is_brukt(self,tall):
        if tall in self.brukte_lodd:return True

    def trekk_vinner(self):
        self.trukket_tall = self.velg_tall()
        for deltaker, liste in self.deltaker_dict.items():
            if self.trukket_tall in liste:
                print(deltaker.capitalize(),"har vunnet! Gratulerer!!")
                self.fjern_lodd(self.trukket_tall)
                time.sleep(3)

    def fjern_spiller(self):
        hvilken_spiller = input("Hvilken spiller ønsker du å fjerne: ")
        if hvilken_spiller in self.deltaker_dict:self.deltaker_dict.pop(hvilken_spiller)
        else:print("Spiller er ikke registrert i loddtrekningen.")

    def one_plus_ant_deltakere(self):
        self.antall_deltakere += 1

    def n_pluss_ant_lodd(self, ant_lodd):
        self.sum_lodd += ant_lodd

    def fjern_lodd(self, lodd_nr):
        for k,v in self.deltaker_dict.items():
            if lodd_nr in v:
                self.deltaker_dict[k].remove(lodd_nr)
                self.brukte_lodd.append(lodd_nr)


