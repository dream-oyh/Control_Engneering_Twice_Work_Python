from contextlib import suppress
from typing import Callable, Optional, Tuple, Union

import customtkinter

from .tab_frame import tab_frame


class MyTab(customtkinter.CTkTabview):
    def __init__(self, master: any, **kwargs):
        from components.tab_frame import tab_frame

        super().__init__(master, **kwargs)
        self.Pulse = self.add("Pulse Input")
        self.Slope = self.add("Slope Input")
        self.Step = self.add("Step Input")
        self.Sin = self.add("Sin Input")
        frame_args = {
            "slidertext": ["w", "阻尼度", "T"],
            "max": [10, 2, 10],
            "min": [0, 0, 0],
        }
        self.frames = [
            tab_frame(
                self.Pulse,
                text="Pulse Signal Plot",
                img_path="img/pulse_signal.png",
                **frame_args
            ),
            tab_frame(
                self.Slope,
                text="Slope Signal Plot",
                img_path="img/slope_signal.png",
                **frame_args
            ),
            tab_frame(
                self.Step,
                text="Step Signal Plot",
                img_path="img/step_signal.png",
                **frame_args
            ),
            tab_frame(
                self.Sin,
                text="Sin Signal Plot",
                img_path="img/sin_signal.png",
                **frame_args
            ),
        ]
        for i in self.frames:
            i.grid(row=0, column=0, padx=10, pady=10)

    def get_frame_by_name(self, name: str):
        for i in self.frames:
            if i.name == name:
                return i
