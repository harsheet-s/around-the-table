from model.card_library import CardLibrary

class Deck:
    def __init__(self, size):
        self.__cards = [card.copy() for card in CardLibrary.ALL_CARDS[:size]]

    def remove_card(self):
        return self.__cards.pop()

    def has_enough(self, amount_needed):
        return len(self.__cards) >= amount_needed

    def get_cards(self):
        return self.__cards
