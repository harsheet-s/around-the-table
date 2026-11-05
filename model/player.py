from model.exception.full_hand_exception import FullHandException

class Player:
    MAX_HAND_SIZE = 4
    def __init__(self, name):
        self.__name = name
        self.__hand = []
        self.__temp_hand = []
        self.__selected_card = None
        self.__total_health = 0

    def get_hand(self):
        return self.__hand

    def get_temp_hand(self):
        return self.__temp_hand

    def get_name(self):
        return self.__name
    
    def get_selected_card(self):
        return self.__selected_card

    def get_total_health(self):
        return self.__total_health

    def deal(self, deal):
        self.__temp_hand.clear()
        self.__temp_hand.extend(deal)

    def place(self, card):
        if self.hand_full():
            raise FullHandException("Hand is full!")
        self.__temp_hand.remove(card)
        self.__hand.append(card)
        self.calculate_health()

    def play(self, next_player):
        next_player.apply_damage(self.get_selected_card())
        self.__selected_card = None

    def select(self, card):
        self.__selected_card = card

    def has_selected(self):
        return self.__selected_card != None

    def calculate_health(self):
        total = 0
        for card in self.__hand:
            total += card.get_health()
        self.__total_health = total

    def hand_full(self):
        return len(self.__hand) >= Player.MAX_HAND_SIZE

    def apply_damage(self, card):
        matches = []
        for c in self.__hand:
            c.apply_damage(card)
            if c.get_health() <= 0:
                matches.append(c)
        for c in matches:
            self.__hand.remove(c)
        self.calculate_health()
