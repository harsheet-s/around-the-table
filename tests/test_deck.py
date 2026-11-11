from model.card import Card
from model.card_library import CardLibrary
from model.deck import Deck
from model.weapon_style import WeaponStyle


def test_deck_is_built_to_the_requested_size():
    assert len(Deck(16).get_cards()) == 16
    assert len(Deck(6).get_cards()) == 6


def test_has_enough_is_true_up_to_the_card_count():
    deck = Deck(6)
    assert deck.has_enough(1) is True
    assert deck.has_enough(6) is True
    assert deck.has_enough(7) is False


def test_remove_card_returns_a_card_and_shrinks_the_deck():
    deck = Deck(6)
    card = deck.remove_card()
    assert isinstance(card, Card)
    assert len(deck.get_cards()) == 5


def test_deck_can_be_emptied_and_then_reports_no_cards():
    deck = Deck(6)
    for _ in range(6):
        deck.remove_card()
    assert deck.get_cards() == []
    assert deck.has_enough(1) is False


def test_deck_holds_copies_so_damage_does_not_reach_the_library():
    deck = Deck(16)
    deck.get_cards()[0].apply_damage(Card("Shutdown", 100, WeaponStyle.FURY))

    assert deck.get_cards()[0].get_health() <= 0
    assert CardLibrary.ALL_CARDS[0].get_health() == 100


def test_two_decks_do_not_share_card_objects():
    first = Deck(6)
    second = Deck(6)
    first.get_cards()[0].apply_damage(Card("Showdown", 60, WeaponStyle.FURY))

    assert second.get_cards()[0].get_health() == 100
