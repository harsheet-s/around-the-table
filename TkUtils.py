from tkinter import *
from tkinter import ttk
from PIL import Image
from PIL import ImageTk

#You will never have to manually call this, It's used as part of one of the static methods
class ObservableButton(Button):
    def __init__(self, root, text, callback, main_color, hover_color):
        Button.__init__(self, root, text=text, command=callback, background=main_color, padx=0, relief=FLAT,
                   font="Arial 11 bold", foreground="white")
        self.bind("<Enter>", self.on_hover)
        self.bind("<Leave>", self.on_exit)
        self.main_color = main_color
        self.hover_color = hover_color

    def on_hover(self, event):
        self["background"] = self.hover_color

    def on_exit(self, event):
        self["background"] = self.main_color

class TkUtils:
    red = "#ff8f8f"
    off_white = "#f4f4f4"

    @staticmethod
    def root():
        """
        Generates the root login window for the application.

        Returns:
            The root tk.Tk() object, prestyled and preconfigured.
        """
        window = Tk()
        window.title("Login")
        window.configure(background=TkUtils.off_white)
        return window

    @staticmethod
    def top_level(title_):
        """
        Generates a top level window for the application.

        Parameters:
            title_ (str): The title of the window.

        #TODO
        Returns:
            A toplevel window, prestyled and preconfigured.
        """
        tl = Toplevel()
        tl.resizable(False, False)
        tl.title(title_)
        tl.configure(background=TkUtils.off_white)
        return tl

    @staticmethod
    def same_window(title, root):
        """
        A simple way to replace the content of a window without a top level window.

        Parameters:
            title (str): The title of the window.
            root (tk.Tk): The existing window.

        Returns:
            The existing window with all packed elements removed.
        """
        for pack in root.pack_slaves():
            pack.destroy()
        root.title(title)
        return root

    @staticmethod
    def frame(root):
        """
        Generates a frame
        
        Parameters:
            root (tk.Tk): The window or frame containing the frame.
        
        Returns:
            A tk.Frame() object, prestyled and preconfigured.
        """
        frame = Frame(root)
        frame.configure(background=TkUtils.off_white)
        return frame

    @staticmethod
    def button(root, text_, callback=None):
        """
        Generates a prestyled button according to the assignment specifications.

        Parameters:
            root (tk.Tk): The window or frame containing the button.
            text_ (str): The text of the button.
            callback (function, optional): The callback function.

        Returns:
            A tk.Button() object, prestyled and preconfigured.
        """
        return ObservableButton(root, text_, callback, TkUtils.red, "#ff8080")

    @staticmethod
    def separator(root):
        """
        Generates a prestyled separator according to the assignment specifications.

        Parameters:
            root (tk.Tk): The window or frame containing the separator.

        Returns:
            A ttk.Separator() object, prestyled and preconfigured.
        """
        return ttk.Separator(root, orient='horizontal')

    @staticmethod
    def label(root, text_):
        """
        Generates a prestyled label according to the assignment specifications.

        Parameters:
            root (tk.Tk): The window or frame containing the label.
            text_ (str): The text of the label.

        Returns:
            A tk.Label() object, prestyled and preconfigured.
        """
        return Label(root, text=text_, font="Helvetica 12 bold", foreground="#000000", background=TkUtils.off_white)

    @staticmethod
    def text(root, text_):
        """
        Generates a prestyled piece of text according to the assignment specifications.
        
        Parameters:
            root (tk.Tk): The window or frame containing the label.
            text_ (str): The text of the label.

        Returns:
            A tk.Label() object, prestyled and preconfigured.
        """
        return Label(root, text=text_, font="Helvetica 10", foreground="#222222", background=TkUtils.off_white)

    @staticmethod
    def error_label(root, text_):
        """
        Generates a prestyled error label according to the assignment specifications.

        Parameters:
            root (tk.Tk): The window or frame containing the label.
            text_ (str): The text of the label.

        Returns:
            A tk.Label() object, prestyled and preconfigured.
        """
        return Label(root, text=text_, font="Courier 14", foreground="RED", background=TkUtils.off_white)

    @staticmethod
    def image(root, path, height, width, background=None):
        """
        Generates an image.

        Parameters:
            root (tk.Tk): The window or frame containing the image.
            path (str): The path to the image.
            height (int): The height of the image.
            width (int): The width of the image.
            background (str, optional): The background of the image. Defaults to no background

        Returns:
            A tk.Label() object with an image attribute, prestyled and preconfigured.
        """
        image_ = ImageTk.PhotoImage(Image.open(path).resize((width, height)))
        lbl = Label(root, image=image_)
        lbl.photo = image_
        if background:
            lbl.configure(background=background)
        else:
            lbl.configure(background=TkUtils.off_white)
        return lbl

    @staticmethod
    def entry(root, placeholder="", editable=True):
        """
        Generates an entry field
        
        Parameters:
            root (tk.Tk): The window or frame containing the entry field
            placeholder (str, optional): The text to display by default. Defaults to nothing.
            editable (bool, optional): Specified whether then entry is permitted to be edited. Defaults to True.
        
        Returns:
            A tk.Entry() object.
        """
        entry = Entry(root)
        if placeholder:
            entry.insert(0, placeholder)
        if not editable:
            entry.config(state=DISABLED)
        entry.config(width=16)
        return entry

    #You will never have to manually call this, It's used as part of one of the static methods
    @staticmethod
    def _select(event, tree):
        item_id = tree.identify_row(event.y)
        if item_id is None:
            return
        if item_id in tree.selection():
            tree.selection_remove(item_id)
            return 'break'

    @staticmethod
    def treeview(root, columns, multi=False, width=300):
        """
        Generates a prestyled treeview according to the assignment specifications.

        Parameters:
            root (tk.Tk): The window or frame containing the treeview.
            columns (list): A list of column names.
            multi (bool, optional): Whether the tree view is multi-column or not. Defaults to browse (single) mode
            width (int, optional): The width of the treeview. Defaults to 300

        Returns:
            A ttk.Treeview() object, prestyled and preconfigured with deselecting
        """
        tree = ttk.Treeview(root, show="headings", height=12, columns=columns, selectmode="extended" if multi else "browse")
        for column in tree["columns"]:
            tree.column(column, anchor=CENTER, width=int(width/len(columns)), stretch=NO)
        for i in range(len(columns)):
            tree.heading(i, text=columns[i])
        tree.bind("<<TreeViewSelect>>", 'break')
        tree.bind("<Button-1>", lambda event: TkUtils._select(event, tree))
        return tree
