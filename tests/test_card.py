from model.card import Card
from model.weapon_style import WeaponStyle


def test_card_starts_at_full_health():
    card = Card("Icicle", 10, WeaponStyle.ICE)
    assert card.get_health() == 100


def test_card_exposes_its_attributes():
    card = Card("Spitfire", 25, WeaponStyle.HEAT)
    assert card.get_name() == "Spitfire"
    assert card.get_attack() == 25
    assert card.get_style() == WeaponStyle.HEAT


def test_has_style_matches_only_its_own_style():
    card = Card("Iceberg", 15, WeaponStyle.ICE)
    assert card.has_style(WeaponStyle.ICE) is True
    assert card.has_style(WeaponStyle.FURY) is False


def test_damage_from_a_different_style_costs_the_attack_value():
    defender = Card("Iceberg", 15, WeaponStyle.ICE)
    attacker = Card("Spitfire", 25, WeaponStyle.HEAT)
    defender.apply_damage(attacker)
    assert defender.get_health() == 75


def test_damage_from_a_matching_style_is_doubled():
    defender = Card("Iceberg", 15, WeaponStyle.ICE)
    attacker = Card("Freeze Fire", 40, WeaponStyle.ICE)
    defender.apply_damage(attacker)
    assert defender.get_health() == 20


def test_damage_accumulates_across_attacks():
    defender = Card("Iceberg", 15, WeaponStyle.ICE)
    attacker = Card("Icicle", 10, WeaponStyle.ICE)
    defender.apply_damage(attacker)
    defender.apply_damage(attacker)
    assert defender.get_health() == 60


def test_health_can_fall_to_zero_or_below():
    defender = Card("Icicle", 10, WeaponStyle.ICE)
    attacker = Card("Shutdown", 100, WeaponStyle.FURY)
    defender.apply_damage(attacker)
    assert defender.get_health() <= 0


def test_copy_is_independent_and_restored_to_full_health():
    original = Card("Blindside", 30, WeaponStyle.ENERGY)
    original.apply_damage(Card("Showdown", 60, WeaponStyle.FURY))

    duplicate = original.copy()

    assert duplicate.get_name() == original.get_name()
    assert duplicate.get_attack() == original.get_attack()
    assert duplicate.get_style() == original.get_style()
    assert duplicate.get_health() == 100
    assert original.get_health() == 40


def test_str_returns_the_card_name():
    assert str(Card("Showdown", 60, WeaponStyle.FURY)) == "Showdown"
