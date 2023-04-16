import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from functools import partial
from typing import Tuple, Dict

from ...ApplicationConfig import ApplicationConfig

class Preferences(ttk.Menu):

    application_config : ApplicationConfig

    theme_identifiers : Dict[str, Tuple[str]] = {
        'light' : (
            'cosmo', 'flatly', 'journal', 'litera',
            'lumen', 'minty', 'pulse', 'sandstone',
            'united', 'yeti', 'morph', 'simplex',
            'cerulean'),

        'dark' : ('solar', 'vapor', 'darkly', 'superhero', 'cyborg')
    }

    theme_checkbutton_var : tk.IntVar
    toast_var = tk.BooleanVar

    def __init__(self, root : ttk.Window, application_config : ApplicationConfig) -> None:

        self.root = root
        self.application_config = application_config

        super().__init__(
            self.root,
            tearoff = 0,
        )

        self.init_vars()

        self.add_cascade(
            label = "Set Theme...", menu=self.build_theme_cascade()
        )

        self.add_checkbutton(
            label = "Toggle Toasts",
            variable = self.toast_var
        )

    def init_vars(self):

        self.theme_checkbutton_var = tk.IntVar(self)
        self.toast_var = tk.BooleanVar(self, value = self.application_config.get_toast_status())

    def set_program_theme(self, t : str) -> None:
        self.application_config.set_config_option(
            t, 'application', 'theme'
        )

        self.root.style.theme_use(t)

        self.update()

    def build_theme_cascade(self) -> ttk.Menu:
        
        m = ttk.Menu(self.root)

        for offset, kv in enumerate(self.theme_identifiers.items()):

            k, v = kv # upack
    
            m.add_command(
                label=k.capitalize() + " Themes",
                font = ttk.font.Font(weight='bold'),
            )

            for i, t in enumerate(v, start=100 * offset):

                m.add_radiobutton(
                    label = str(t).capitalize(),
                    command = partial(self.set_program_theme, t),
                    variable = self.theme_checkbutton_var,
                    value = i
                )

                if t == self.application_config.get_theme():
                    self.theme_checkbutton_var.set(i)

        return m
    
    def update_theme_cascade() -> None:
        pass
