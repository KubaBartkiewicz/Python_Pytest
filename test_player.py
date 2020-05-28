import pytest
from player_file import Player
from exceptions import ClubNotSetException
import random


@pytest.fixture
def player():
    age = random.randint(20, 41)
    name = random.choice(['Zbigniew Boniek', 'Michael Platini', 'Maradona', 'Pele'])
    position = random.choice(['goalkeeper', 'defender', 'midfielder', 'striker'])
    return Player(name, position, age)


@pytest.fixture
def player_with_club(player):
    player.transfer('Juventus')
    return player


def test_new_player(player):
    assert player.get_goals() == 0, 'At the beginning player should have 0 goals'
    assert player.get_club() is None


def test_player_scoring(player_with_club):
    player_with_club.score()
    assert player_with_club.get_goals() == 1, 'After one goal, number of goals is not 1'


def test_player_scoring_with_no_club(player):
    with pytest.raises(ClubNotSetException, match='Choose your club'):
        player.score()


def test_test_player_position(player):
    player.change_position('striker')
    assert player.get_position() == 'striker', 'player position should be striker'


def test_player_change_position_age(player):
    expected_age = player.get_age() + 2
    player.change_position('striker')
    assert player.get_age() == expected_age, 'player age is incorrect'


def test_player_transfer(player):
    player.transfer('Milan')
    assert player.get_club() == 'Milan', 'player club is incorrect'


def test_player_score_after_transfer(player_with_club):
    player_with_club.score()
    player_with_club.transfer('Milan')
    assert player_with_club.get_goals() == 0, 'number of goals is incorrect'


def test_player_cards(player):
    for i in range(100): player.foul()
    assert 60 >= player.get_number_of_cards() >= 40, 'Number of cards is incorrect'
