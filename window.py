from typing import Callable, Optional, Tuple, Union

import customtkinter
import matplotlib.pyplot as plt
from customtkinter.windows.widgets.font import CTkFont
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
from PIL import Image

from components.MyOrder import MyOrder


class MyTabView(customtkinter.CTkTabview):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # 定义各个tab名称
        Pulse_Input = self.add("Pulse Input")  # 脉冲
        Slope_Input = self.add("Slope Input")  # 斜坡
        Step_Input = self.add("Step Input")  # 跃迁
        Sin_Input = self.add("Sin Input")  # 正弦

        fig_width = 6
        fig_height = 6
        dpi = 100
        # 创建曲线图
        # 脉冲
        Pulse_fig = Figure(figsize=(fig_width, fig_height), dpi=dpi)
        Pulse_plot = Pulse_fig.add_subplot(111)
        Pulse_plot.grid()
        # 斜坡
        Slope_fig = Figure(figsize=(fig_width, fig_height), dpi=dpi)
        Slope_plot = Slope_fig.add_subplot(111)
        Slope_plot.grid()
        # 跃迁
        Step_fig = Figure(figsize=(fig_width, fig_height), dpi=dpi)
        Step_plot = Step_fig.add_subplot(111)
        Step_plot.grid()
        # 正弦
        Sin_fig = Figure(figsize=(fig_width, fig_height), dpi=dpi)
        Sin_plot = Sin_fig.add_subplot(111)
        Sin_plot.grid()
        # 创建canvas
        # 脉冲canvas
        Pulse_Canvas = FigureCanvasTkAgg(Pulse_fig, Pulse_Input)
        # 斜坡canvas
        Slope_Canvas = FigureCanvasTkAgg(Slope_fig, Slope_Input)
        # 跃迁canvas
        Step_Canvas = FigureCanvasTkAgg(Step_fig, Step_Input)
        # 正弦canvas
        Sin_Canvas = FigureCanvasTkAgg(Sin_fig, Sin_Input)

        # 放置canvas
        # pulse canvas
        Pulse_Canvas.get_tk_widget().place(x=1200, y=300, anchor=customtkinter.CENTER)
        # slope canvas
        Slope_Canvas.get_tk_widget().place(x=1200, y=300, anchor=customtkinter.CENTER)
        # step canvas
        Step_Canvas.get_tk_widget().place(x=1200, y=300, anchor=customtkinter.CENTER)
        # sin canvas
        Sin_Canvas.get_tk_widget().place(x=1200, y=300, anchor=customtkinter.CENTER)

        # put toolbar
        Pulse_toolbar = NavigationToolbar2Tk(Pulse_Canvas, Pulse_Input)
        Slope_toolbar = NavigationToolbar2Tk(Slope_Canvas, Slope_Input)
        Step_toolbar = NavigationToolbar2Tk(Step_Canvas, Step_Input)
        Sin_toolbar = NavigationToolbar2Tk(Sin_Canvas, Sin_Input)

        Pulse_toolbar.place(x=1100, y=620, width=230, height=40)
        Slope_toolbar.place(x=1100, y=620, width=230, height=40)
        Step_toolbar.place(x=1100, y=620, width=230, height=40)
        Sin_toolbar.place(x=1100, y=620, width=230, height=40)

        # put corresponding image
        # Pulse signal img
        Pulse_signal_img = customtkinter.CTkImage(
            Image.open("img/pulse_signal.png"), size=(100, 100)
        )
        Pulse_signal_label_for_image = customtkinter.CTkLabel(
            Pulse_Input,
            image=Pulse_signal_img,
            text="",
            width=50,
            height=50,
        )
        Pulse_signal_label = customtkinter.CTkLabel(
            Pulse_Input, text="Pulse signal plot:"
        )
        Pulse_signal_label_for_image.place(x=130, y=5)
        Pulse_signal_label.place(x=20, y=30)
        # slope signal image
        Slope_signal_img = customtkinter.CTkImage(
            Image.open("img/slope_signal.png"), size=(100, 100)
        )
        Slope_signal_label_for_image = customtkinter.CTkLabel(
            Slope_Input,
            image=Slope_signal_img,
            text="",
            width=50,
            height=50,
        )
        Slope_signal_label = customtkinter.CTkLabel(
            Slope_Input, text="Slope signal plot:"
        )
        Slope_signal_label_for_image.place(x=130, y=5)
        Slope_signal_label.place(x=20, y=30)

        # step signal image
        Step_signal_img = customtkinter.CTkImage(
            Image.open("img/step_signal.png"), size=(100, 100)
        )
        Step_signal_label_for_image = customtkinter.CTkLabel(
            Step_Input,
            image=Step_signal_img,
            text="",
            width=50,
            height=50,
        )
        Step_signal_label = customtkinter.CTkLabel(Step_Input, text="Step signal plot:")
        Step_signal_label_for_image.place(x=130, y=5)
        Step_signal_label.place(x=20, y=30)

        # sin signal image
        Sin_signal_img = customtkinter.CTkImage(
            Image.open("img/sin_signal.png"), size=(100, 100)
        )
        Sin_signal_label_for_image = customtkinter.CTkLabel(
            Sin_Input,
            image=Sin_signal_img,
            text="",
            width=50,
            height=50,
        )
        Sin_signal_label = customtkinter.CTkLabel(Sin_Input, text="Sin signal plot:")
        Sin_signal_label_for_image.place(x=130, y=5)
        Sin_signal_label.place(x=20, y=30)

        # put CTkRadioButton
        # pulse
        Pulse_order = MyOrder(
            Pulse_Input,
            title="Pulse_order",
            button_name=["test1", "Test2"],
        )
        Pulse_order.place(x=50, y=120)
        # slope
        Slope_order = MyOrder(
            Slope_Input,
            title="Slope_order",
            button_name=["Test1", "Test2", "Test3"],
        )
        Slope_order.place(x=50, y=120)
        # step
        Step_order = MyOrder(
            Step_Input,
            title="Step_order",
            button_name=["Test1"],
        )
        Step_order.place(x=50, y=120)
        # sin
        Sin_order = MyOrder(
            Sin_Input,
            title="Sin_order",
            button_name=["Test1", "Test2"],
        )
        Sin_order.place(x=50, y=120)
