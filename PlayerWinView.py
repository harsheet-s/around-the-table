from tkinter import *
from TkUtils import TkUtils as ut

class PlayerWinView:
    def __init__(self, root, winner):
        self.root = root
        self.winner = winner

    def control(self):
        mainframe = ut.frame(self.root)
        mainframe.pack(padx=30, pady=30)

        winnermessage = (
            self.winner.get_name()
            + " wins with "
            + str(self.winner.get_total_health())
            + " health"
        )

        winlabel = ut.label(
            mainframe,
            winnermessage
        )

        winlabel.pack(pady=20)
