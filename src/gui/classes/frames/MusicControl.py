import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

from os.path import exists
from ...WidgetController import WidgetController

from PIL import ImageTk, Image

class MusicControl(ttk.LabelFrame):

    widget_controller : WidgetController 

    def __init__(self, root : ttk.Window, widget_controller : WidgetController) -> None:

        self.root = root

        super().__init__(
            self.root,
            labelwidget = ttk.Label(self.root, text="Music Controls")
        )

        self.widget_controller = widget_controller
        self.widget_controller.music_control = self

        self.construct_widgets()

    def construct_widgets(self) -> None:

        pb = ImageTk.PhotoImage(Image.open("./assets/fugue/icons/control-stop.png"))
        skbb = ImageTk.PhotoImage(Image.open("./assets/fugue/icons/arrow-skip-180.png"))
        bb = ImageTk.PhotoImage(Image.open("./assets/fugue/icons/control-skip-180.png"))
        skfb = ImageTk.PhotoImage(Image.open("./assets/fugue/icons/arrow-skip.png"))
        fb = ImageTk.PhotoImage(Image.open("./assets/fugue/icons/control-skip.png"))

        self.back_button = ttk.Button(
            self, image = bb,
            bootstyle=PRIMARY
        )
        self.back_button.image = bb # Garbage Collector Fix

        self.skip_back_button = ttk.Button(
            self, image = skbb,
            bootstyle=PRIMARY
        )
        self.skip_back_button.image = skbb # Garbage Collector Fix

        self.play_button = ttk.Button(
            self, image = pb,
            bootstyle=PRIMARY,
            command = self.widget_controller.pause_music
        )
        self.play_button.image = pb # Garbage Collector Fix

        self.skip_forward_button = ttk.Button(
            self, image = skfb,
            bootstyle = PRIMARY
        )
        self.skip_forward_button.image = skfb # Garbage Collector Fix

        self.forward_button = ttk.Button(
            self, image = fb,
            bootstyle = PRIMARY
        )
        self.forward_button.image = fb # Garbage Collector Fix

        self.back_button.grid(row = 0, column = 0, padx=5, pady=5, sticky="EW")
        self.skip_back_button.grid(row = 0, column = 1, padx=5, pady=5, sticky="EW")
        self.play_button.grid(row = 0, column = 2, padx=5, pady=5, sticky="EW")
        self.skip_forward_button.grid(row = 0, column = 3, padx=5, pady=5, sticky="EW")
        self.forward_button.grid(row = 0, column = 4, padx=5, pady=5, sticky="EW")