from tkinter import *
from TkUtils import TkUtils as ut
from model.player import Player
from model.dealer import Dealer
from DealerView import DealerView
from model.login_model import LoginModel
from PlayerView import PlayerView

#Note that this class is not done!
#This will only add 2 players to the game.

#This structure is following the method shown in the study modules
#You are welcome to change this however you want
class LoginView:

    def __init__(self, root, model):
        self.model = model
        self.root = root
        
        self.player1 = None
        self.player2 = None
        self.player3 = None
        self.player4 = None

    

    def control(self):
        entryframe = ut.frame(self.root)
        
        p1col = ut.frame(entryframe)
        ut.image(p1col, "image/avatar.png", 100, 80).pack(pady=(10, 5))
        self.player1 = ut.entry(p1col, "Davey", False)
        self.player1.pack(padx=10, pady=10)
        p1col.pack(side=LEFT)
        
        p2col = ut.frame(entryframe)
        ut.image(p2col, "image/avatar.png", 100, 80).pack(pady=(10, 5))
        self.player2 = ut.entry(p2col, "Jenny", False)
        self.player2.pack(padx=10, pady=10)
        p2col.pack(side=LEFT)
        
        p3col = ut.frame(entryframe)
        ut.image(p3col, "image/avatar.png", 100, 80).pack(pady=(10, 5))
        self.player3 = ut.entry(p3col)
        self.player3.pack(padx=10, pady=10)
        p3col.pack(side=LEFT)
        
        p4col = ut.frame(entryframe)
        ut.image(p4col, "image/avatar.png", 100, 80).pack(pady=(10, 5))
        self.player4 = ut.entry(p4col)
        self.player4.pack(padx=10, pady=10)
        p4col.pack(side=LEFT)
        
        entryframe.pack(pady=(0, 50), padx=50)
        
        btnframe = ut.frame(self.root)
        ut.button(btnframe, "Start Game", self.start).pack(expand=TRUE, fill=X)
        btnframe.pack(expand=TRUE, fill=X)

    def start(self):
        self.model.add_to_game(Player(self.player1.get()))
        self.model.add_to_game(Player(self.player2.get()))
        p3name = self.player3.get()
        if p3name:
            self.model.add_to_game(Player(p3name))
        p4name = self.player4.get()
        if p4name:
            self.model.add_to_game(Player(p4name))
        
        players = self.model.get_players()
        dealer = Dealer(players)
        dealer_view = DealerView(ut.same_window("Dealer", self.root), dealer, [])
        dealer_view.control()
        for player in players:
            pv = PlayerView(ut.top_level(player.get_name()), player, dealer, dealer_view)
            pv.control()
            dealer_view.playerviews.append(pv)

        

if __name__ == "__main__":
    root = ut.root()
    LoginView(root, LoginModel()).control()
    root.mainloop()
