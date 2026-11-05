from tkinter import *
from TkUtils import TkUtils as ut
from model.exception.full_hand_exception import FullHandException
from ErrorView import ErrorView

class PlayerView:
    def __init__(self, root, player, dealer, dealer_view):
        self.root = root
        self.player = player
        self.dealer = dealer
        self.dealer_view = dealer_view

    def updatetemphand(self):

        rows = self.temptree.get_children()
        self.temptree.delete(*rows)
        cards = self.player.get_temp_hand()

        for card in cards:

            cardname = card.get_name()

            self.temptree.insert(
                "",
                "end",
                values=(cardname,)
            )
    def updatehand(self):

        rows = self.handtree.get_children()
        self.handtree.delete(*rows)
        cards = self.player.get_hand()

        for card in cards:

            cardname = card.get_name()
            cardattack = card.get_attack()
            cardstyle = card.get_style()
            cardhealth = card.get_health()

            self.handtree.insert(
                "",
                "end",
                values=(cardname, cardattack, cardstyle, cardhealth)
            )
    
    def placeclicked(self):
        selection = self.temptree.selection()
        if not selection:
            return
        selectedname = self.temptree.item(selection[0])["values"][0]
        
        cardtoplace = None
        for card in self.player.get_temp_hand():
            if card.get_name() == selectedname:
                cardtoplace = card
                break
        
        if cardtoplace is None:
            return
        
        try:
            self.player.place(cardtoplace)
            self.updatetemphand()
            self.updatehand()
            self.dealer_view.updatescores()
        except FullHandException as error:
            ErrorView(ut.top_level("Error"), error).control()
        self.dealer_view.updatebuttonstates()
    
    def updatecardphoto(self, card):
        self.cardphoto.destroy()
        path = "image/cards/" + card.get_name().lower().replace(" ", "") + ".png"
        self.cardphoto = ut.image(self.rightframe, path, 200, 140)
        self.cardphoto.pack(pady=10)
    
    def selectclicked(self):
        selected = self.handtree.selection()
        if not selected:
            return

        item = self.handtree.item(selected[0])
        values = item["values"]
        cardname = values[0]

        selectedcard = None
        for card in self.player.get_hand():
            if card.get_name() == cardname:
                selectedcard = card
                break

        if selectedcard is None:
            return

        self.player.select(selectedcard)
        self.updatecardphoto(selectedcard)
        self.dealer_view.updatebuttonstates()
    
    def updateplacestate(self, event=None):
        if self.temptree.selection():
            self.placebtn.config(state="normal", background=ut.red)
        else:
            self.placebtn.config(state="disabled", background="#ffd0d0")
    
    def updateselectstate(self, event = None):

        if self.handtree.selection():
            self.selectbtn.config(state="normal",background=ut.red)
        else:
            self.selectbtn.config(state="disabled",background="#ffd0d0")
    
    def control(self):
        mainframe = ut.frame(self.root)
        mainframe.pack(pady=20)

        leftframe = ut.frame(mainframe)
        leftframe.pack(side=LEFT, padx=20)
        ut.label(leftframe, "Hand").pack(pady=5)

        self.handtree = ut.treeview(
            leftframe,
            ["Name", "Attack", "Style", "Health"],
            width=400
        )
        self.handtree.config(height=5)
        self.handtree.pack()
        

        self.selectbtn = ut.button(
            leftframe,
            "Select",
            self.selectclicked
        )
        self.selectbtn.pack(pady=10)
        self.selectbtn.config(state="disabled",background="#ffd0d0")
        
        self.handtree.bind(
        "<<TreeviewSelect>>",
        self.updateselectstate
    )

        self.rightframe = ut.frame(mainframe)
        self.rightframe.pack(side=LEFT, padx=20)

        ut.label(self.rightframe, "Temp Hand").pack(pady=5)

        self.temptree = ut.treeview(
            self.rightframe,
            ["Name"],
            width=150
        )
        self.temptree.config(height=3)
        self.temptree.pack()
        
        self.placebtn = ut.button(
            self.rightframe,
            "Place",
            self.placeclicked
        )
        self.placebtn.pack(pady=10)
        self.placebtn.config(state="disabled", background="#ffd0d0")
        self.placebtn.config(state="disabled")
        
        
        self.temptree.bind("<<TreeviewSelect>>", self.updateplacestate)

        self.cardphoto = ut.image(
            self.rightframe,
            "image/cards/empty.png",
            200,
            140
        )
        self.cardphoto.pack(pady=10)