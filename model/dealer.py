from model.deck import Deck
from model.exception.empty_deck_exception import EmptyDeckException
from model.exception.round_not_ready_exception import RoundNotReadyException


class Dealer:
    def __init__(self, players):
        self.__main_deck = Deck(16)
        self.__secondary_deck = Deck(6)
        self.__players = players
        self.__round_counter = 0

    def get_main_deck(self):
        return self.__main_deck

    def get_secondary_deck(self):
        return self.__secondary_deck

    def get_players(self):
        return self.__players

    def deal(self):
        if not self.__main_deck.has_enough(len(self.__players)):
            raise EmptyDeckException("Not enough cards in main deck to deal!")
        if not self.__secondary_deck.has_enough(1):
            raise EmptyDeckException("Not enough cards in secondary deck to deal!")
        self.__round_counter += 1
        for player in self.__players:
            deal = [self.__main_deck.remove_card()]
            if (self.__round_counter - 1) % len(self.__players) == self.__players.index(player):
                deal.append(self.__secondary_deck.remove_card())
            player.deal(deal)

    def play(self):
        if not self.every_player_selected():
            raise RoundNotReadyException("All players must select a card from their hand!")
        for player in self.__players:
            next_player = None
            if self.__players.index(player) == (len(self.__players) - 1):
                next_player = self.__players[0]
            else:
                next_player = self.__players[self.__players.index(player) + 1]
            player.play(next_player)

    def every_player_selected(self):
        for player in self.__players:
            if not player.has_selected():
                return False
        return True
