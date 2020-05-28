from random import choice
from exceptions import ClubNotSetException


class Player:
    def __init__(self, name, position, age):
        self._name = name
        self._age = age
        self._position = position
        self._goals = 0
        self._club = None
        self._jersey_number = 0
        self._number_of_cards = 0

    def get_name(self):
        return self._name

    def set_name(self, value):
        self._name = value

    def get_age(self):
        return self._age

    def set_age(self, value):
        self._age = value

    def get_goals(self):
        return self._goals

    def get_jersey_number(self):
        return self._jersey_number

    def set_jersey_number(self, value):
        self._jersey_number = value

    def get_number_of_cards(self):
        return self._number_of_cards

    def get_club(self):
        return self._club

    def get_position(self):
        return self._position

    def score(self):
        if self._club is not None:
            self._goals += 1
        else:
            raise ClubNotSetException('Choose your club!')

    def change_position(self, new_position):
        self._position = new_position
        self._age += 2

    def transfer(self, club):
        self._club = club
        self._goals = 0

    def foul(self):
        if choice([0, 1]):
            self._number_of_cards += 1
            #print('Got a card!')


my_player = Player('Test Player', 'defender', 23)
print(my_player.get_age())
print(my_player.get_goals())
try:
    my_player.score()
except:
    my_player.transfer('Liverpool FC')
my_player.set_jersey_number(7)
my_player.score()
print(my_player.get_goals())
my_player.change_position('attacker')
print(my_player.get_age())
print(my_player.get_position())
my_player.foul()
my_player.foul()
my_player.foul()
my_player.foul()
print(my_player.get_number_of_cards())
my_player.transfer('FC Barcelona')
print(my_player.get_goals())
