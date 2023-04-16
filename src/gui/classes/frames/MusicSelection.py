import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

from ...PlaylistTreeConsumer import PlaylistTreeConsumer
from ...WidgetController import WidgetController

class MusicSelection(ttk.LabelFrame):

    search_var : tk.StringVar

    def __init__(self, root : ttk.Window, widget_controller : WidgetController) -> None:

        self.root = root

        super().__init__(
            self.root,
            labelwidget = ttk.Label(self.root, text="Playlist Collection")
        )

        self.widget_controller = widget_controller
        self.widget_controller.music_selection = self

        self.init_vars()

        self.construct_widgets()

    def init_vars(self) -> None:
        
        self.search_var = tk.StringVar(self)
        self.search_var.set("Search...") 

    def construct_widgets(self) -> None:

        self.search_bar = ttk.Entry(
            self,
            textvariable = self.search_var
        )

        self.search_bar.grid(
            column=0, columnspan=2, row=0,
            sticky = "EW",
            pady=5
        )

        self.tree_view = ttk.Treeview(
            self, 
            columns=['artist'],
            displaycolumns=['artist'],
            show="tree headings",
        )

        self.build_playlist_tree()

        self.tree_view.grid(row=1, column=0)

        self.tree_view.heading('#0', text='Song', anchor='w')
        self.tree_view.heading('#1', text='Artist', anchor='w')

        self.playlist_scrollbar = ttk.Scrollbar(self, orient='vertical', bootstyle="secondary round")

        self.playlist_scrollbar.grid(row=1, column=1, sticky="NS")

        

    def build_playlist_tree(self) -> None:

        PlaylistTreeConsumer.buildTree(
            self.tree_view, self.widget_controller.playlist_handler.get_playlists()
        )
