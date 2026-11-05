from enum import Enum

class WeaponStyle(Enum):
    ENERGY = "ENERGY"
    HEAT = "HEAT"
    ICE = "ICE"
    FURY = "FURY"

    def __str__(self):
        return self.value
