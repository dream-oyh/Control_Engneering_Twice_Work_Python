from typing import Optional, Tuple, Union
import customtkinter
from PIL import Image
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure


class Indicator(customtkinter.CTkFrame):
    def __init__(self, master: any, text: str, img_path: str, **kwargs):
        super().__init__(master, **kwargs)
        self.label = customtkinter.CTkLabel(self, text=text)
        self.label.grid(row=0, column=0, padx=0, pady=0)

        self.img = customtkinter.CTkImage(Image.open(img_path), size=(100, 100))
        self.label_img = customtkinter.CTkLabel(
            self, image=self.img, text="", width=50, height=50
        )
        self.label_img.grid(row=1, column=0, padx=10, pady=0)


class MyArgument(customtkinter.CTkFrame):
    def __init__(self, master: any, **kwargs):
        super().__init__(master, **kwargs)
        self.argument_display = customtkinter.CTkLabel(
            self, text="超调量： \n 收敛时间：", width=420, height=50
        )
        self.argument_display.grid(row=0, column=0, padx=5, pady=10, sticky="wn")


class MyButton(customtkinter.CTkFrame):
    def __init__(self, master: any, **kwargs):
        super().__init__(master, **kwargs)
        self.caculate = customtkinter.CTkButton(self, text="caculate")
        self.clear = customtkinter.CTkButton(self, text="clear")
        self.hold_on = customtkinter.CTkButton(self, text="hold on")
        self.caculate.grid(row=0, column=0, padx=20, pady=20)
        self.clear.grid(row=0, column=1, padx=20, pady=20)
        self.hold_on.grid(row=0, column=2, padx=20, pady=20)


class MyCanvas(customtkinter.CTkFrame):
    def __init__(self, master: any, **kwargs):
        super().__init__(master, **kwargs)
        self.f = Figure(figsize=(6, 6), dpi=100)
        plot = self.f.add_subplot(111)
        plot.grid()

        self.Canvas = FigureCanvasTkAgg(self.f, self)
        self.Canvas.get_tk_widget().grid(row=0, column=0, padx=20, pady=20)
        self.toolbar = MyPlotNavigation(self, canvas=self.Canvas)
        self.toolbar.grid(row=1, column=0, padx=20, pady=20)


class MyPlotNavigation(customtkinter.CTkFrame):
    def __init__(self, master: any, canvas, height=250, width=30, **kwargs):
        kwargs = {"fg_color": master._fg_color}
        super().__init__(master, height, width, **kwargs)
        self.toolbar = NavigationToolbar2Tk(canvas, self)
        self.toolbar.place(x=190, y=20, anchor=customtkinter.CENTER)


class MySlider(customtkinter.CTkFrame):
    def __init__(self, master: any, text: str, max, min, **kwargs):
        kwargs = {"fg_color": master._fg_color}
        super().__init__(master, **kwargs)
        # label
        self.label = customtkinter.CTkLabel(self, text=text)
        # slider
        self.x = customtkinter.DoubleVar(value=0.01)

        def set_round(value):
            self.x.set(format(value, ".2f"))

        self.x_slider = customtkinter.CTkSlider(
            self, variable=self.x, from_=min, to=max, command=set_round
        )
        # entry
        self.x_entry = customtkinter.CTkEntry(self, textvariable=self.x)
        self.label.grid(row=0, column=0, padx=20, pady=20, sticky="w")
        self.x_slider.grid(row=0, column=1, padx=20, pady=20, columnspan=2, sticky="w")
        self.x_entry.grid(row=0, column=3, padx=20, pady=20, sticky="w")


class MySliderBlock(customtkinter.CTkFrame):
    def __init__(
        self,
        master: any,
        text: list[str],
        max: list[float],
        min: list[float],
        *a,
        **kwargs
    ):
        super().__init__(master, *a, **kwargs)
        """
        text: 需要的物理量列表
        max: 各物理量所需滑条最大值
        min: 各物理量所需滑条最小值
        """
        assert text.__len__() == max.__len__(), "text have not same size with max"
        assert max.__len__() == min.__len__(), "max have not same size with min"
        self.frame = [
            MySlider(self, text=text[i], max=max[i], min=min[i])
            for i in range(text.__len__())
        ]
        for i, j in enumerate(self.frame):
            j.grid(row=i + 1, column=0, padx=20, pady=5, sticky="e")


class MyOrder(customtkinter.CTkFrame):
    """
    具有多个 RadioButton 的组件
    :param title: 组件标签
    :param button_name: 按钮的名字列表，决定了按钮的数量
    """

    def __init__(
        self, master, title: str, button_name: list[str], command: list, **kwargs
    ):
        assert button_name, "button_name can not be empty"

        # border_color 与 border_width 具有默认值，且通过 kwargs 传参
        kwargs = {
            "border_color": "black",
            "border_width": 1,
            **kwargs,
        }
        super().__init__(master, **kwargs)
        self.label = customtkinter.CTkLabel(self, text=title)
        self.label.grid(row=0, column=0, padx=20, pady=10)

        # define one order or two orders
        self.selected = customtkinter.IntVar(value=0)
        self.orders = [
            customtkinter.CTkRadioButton(
                self,
                command=command[i],
                variable=self.selected,
                text=j,
                value=i,
            )
            for i, j in enumerate(button_name)
        ]
        for i, j in enumerate(self.orders):
            j.grid(row=i + 1, column=0, padx=5, pady=10)

    def set_disabled_one_order(sliderblock: MySliderBlock, ban: list[int]):
        # if self.orders[num]._value == num:
        for banner in ban:
            sliderblock.frame[banner].x_slider.configure(state="disabled")
            sliderblock.frame[banner].x_entry.configure(state="disabled")


class tab_frame(customtkinter.CTkFrame):
    def __init__(
        self,
        master: any,
        text: str,
        slidertext: str,
        max: list[float],
        min: list[float],
        img_path: str,
        **kwargs
    ):
        super().__init__(master, **kwargs)
        # Put indicator, orderoption, sliderblock, canvas, arguments
        self.indicator = Indicator(self, text=text, img_path=img_path)
        self.sliblo = MySliderBlock(self, text=slidertext, max=max, min=min)
        self.OptCommand = [
            MyOrder.set_disabled_one_order(sliderblock=self.sliblo),
            MyOrder.set_disabled_two_order(sliderblock=self.sliblo),
        ]
        self.orderopt = MyOrder(
            self,
            title="Order Option",
            button_name=["One Order System", "Two Order System"],
            command=self.OptCommand,
        )

        self.but = MyButton(self)
        self.can = MyCanvas(self)
        self.text = MyArgument(self)

        self.indicator.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.orderopt.grid(row=0, column=1, padx=10, pady=10, sticky="w")
        self.sliblo.grid(row=1, column=0, padx=10, pady=10, columnspan=2)
        self.but.grid(row=2, column=0, padx=10, pady=10, columnspan=2)
        self.can.grid(row=0, column=3, padx=10, pady=10, rowspan=2)
        self.text.grid(row=2, column=3, padx=10, pady=10)
