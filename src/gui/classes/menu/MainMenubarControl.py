import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

class MainMenubar(ttk.Menu):

    def __init__(self, root : ttk.Window) -> None:

        self.root = root

        super().__init__(
            self.root,
            tearoff = 0
        )