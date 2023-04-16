import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

from ...WidgetController import WidgetController

class MusicProgress(ttk.LabelFrame):

    # The number of microseconds that have surpassed in the song
    music_progress_total_duration : int
    music_progress : int

    tkinter_progressbar_var : tk.DoubleVar

    widget_controller : WidgetController

    def __init__(
        self, root : ttk.Window, widget_controller : WidgetController) -> None:

        self.root = root

        super().__init__(
            self.root,
            labelwidget = ttk.Label(self.root, text="Music Progress")
        )

        self.widget_controller = widget_controller
        self.widget_controller.music_progress = self

        self.init_vars()

        self.construct_widgets()

        # Starts the music progress update hook
        self.music_progress_update_hook()

    def init_vars(self) -> None:

        self.tkinter_progressbar_var = tk.DoubleVar(self, value=25)

    def construct_widgets(self) -> None:

        self.music_progress_bar = ttk.Progressbar(
            self,
            mode = 'determinate',
            orient = 'horizontal',
            variable=self.tkinter_progressbar_var,
            maximum = 100,
            bootstyle = 'secondary'
        )

        self.grid_columnconfigure(0, weight=1)

        self.music_progress_bar.grid(
            column = 0, row = 0, sticky = 'EW',
            padx = 10, pady= 10
        )

        self.music_progress_text = ttk.Label(
            self,
            text = "0:00 / 0:00"
        )

        self.music_progress_text.grid(
            column = 1, row = 0, 
            padx = 10, pady = 10,
            sticky = 'NSEW'
        )

    def music_progress_update_hook(self):

        # Updates the clock next to the progress bar
        self.update_string_timestamp() 

        # Updates the tkinter var with the 0-100 value for completion
        self.update_tkinter_progress_var()

        # Updates appropriate widgets
        self.update_widgets()

        # Call the hook again after 500 ms
        self.after(50, self.music_progress_update_hook)

    def update_string_timestamp(self) -> None:
        pass

    def update_tkinter_progress_var(self) -> None:
        pass

    def update_widgets(self) -> None:

        if self.widget_controller.is_music_paused:
            self.music_progress_bar.config(bootstyle="primary-striped")
        else:
            self.music_progress_bar.config(bootstyle='secondary')

        self.music_progress_bar.update()

        self.music_progress_text.update()

    # Everything below is for outer widgets

    def set_paused_state(self, state : bool) -> None:
        self.paused = state

    def toggle_paused_state(self) -> bool:
        self.paused = not self.paused
        return self.paused
    
    def set_music_played_duration(self, t: int) -> None:
        self.music_progress = t

    def set_song_duration(self, t : int) -> None:
        self.music_progress_total_duration = t