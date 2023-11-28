from typing import Optional, Tuple, Union
import customtkinter
import matplotlib.pyplot as plt
from customtkinter.windows.widgets.font import CTkFont
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
from PIL import Image


# create the class for curve canvas
# including canvas and toolbar


class MyToolbar(customtkinter.CTkFrame):
    def __init__(self, master: any, canvas, height=250, width=30, **kwargs):
        super().__init__(master, height, width, **kwargs)
        self.toolbar = NavigationToolbar2Tk(canvas, self)
        self.toolbar.place(x=190, y=20, anchor=customtkinter.CENTER)


class Canvas(customtkinter.CTkFrame):
    def __init__(self, master: any, **kwargs):
        super().__init__(master, **kwargs)
        self.f = Figure(figsize=(6, 6), dpi=100)
        plot = self.f.add_subplot(111)
        plot.grid()

        self.Canvas = FigureCanvasTkAgg(self.f, self)
        self.Canvas.get_tk_widget().grid(row=0, column=0, padx=20, pady=20)
        self.toolbar = MyToolbar(self, canvas=self.Canvas)
        self.toolbar.grid(row=1, column=0, padx=20, pady=20)
        # self.toolbar = NavigationToolbar2Tk(self.Canvas, self)
        # self.toolbar.grid(row=1, column=0, padx=20, pady=20)


# create the mode metric
# add the image route and text name to note the signal shape
class ModeImg(customtkinter.CTkFrame):
    def __init__(self, master: any, text, img, **kwargs):
        super().__init__(master, **kwargs)
        self.label = customtkinter.CTkLabel(self, text=text)
        self.label.grid(row=0, column=0, padx=20, pady=20)

        self.img = customtkinter.CTkImage(Image.open(img), size=(100, 100))
        self.label_img = customtkinter.CTkLabel(
            self, image=self.img, text="", width=50, height=50
        )
        self.label_img.grid(row=0, column=1, padx=20, pady=20)


# create the class to choose the order one or two
class OrderOption(customtkinter.CTkFrame):
    def __init__(self, master: any, **kwargs):
        super().__init__(master, **kwargs)
        self._border_width = 1
        self._border_color = "black"
        self.label = customtkinter.CTkLabel(self, text="Order option:")
        self.label.grid(row=0, column=0, padx=20, pady=20)
        self.if_one_order = customtkinter.IntVar(value=0)

        def one_order_fun():
            print(self.if_one_order.get())

        self.one_order = customtkinter.CTkRadioButton(
            self,
            value=1,
            variable=self.if_one_order,
            command=one_order_fun,
            text="One order system",
        )
        self.two_order = customtkinter.CTkRadioButton(
            self,
            value=0,
            variable=self.if_one_order,
            command=one_order_fun,
            text="Two order system",
        )

        self.one_order.grid(row=1, column=0, padx=20, pady=20)
        self.two_order.grid(row=2, column=0, padx=20, pady=20)


class MySlider(customtkinter.CTkFrame):
    def __init__(self, master: any, text, max, min, **kwargs):
        super().__init__(master, **kwargs)
        # label
        self.label = customtkinter.CTkLabel(self, text=text)
        self.label.grid(row=0, column=0, padx=20, pady=20, sticky="w")

        # slider
        self.x = customtkinter.DoubleVar(value=0.01)
        self.x_slider = customtkinter.CTkSlider(
            self, variable=self.x, from_=min, to=max
        )
        self.x_slider.grid(row=0, column=1, padx=20, pady=20, columnspan=2, sticky="w")
        # entry
        self.x_entry = customtkinter.CTkEntry(self, textvariable=self.x)
        self.x_entry.grid(row=0, column=3, padx=20, pady=20, sticky="w")
        if self.x_entry.get() == "":
            self.x = 0


class MyButton(customtkinter.CTkFrame):
    def __init__(self, master: any, **kwargs):
        super().__init__(master, **kwargs)
        self.caculate = customtkinter.CTkButton(self, text="caculate")
        self.clear = customtkinter.CTkButton(self, text="clear")
        self.hold_on = customtkinter.CTkButton(self, text="hold on")
        self.caculate.grid(row=0, column=0, padx=20, pady=20)
        self.clear.grid(row=0, column=1, padx=20, pady=20)
        self.hold_on.grid(row=0, column=2, padx=20, pady=20)


class MyArgument(customtkinter.CTkScrollableFrame):
    def __init__(self, master: any, **kwargs):
        super().__init__(master, **kwargs)
        self.argument_display = customtkinter.CTkLabel(self, text="超调量： \n 收敛时间：")
        self.argument_display.grid(row=0, column=0, padx=20, pady=20)


class MyTab(customtkinter.CTkTabview):
    def __init__(self, master: any, **kwargs):
        super().__init__(master, **kwargs)
        Pulse = self.add("Pulse Input")
        Slope = self.add("Slope Input")
        Step = self.add("Step Input")
        Sin = self.add("Sin Input")

        # self.ModeImg1 = ModeImg(
        #     master=Pulse, text="Pulse Signal Plot: ", img="img/pulse_signal.png"
        # )
        self.ModeImg1 = ModeImg(
            master=Pulse, text="Pulse Signal Plot", img="img/Pulse_signal.png"
        )
        self.ModeImg1.grid(row=0, column=0)
        self.OrderOpt = OrderOption(Pulse)
        self.OrderOpt.grid(row=1, column=0)
        self.Omega_Slider = MySlider(Pulse, text="w", max=10, min=0)
        self.Omega_Slider.grid(row=2, column=0, sticky="e")
        self.Ksai_Slider = MySlider(Pulse, text="阻尼度", max=2, min=0)
        self.Ksai_Slider.grid(row=3, column=0, sticky="e")
        self.T_Slider = MySlider(Pulse, text="T", max=10, min=0)
        self.T_Slider.grid(row=4, column=0, sticky="e")
        self.Button = MyButton(Pulse)
        self.Button.grid(row=5, column=0, sticky="w")
        self.Argument = MyArgument(Pulse)
        self.Argument.grid(row=0, column=1, rowspan=3, sticky="wn")
        self.canvas_plot = Canvas(Pulse)
        self.canvas_plot.grid(row=0, column=2, rowspan=4, columnspan=3, sticky="w")


class App(customtkinter.CTk):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.Tabview = MyTab(self)
        self.Tabview.grid(row=0, column=0)


app = App()
app.title("The parameter changes impact on arbitrary order system output")
app.mainloop()
