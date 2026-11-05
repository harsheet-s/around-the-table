class Card:
    def __init__(self, name, attack, style):
        self.__name = name
        self.__attack = attack
        self.__style = style
        self.__health = 100

    def copy(self):
        return Card(self.__name, self.__attack, self.__style)

    def get_name(self):
        return self.__name

    def get_attack(self):
        return self.__attack

    def get_health(self):
        return self.__health
    
    def get_style(self):
        return self.__style

    def has_style(self, style):
        return self.__style == style

    def apply_damage(self, card):
        damage = (card.get_attack() * 2) if card.has_style(self.__style) else card.get_attack()
        self.__health -= damage
    
    def __str__(self):
        return self.__name
