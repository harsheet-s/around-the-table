from tkinter import *
from TkUtils import TkUtils as ut
from model.exception.empty_deck_exception import EmptyDeckException
from model.exception.round_not_ready_exception import RoundNotReadyException
from DeckView import DeckView
from ErrorView import ErrorView
from PlayerWinView import PlayerWinView

class DealerView:
    def __init__(self, root, dealer, playerviews):
        self.root = root
        self.dealer = dealer
        self.playerviews = playerviews

    def dealclicked(self):
        try:
            self.dealer.deal()
            self.updatescores()
            for pv in self.playerviews:
                pv.updatetemphand()

        except EmptyDeckException as error:
            ErrorView(ut.top_level("Error"), error).control()
        self.updatebuttonstates()

    def playclicked(self):
        try:
            self.dealer.play()
            self.updatescores()
            for pv in self.playerviews:
                pv.updatehand()
        except RoundNotReadyException as error:
            ErrorView(ut.top_level("Error"), error).control()
        self.updatebuttonstates()

    def callclicked(self):
        players = self.dealer.get_players()
        winner = players[0]
        for player in players:
            if player.get_total_health() > winner.get_total_health():
                winner = player
        PlayerWinView(ut.top_level("Game Over"), winner).control()
    
    def updatescores(self):
         players = self.dealer.get_players()
         for i in range(4):
             if i < len(players):
                 health = players[i].get_total_health()
                 self.scorelabels[i].config(
                     text=f"Player {i + 1}: {health}"
                 )

             else:
                 self.scorelabels[i].config(
                     text=f"Player {i + 1}: N/A"
                 )
    def updatebuttonstates(self):
        pass
        #mainok = self.dealer.get_main_deck().has_enough(len(self.dealer.get_players()))
        #secondaryok = self.dealer.get_secondary_deck().has_enough(1)
        #if mainok and secondaryok:
            #self.dealbtn.config(state="normal", background=ut.red)
        #else:
            #self.dealbtn.config(state="disabled", background="#ffd0d0")
        
        
        ##if self.dealer.every_player_selected():
            ##self.playbtn.config(state="normal", background=ut.red)
        ##else:
            ##self.playbtn.config(state="disabled", background="#ffd0d0")
    
    
    def openmaindeck(self):
        DeckView(ut.top_level("Main Deck"), self.dealer.get_main_deck()).control()

    def opensecondarydeck(self):
        DeckView(ut.top_level("Secondary Deck"), self.dealer.get_secondary_deck()).control()
    
    def control(self):

    
        firstframe = ut.frame(self.root)
        firstframe.pack(pady=20)

        self.maindeck = ut.image(firstframe, "image/deck.png", 150, 100)
        self.maindeck.pack(side=LEFT, padx=20)

        self.secondarydeck = ut.image(firstframe, "image/deck.png", 150, 100)
        self.secondarydeck.pack(side=LEFT, padx=20)

        self.maindeck.bind("<Button-1>", lambda e: self.openmaindeck())
        self.secondarydeck.bind("<Button-1>", lambda e: self.opensecondarydeck())
        
        middleframe = ut.frame(self.root)
        middleframe.pack(pady=10)
        scores = ut.frame(middleframe)
        scores.pack(side=LEFT, padx=20)

        self.player1score = ut.text(scores, "Player 1: 0")
        self.player1score.pack(anchor="w")
        self.player2score = ut.text(scores, "Player 2: 0")
        self.player2score.pack(anchor="w")
        self.player3score = ut.text(scores, "Player 3: N/A")
        self.player3score.pack(anchor="w")
        self.player4score = ut.text(scores, "Player 4: N/A")
        self.player4score.pack(anchor="w")

        self.scorelabels = [
            self.player1score,
            self.player2score,
            self.player3score,
            self.player4score
        ]

        
        callbtn = ut.button(middleframe, "Call", self.callclicked)
        callbtn.pack(side=LEFT, padx=20)

        
        bottomframe = ut.frame(self.root)
        bottomframe.pack(pady=20)

        self.dealbtn = ut.button(bottomframe, "Deal", self.dealclicked)
        self.dealbtn.pack(side=LEFT, padx=10)

        self.playbtn = ut.button(bottomframe, "Play Round", self.playclicked)
        self.playbtn.pack(side=LEFT, padx=10)

        exitbtn = ut.button(bottomframe, "Exit", self.root.destroy)
        exitbtn.pack(side=LEFT, padx=10)

        self.updatescores()
        self.updatebuttonstates()

        

    
