from tkinter import *
from TkUtils import TkUtils as ut

class CardView:
    def __init__(self, root, card):
        self.root = root
        self.card = card

    def control(self):

        cardpath = (
            "image/cards/"
            + self.card.get_name().lower().replace(" ", "")
            + ".png"
        )

        cardimage = ut.image(
            self.root,
            cardpath,
            280,
            200
        )

        cardimage.pack(padx=20, pady=20)
