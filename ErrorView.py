from tkinter import *
from TkUtils import TkUtils as ut

class ErrorView:
    def __init__(self, root, error):
        self.root = root
        self.error = error

    def control(self):

        mainframe = ut.frame(self.root)
        mainframe.pack(padx=20, pady=20)

        errorimage = ut.image(
            mainframe,
            "image/error.png",
            100,
            100
        )
        errorimage.pack(pady=10)

        errorname = ut.error_label(
            mainframe,
            type(self.error).__name__
        )
        errorname.pack(pady=5)

        errortext = ut.error_label(
            mainframe,
            str(self.error)
        )
        errortext.pack(pady=5)
