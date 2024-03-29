import customtkinter
from core import Sin_one_order, Sin_two_order
from draw import draw_slider
import matplotlib.pyplot as plt
import numpy as np
from metric_caculate import update

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

    def draw_canvas(self, v, T, w, c):
        # T = self.master.slider_block.frame[2].x.get()

        global legend_on
        f_plot = self.master.master.canvas.plot
        Switch = self.master.master.button.button[2].get()
        canvas = self.master.master.canvas.Canvas
        # slider_block = self.master.master.slider_block
        status = self.master.master.order_panel.selected.get()
        metric = self.master.master.metric

        self.master.master.canvas.f.figure
        x, o_np = draw_slider(Switch, canvas, f_plot, status, v, T, w, c)
        if Switch == 0:
            update(metric, x, o_np)

    def sin_draw_canvas(self, T, omega, w, c):
        # T = self.master.slider_block.frame[2].x.get()

        global legend_on
        f_plot = self.master.master.canvas.plot
        self.master.master.canvas.f.figure
        if self.master.master.button.button[2].get() == 0:
            f_plot.clear()
        match self.master.master.order_panel.selected.get():
            case 0:
                o_np = Sin_one_order(omega, T)
                x = np.linspace(0, 10, 100)
                f_plot.plot(x, o_np(x))
                legend_on = ["omega=%s,T=%s" % (str(omega), str(format(T, ".2f")))]
                f_plot.legend(legend_on)
            case 1:
                o_np = Sin_two_order(omega, w, c)
                x = np.linspace(0, 10, 100)
                f_plot.plot(x, o_np(x))
                legend_on = ["omega=%s,w=%s,c=%s" % (str(omega), str(w), str(c))]
                f_plot.legend(legend_on)
        self.master.master.canvas.Canvas.draw()

    def caculate(self, value):
        self.x.set(format(value, ".2f"))
        # # f_plot = self.master.master.canvas.plot
        tab_name = self.master.master.master.master
        switch_val = self.master.master.button.button[2].get()
        status = self.master.master.order_panel.selected.get()
        for i, j in enumerate(["Pulse Input", "Step Input", "Slope Input"]):
            if tab_name.get() == j:
                if self.label._text == "w":
                    c = self.master.frame[1].x.get()
                    self.draw_canvas(v=i, w=value, c=c, T=0.01)
                if self.label._text == "阻尼度":
                    w = self.master.frame[0].x.get()
                    self.draw_canvas(v=i, w=w, c=value, T=0.01)
                if self.label._text == "T":
                    T = self.master.frame[2].x.get()
                    self.draw_canvas(v=i, T=T, w=0.01, c=0.01)
                    # self.draw_canvas(v=i, T=value, w=0.01, c=0.01)

        if (
            tab_name.get() == "Sin Input"
            and switch_val == 0
            and self.label._text == "固有频率"
            and status == 0
        ):
            T = self.master.frame[2].x.get()
            self.sin_draw_canvas(omega=value, T=T, w=0.01, c=0.01)

        if (
            tab_name.get() == "Sin Input"
            and switch_val == 0
            and self.label._text == "T"
            and status == 0
        ):
            omega = self.master.frame[3].x.get()
            self.sin_draw_canvas(omega=omega, T=value, w=0.01, c=0.01)
        # 二阶
        if (
            tab_name.get() == "Sin Input"
            and switch_val == 0
            and self.label._text == "固有频率"
            and status == 1
        ):
            w = self.master.frame[0].x.get()
            c = self.master.frame[1].x.get()
            self.sin_draw_canvas(omega=value, w=w, c=c, T=0.01)

        if (
            tab_name.get() == "Sin Input"
            and switch_val == 0
            and self.label._text == "w"
            and status == 1
        ):
            omega = self.master.frame[3].x.get()
            c = self.master.frame[1].x.get()
            self.sin_draw_canvas(omega=omega, w=value, c=c, T=0.01)

        if (
            tab_name.get() == "Sin Input"
            and switch_val == 0
            and self.label._text == "阻尼度"
            and status == 1
        ):
            omega = self.master.frame[3].x.get()
            w = self.master.frame[0].x.get()
            self.sin_draw_canvas(omega=omega, w=w, c=value, T=0.01)
