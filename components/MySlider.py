import customtkinter
from core import one_order
import matplotlib.pyplot as plt
import numpy as np

global legend_on
legend_on = []


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
        self.x_slider.configure(button_color="#3B8ED0" if state else "#94acb9")
        self.x_entry.configure(state="normal" if state else "disabled")
        self.x_entry.configure(text_color="#000000" if state else "#94acb9")

    # button_color="#94acb9",
    # text_color="#b0b6b9",

    def draw_canvas(self, T, v):
        # T = self.master.slider_block.frame[2].x.get()

        global legend_on
        f_plot = self.master.master.canvas.plot
        self.master.master.canvas.f.figure
        if self.master.master.button.button[2].get() == 0:
            f_plot.clear()
        o_np = one_order(v, T)
        x = np.linspace(0, 10, 100)
        f_plot.plot(x, o_np(x))
        if self.master.master.button.button[2].get() == 1:  # 需要hold on，需要比较不同T值的曲线
            legend_on.append("v=%s,T=%s" % (str(v), str(format(T, ".2f"))))
            f_plot.legend(legend_on)
        if self.master.master.button.button[2].get() == 0:
            legend_on = ["v=%s,T=%s" % (str(v), str(format(T, ".2f")))]
            f_plot.legend(legend_on)
        # legend_pulse.append("v=%s,T=%s" % (str(v), str(T)))
        self.master.master.canvas.Canvas.draw()

    def caculate(self, value):
        self.x.set(format(value, ".2f"))
        # # f_plot = self.master.master.canvas.plot
        tab_name = self.master.master.master.master
        switch_val = self.master.master.button.button[2]
        for i, j in enumerate(["Pulse Input", "Step Input", "Slope Input"]):
            if tab_name.get() == j and switch_val.get() == 0:
                self.draw_canvas(T=value, v=i)
        # f_plot = self.master.master.canvas.plot
        # f_plot.clear()
        # v = 0
        # # T = self.master.slider_block.frame[2].x.get()
        # T = value
        # self.master.master.canvas.f.figure

        # o_np = one_order(v, T)
        # x = np.linspace(0, 10, 100)
        # f_plot.plot(x, o_np(x))
        # # legend_pulse.append("v=%s,T=%s" % (str(v), str(T)))
        # legend_pulse = ["v=%s,T=%s" % (str(v), str(format(T, ".2f")))]
        # f_plot.legend(legend_pulse)
        # self.master.master.canvas.Canvas.draw()
