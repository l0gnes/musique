import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

from PIL import ImageTk, Image

from .frames.MusicSelection import MusicSelection
from .frames.MusicControl import MusicControl
from .frames.MusicProgress import MusicProgress
from .frames.SongView import SongView

from ..WidgetController import WidgetController
from ..ApplicationConfig import ApplicationConfig

from .menu.MyMusic import MyMusic

from random import choice
from os import PathLike, environ

class MainPage(ttk.Window):

    widget_controller : WidgetController

    application_path : PathLike = "%s\\musique3" % environ['APPDATA']
    application_config : ApplicationConfig

    quirky_quotes = (
        ", now with more monkey business!",
        ", finally... an upgrade",
        ", i know it's not a mistake the third time around"
    )

    def __init__(
        self) -> None:
        
        self.application_config = ApplicationConfig(self.application_path)

        super().__init__(
            themename = self.application_config.get_theme()
        )

        super().title("Musique 3" + choice(self.quirky_quotes))

        app_icon = ImageTk.PhotoImage(Image.open("./assets/fugue/icons/animal-monkey.png"))
        super().iconphoto(False, app_icon)

        self.widget_controller = WidgetController(self, self.application_config)

        self.construct_widgets()

        self.config(menu=MyMusic(self, self.application_config))

    def construct_widgets(
        self) -> None:

        ms = MusicSelection(self, self.widget_controller)
        mp = MusicProgress(self, self.widget_controller)
        mc = MusicControl(self, self.widget_controller)
        sv = SongView(self, self.widget_controller)

        ms.grid(row=0, column=0, columnspan=2)
        mc.grid(row=1, column=0, columnspan=2, sticky="EW")
        mp.grid(row=2, column=0, sticky='EW', columnspan=2)
        sv.grid(row=0, column=2, rowspan=3, sticky="NS", padx=5)

    def run_hook(
        self) -> None:

        self.mainloop()