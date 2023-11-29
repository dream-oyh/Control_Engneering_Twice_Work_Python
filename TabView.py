from contextlib import suppress
from typing import Callable, Optional, Tuple, Union

import customtkinter
import matplotlib.pyplot as plt
from customtkinter.windows.widgets.font import CTkFont
from PIL import Image
from components import components as comp


class MyTab(customtkinter.CTkTabview):
    def __init__(self, master: any, **kwargs):
        super().__init__(master, **kwargs)
        self.Pulse = self.add("Pulse Input")
        self.Slope = self.add("Slope Input")
        self.Step = self.add("Step Input")
        self.Sin = self.add("Sin Input")
        kwargs = {"slidertext": ["w", "阻尼度", "T"], "max": [10, 2, 10], "min": [0, 0, 0]}
        self.Pulse_tab = comp.tab_frame(
            self.Pulse,
            text="Pulse Signal Plot",
            img_path="img/pulse_signal.png",
            **kwargs
        )
        self.Slope_tab = comp.tab_frame(
            self.Slope,
            text="Slope Signal Plot",
            img_path="img/slope_signal.png",
            **kwargs
        )
        self.Step_tab = comp.tab_frame(
            self.Step, text="Step Signal Plot", img_path="img/step_signal.png", **kwargs
        )
        self.Pulse_tab.grid(row=0, column=0, padx=20, pady=20)
        self.Slope_tab.grid(row=0, column=0, padx=20, pady=20)
        self.Step_tab.grid(row=0, column=0, padx=20, pady=20)
