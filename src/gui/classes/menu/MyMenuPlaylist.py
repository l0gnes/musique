import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

from PIL import Image, ImageTk

class MyMusicPlaylistMenu(ttk.Menu):

    def __init__(self, root : ttk.Window) -> None:

        self.root = root

        super().__init__(
            self.root,
            tearoff = 0
        )

        self.add_command(
            label="Create New Playlist", 
            command=lambda: CreatePlaylistDialog(self.root),
            compound = "left",
        )
        self.add_command(label="Edit Playlist", command = lambda: print("Hello World!"))

        self.add_separator()

        self.add_command(label="Import Playlist", command=lambda: print("Hello World!"))
        self.add_command(label="Export Playlist", command=lambda: print("Hello World!"))
    