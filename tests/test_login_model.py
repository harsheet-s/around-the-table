import pytest

from model.login_model import LoginModel
from model.player import Player


def test_a_new_game_has_no_players():
    assert LoginModel().get_players() == []


def test_players_are_added_in_order():
    model = LoginModel()
    model.add_to_game(Player("Davey"))
    model.add_to_game(Player("Jenny"))

    assert [p.get_name() for p in model.get_players()] == ["Davey", "Jenny"]


def test_the_maximum_number_of_players_is_accepted():
    model = LoginModel()
    for i in range(LoginModel.MAX_PLAYERS):
        model.add_to_game(Player(f"Player {i + 1}"))

    assert len(model.get_players()) == LoginModel.MAX_PLAYERS


def test_adding_beyond_the_maximum_is_rejected():
    model = LoginModel()
    for i in range(LoginModel.MAX_PLAYERS):
        model.add_to_game(Player(f"Player {i + 1}"))

    with pytest.raises(RuntimeError):
        model.add_to_game(Player("One Too Many"))
