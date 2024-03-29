import customtkinter
from core import one_order, Sin_one_order, two_order, Sin_two_order
from draw import draw
import numpy as np
import matplotlib.pyplot as plt
from metric_caculate import update

global legend_on
legend_on = []


class MyButton(customtkinter.CTkFrame):
    def __init__(self, master: any, **kwargs):
        super().__init__(master, **kwargs)
        self.switch_var = customtkinter.IntVar(value=1)
        self.button = [
            customtkinter.CTkButton(self, text="caculate", command=self.draw_canvas),
            customtkinter.CTkButton(self, text="clear", command=self.clear),
            customtkinter.CTkSwitch(
                self,
                text="hold on",
                variable=self.switch_var,
                onvalue=1,
                offvalue=0,
                command=self.switch_disabled,
            ),
        ]
        for i, j in enumerate(self.button):
            j.grid(row=0, column=i, padx=5, pady=20)

    def caculate(self, v):
        f_plot = self.master.canvas.plot
        canvas = self.master.canvas.Canvas
        # tab_name = self.master.master.master
        # if tab_name.get() == "Pulse Input":  # 之后会重新写
        self.master.canvas.f.figure
        status = self.master.order_panel.selected.get()
        slider_block = self.master.slider_block
        metric = self.master.metric

        x, o_np = draw(canvas, f_plot, slider_block, status, v)
        update(metric, x, o_np)

    def sin_caculate(self, omega, T, w, c):
        f_plot = self.master.canvas.plot
        canvas = self.master.canvas.Canvas
        tab_name = self.master.master.master
        match self.master.order_panel.selected.get():
            case 0:
                self.master.canvas.f.figure
                o_np = Sin_one_order(omega, T)
                x = np.linspace(0, 10, 100)
                f_plot.plot(x, o_np(x))
                legend_on.append("omega=%s,T=%s" % (str(omega), str(T)))
                f_plot.legend(legend_on)
            case 1:
                self.master.canvas.f.figure
                o_np = Sin_two_order(omega, w, c)
                x = np.linspace(0, 10, 100)
                f_plot.plot(x, o_np(x))
                legend_on.append("omega=%s,w=%s, c=%s" % (str(omega), str(w), str(c)))
                f_plot.legend(legend_on)
        canvas.draw()

    def switch_disabled(self):
        f_plot = self.master.canvas.plot
        f_plot.cla()
        legend_on = []
        self.master.canvas.Canvas.draw()
        if self.button[2].get() == 0:
            self.button[0].configure(state="disabled")
        if self.button[2].get() == 1:
            self.button[0].configure(state="normal")

    def draw_canvas(self):
        tab_name = self.master.master.master
        w = self.master.slider_block.frame[0].x.get()
        c = self.master.slider_block.frame[1].x.get()
        T = self.master.slider_block.frame[2].x.get()

        for i, j in enumerate(["Pulse Input", "Step Input", "Slope Input"]):
            if tab_name.get() == j:  # 之后会重新写
                self.caculate(v=i)
        if tab_name.get() == "Sin Input":
            omega = self.master.slider_block.frame[3].x.get()
            self.sin_caculate(omega=omega, T=T, w=w, c=c)

    def clear(self):
        f_plot = self.master.canvas.plot
        f_plot.cla()
        self.master.canvas.Canvas.draw()
