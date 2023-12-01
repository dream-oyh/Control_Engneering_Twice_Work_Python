import customtkinter

from .Indicator import Indicator
from .metric import metric
from .MyButton import MyButton
from .MyCanvas import MyCanvas
from .MyOrder import MyOrder
from .MySliderBlock import MySliderBlock


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
        assert len(max) == len(min), "arguments max and min must have same length"
        super().__init__(master, **kwargs)
        # Put indicator, orderoption, sliderblock, canvas, arguments
        self.indicator = Indicator(self, text=text, img_path=img_path)
        self.slider_block = MySliderBlock(self, text=slidertext, max=max, min=min)

        self.order_panel = MyOrder(
            self,
            title="Order Option",
            button_name=["One Order System", "Two Order System"],
            ban=[[0, 1], [2]],
            sliderblock=self.slider_block,
        )

        self.button = MyButton(self)
        self.canvas = MyCanvas(self)
        self.metric = metric(self, text=["超调量", "上升时间", "峰值时间", "调整时间"])
        self.indicator.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.order_panel.grid(row=0, column=1, padx=10, pady=10, sticky="w")
        self.slider_block.grid(row=1, column=0, padx=10, pady=10, columnspan=3)
        self.button.grid(row=2, column=0, padx=10, pady=10, columnspan=3)
        self.canvas.grid(row=0, column=4, padx=10, pady=10, rowspan=3)
        self.metric.grid(row=0, column=2, padx=10, pady=10, sticky="w")
