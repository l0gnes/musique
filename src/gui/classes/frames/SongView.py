import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

from ...WidgetController import WidgetController
from ...data import Song

from PIL import Image, ImageTk

class SongView(ttk.LabelFrame):

    widget_controller : WidgetController

    artist_var : tk.StringVar
    title_var : tk.StringVar

    def __init__(self, root : ttk.Window, wc : WidgetController):

        self.root = root

        super().__init__(
            self.root,
            labelwidget = ttk.Label(
                self.root, 
                text="Song Information", 
                image=ImageTk.PhotoImage(Image.open("./assets/fugue/icons/cookie-bite.png")))
        )

        self.init_vars()

        self.widget_controller = wc
        self.widget_controller.song_view = self

        self.construct_widgets()

    def init_vars(self) -> None:
        self.title_var = tk.StringVar(self)
        self.artist_var = tk.StringVar(self)

    def construct_widgets(self) -> None:

        self.photo_frame = ttk.Frame(self, width=250, height=250, bootstyle=PRIMARY)
        self.photo_frame.grid(row=0, column=0, columnspan=2, pady=5, padx=5, sticky='NS')

        self.song_title_label = ttk.Label(self, text="Song Title", justify='right')
        self.song_title_label.grid(row=1, column=0, padx=5, pady=5)

        self.song_title_value = ttk.Entry(self, state=DISABLED, width=30, textvariable=self.title_var)
        self.song_title_value.grid(row=1, column=1, padx=5, pady=5)
        
        self.artist_title_label = ttk.Label(self, text="Artist", justify='right')
        self.artist_title_label.grid(row=2, column=0, padx=5, pady=5)

        self.artist_title_value = ttk.Entry(self, state=DISABLED, width=30, textvariable=self.artist_var)
        self.artist_title_value.grid(row=2, column=1, padx=5, pady=5)

    def set_currently_shown(self, song : Song) -> None:
        
        self.title_var.set(song.name)
        self.artist_var.set(song.artist)
