import customtkinter
from core import one_order
import matplotlib.pyplot as plt
import numpy as np

global legend_pulse
legend_pulse = []


class MySlider(customtkinter.CTkFrame):
    """
    由标题，滑动条，输入框组成的组件。
    """

    def __init__(self, master: any, text: str, max, min, **kwargs):
        kwargs = {"fg_color": master._fg_color, **kwargs}
        super().__init__(master, **kwargs)
        # label
        self.label = customtkinter.CTkLabel(self, text=text)
        # slider
        self.x = customtkinter.DoubleVar(value=0.01)

        self.x_slider = customtkinter.CTkSlider(
            self, variable=self.x, from_=min, to=max, command=self.caculate
        )
        # entry
        self.x_entry = customtkinter.CTkEntry(self, textvariable=self.x)
        self.label.grid(row=0, column=0, padx=20, pady=20, sticky="w")
        self.x_slider.grid(row=0, column=1, padx=20, pady=20, columnspan=2, sticky="w")
        self.x_entry.grid(row=0, column=3, padx=20, pady=20, sticky="w")

    def set_enabled(self, state: bool):
        self.x_slider.configure(state="normal" if state else "disabled")
        self.x_entry.configure(state="normal" if state else "disabled")

    def caculate(self, value):
        self.x.set(format(value, ".2f"))
        f_plot = self.master.master.canvas.plot
        f_plot.clear()
        if self.master.master.master.master.get() == "Pulse Input":
            v = 0
            # T = self.master.slider_block.frame[2].x.get()
            T = value
            self.master.master.canvas.f.figure

            o_np = one_order(v, T)
            x = np.linspace(0, 10, 100)
            f_plot.plot(x, o_np(x))
            legend_pulse.append("v=%s,T=%s" % (str(v), str(T)))
            f_plot.legend(legend_pulse)
            self.master.master.canvas.Canvas.draw()
