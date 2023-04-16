import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

from .MyMenuPlaylist import MyMusicPlaylistMenu
from .Preferences import Preferences

from ...ApplicationConfig import ApplicationConfig

class MyMusic(ttk.Menu):

    application_config : ApplicationConfig

    def __init__(self, root : ttk.Window, application_config) -> None:

        self.root = root

        super().__init__(
            self.root,
            tearoff = 0,
        )

        self.application_config = application_config

        self.add_cascade(label="Playlists", menu=MyMusicPlaylistMenu(self.root))

        self.add_cascade(label="Preferences", menu=Preferences(self.root, self.application_config))
        self.add_cascade(label="Help")
    