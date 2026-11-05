from tkinter import *
from TkUtils import TkUtils as ut
from CardView import CardView

class DeckView:
    def __init__(self, root, deck):
        self.root = root
        self.deck = deck

    def cardclicked(self):
        selected = self.cardtree.selection()
        if not selected:
            return

        item = self.cardtree.item(selected[0])

        cardname = item["values"][0]
        cards = self.deck.get_cards()
        for card in cards:
            if card.get_name() == cardname:
                CardView(
                    ut.top_level(card.get_name()),
                    card
                ).control()
                return

    def updateshowcardstate(self, event=None):

        if self.cardtree.selection():
            self.showcardbtn.config(
                state="normal",
                background="#ff8f8f"
            )
        else:
            self.showcardbtn.config(
                state="disabled",
                background="#ffd0d0"
        )

    def control(self):

        mainframe = ut.frame(self.root)
        mainframe.pack(pady=20)

        self.cardtree = ut.treeview(
            mainframe,
            ["Name"],
            width=300
        )
        self.cardtree.pack(pady=10)

        cards = self.deck.get_cards()

        for card in cards:

            cardname = card.get_name()

            self.cardtree.insert(
                "",
                "end",
                values=(cardname,)
            )

        self.showcardbtn = ut.button(
            mainframe,
            "Show Card",
            self.cardclicked
        )
        self.showcardbtn.pack(pady=10)
        self.showcardbtn.config(
        state="disabled",
        background="#ffd0d0"
    )
        self.cardtree.bind(
        "<<TreeviewSelect>>",
        self.updateshowcardstate
    )
        self.updateshowcardstate()
