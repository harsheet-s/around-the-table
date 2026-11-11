import pytest

from model.card import Card
from model.exception.full_hand_exception import FullHandException
from model.player import Player
from model.weapon_style import WeaponStyle


def card(name="Icicle", attack=10, style=WeaponStyle.ICE):
    return Card(name, attack, style)


def test_a_new_player_starts_empty():
    player = Player("Davey")
    assert player.get_name() == "Davey"
    assert player.get_hand() == []
    assert player.get_temp_hand() == []
    assert player.get_total_health() == 0
    assert player.has_selected() is False


def test_dealing_replaces_the_temp_hand_rather_than_adding_to_it():
    player = Player("Jenny")
    player.deal([card("Icicle")])
    player.deal([card("Iceberg"), card("Spitfire")])

    assert len(player.get_temp_hand()) == 2
    assert [c.get_name() for c in player.get_temp_hand()] == ["Iceberg", "Spitfire"]


def test_placing_moves_a_card_from_temp_hand_to_hand():
    player = Player("Davey")
    dealt = card("Icicle")
    player.deal([dealt])

    player.place(dealt)

    assert player.get_temp_hand() == []
    assert player.get_hand() == [dealt]


def test_placing_recalculates_total_health():
    player = Player("Davey")
    first, second = card("Icicle"), card("Iceberg", 15)
    player.deal([first, second])

    player.place(first)
    assert player.get_total_health() == 100

    player.place(second)
    assert player.get_total_health() == 200


def test_hand_is_full_at_the_maximum_hand_size():
    player = Player("Davey")
    for _ in range(Player.MAX_HAND_SIZE):
        c = card()
        player.deal([c])
        player.place(c)

    assert player.hand_full() is True


def test_placing_into_a_full_hand_raises_full_hand_exception():
    player = Player("Davey")
    for _ in range(Player.MAX_HAND_SIZE):
        c = card()
        player.deal([c])
        player.place(c)

    extra = card("Showdown", 60, WeaponStyle.FURY)
    player.deal([extra])

    with pytest.raises(FullHandException):
        player.place(extra)


def test_selecting_a_card_sets_the_selection():
    player = Player("Davey")
    chosen = card()
    player.select(chosen)

    assert player.has_selected() is True
    assert player.get_selected_card() is chosen


def test_playing_clears_the_selection_and_damages_the_other_player():
    attacker = Player("Davey")
    defender = Player("Jenny")

    held = card("Iceberg", 15, WeaponStyle.ICE)
    defender.deal([held])
    defender.place(held)

    weapon = card("Spitfire", 25, WeaponStyle.HEAT)
    attacker.select(weapon)
    attacker.play(defender)

    assert attacker.has_selected() is False
    assert defender.get_total_health() == 75


def test_cards_reduced_to_zero_health_are_removed_from_the_hand():
    player = Player("Davey")
    held = card("Icicle", 10, WeaponStyle.ICE)
    player.deal([held])
    player.place(held)

    player.apply_damage(card("Shutdown", 100, WeaponStyle.FURY))

    assert player.get_hand() == []
    assert player.get_total_health() == 0


def test_surviving_cards_stay_in_the_hand_after_damage():
    player = Player("Davey")
    weak = card("Icicle", 10, WeaponStyle.ICE)
    strong = card("Iceberg", 15, WeaponStyle.ICE)
    player.deal([weak, strong])
    player.place(weak)
    player.place(strong)

    player.apply_damage(card("Spitfire", 25, WeaponStyle.HEAT))

    assert len(player.get_hand()) == 2
    assert player.get_total_health() == 150
