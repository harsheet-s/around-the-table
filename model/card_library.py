from model.card import Card
from model.weapon_style import WeaponStyle

class CardLibrary:
    ALL_CARDS = [
        Card("Spitfire", 25, WeaponStyle.HEAT),
        Card("Blindside", 30, WeaponStyle.ENERGY),
        Card("Freeze Fire", 40, WeaponStyle.ICE),
        Card("Blazing Fury", 80, WeaponStyle.FURY),
        Card("Spitfire", 25, WeaponStyle.HEAT),
        Card("Icicle", 10, WeaponStyle.ICE),
        Card("Iceberg", 15, WeaponStyle.ICE),
        Card("Blindside", 30, WeaponStyle.ENERGY),
        Card("Showdown", 60, WeaponStyle.FURY),
        Card("Blindside", 30, WeaponStyle.ENERGY),
        Card("Icicle", 10, WeaponStyle.ICE),
        Card("Spitfire", 25, WeaponStyle.HEAT),
        Card("Shutdown", 100, WeaponStyle.FURY),
        Card("Blazing Fury", 80, WeaponStyle.FURY),
        Card("Blindside", 30, WeaponStyle.ENERGY),
        Card("Icicle", 10, WeaponStyle.ICE)
    ]
