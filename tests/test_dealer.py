import pytest

from model.card import Card
from model.dealer import Dealer
from model.exception.empty_deck_exception import EmptyDeckException
from model.exception.round_not_ready_exception import RoundNotReadyException
from model.player import Player
from model.weapon_style import WeaponStyle


def players(count=2):
    return [Player(f"Player {i + 1}") for i in range(count)]


def test_dealer_builds_both_decks():
    dealer = Dealer(players())
    assert len(dealer.get_main_deck().get_cards()) == 16
    assert len(dealer.get_secondary_deck().get_cards()) == 6


def test_every_player_receives_cards_on_a_deal():
    group = players(3)
    Dealer(group).deal()

    for player in group:
        assert len(player.get_temp_hand()) >= 1


def test_the_secondary_card_rotates_through_the_players():
    group = players(3)
    dealer = Dealer(group)

    dealer.deal()
    assert len(group[0].get_temp_hand()) == 2
    assert len(group[1].get_temp_hand()) == 1

    dealer.deal()
    assert len(group[1].get_temp_hand()) == 2
    assert len(group[0].get_temp_hand()) == 1


def test_dealing_from_an_empty_main_deck_raises_empty_deck_exception():
    dealer = Dealer(players(2))
    main = dealer.get_main_deck()
    while main.has_enough(2):
        main.remove_card()

    with pytest.raises(EmptyDeckException):
        dealer.deal()


def test_dealing_from_an_empty_secondary_deck_raises_empty_deck_exception():
    dealer = Dealer(players(2))
    secondary = dealer.get_secondary_deck()
    while secondary.has_enough(1):
        secondary.remove_card()

    with pytest.raises(EmptyDeckException):
        dealer.deal()


def test_every_player_selected_is_false_until_all_have_chosen():
    group = players(2)
    dealer = Dealer(group)

    assert dealer.every_player_selected() is False

    group[0].select(Card("Icicle", 10, WeaponStyle.ICE))
    assert dealer.every_player_selected() is False

    group[1].select(Card("Iceberg", 15, WeaponStyle.ICE))
    assert dealer.every_player_selected() is True


def test_playing_before_everyone_has_selected_raises_round_not_ready():
    dealer = Dealer(players(2))

    with pytest.raises(RoundNotReadyException):
        dealer.play()


def test_a_played_round_clears_every_selection():
    group = players(3)
    dealer = Dealer(group)
    dealer.deal()

    for player in group:
        player.select(Card("Spitfire", 25, WeaponStyle.HEAT))

    dealer.play()

    for player in group:
        assert player.has_selected() is False
