import customtkinter
from core import one_order
import numpy as np
import matplotlib.pyplot as plt

global legend_on
legend_on = []


class MyButton(customtkinter.CTkFrame):
    def __init__(self, master: any, **kwargs):
        super().__init__(master, **kwargs)
        self.switch_var = customtkinter.IntVar(value=1)
        self.button = [
            customtkinter.CTkButton(self, text="caculate", command=self.caculate),
            customtkinter.CTkButton(self, text="clear"),
            customtkinter.CTkSwitch(
                self,
                text="hold on",
                variable=self.switch_var,
                onvalue=1,
                offvalue=0,
                command=self.switch_plot,
            ),
        ]
        for i, j in enumerate(self.button):
            j.grid(row=0, column=i, padx=5, pady=20)

    def caculate(self):
        f_plot = self.master.canvas.plot
        canvas = self.master.canvas.Canvas
        tab_name = self.master.master.master
        if tab_name.get() == "Pulse Input":  # 之后会重新写
            v = 0
            T = self.master.slider_block.frame[2].x.get()
            self.master.canvas.f.figure
            o_np = one_order(v, T)
            x = np.linspace(0, 10, 100)
            f_plot.plot(x, o_np(x))
            legend_on.append("v=%s,T=%s" % (str(v), str(T)))
            f_plot.legend(legend_on)
            canvas.draw()

    def switch_plot(self):
        f_plot = self.master.canvas.plot
        f_plot.cla()
        self.master.canvas.Canvas.draw()
        if self.button[2].get() == 0:
            self.button[0].configure(state="disabled")
        if self.button[2].get() == 1:
            self.button[0].configure(state="normal")
