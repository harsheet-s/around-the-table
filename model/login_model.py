class LoginModel:
    MAX_PLAYERS = 4
    def __init__(self):
        self.__players = []

    def add_to_game(self, player):
        if len(self.__players) == LoginModel.MAX_PLAYERS:
            raise RuntimeError("Too many players")
        self.__players.append(player)

    def get_players(self):
        return self.__players
