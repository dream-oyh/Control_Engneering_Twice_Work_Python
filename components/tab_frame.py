import customtkinter
from components.Indicator import Indicator
from components.MyArgument import MyArgument
from components.MyButton import MyButton
from components.MyCanvas import MyCanvas
from components.MyOrder import MyOrder
from components.MySliderBlock import MySliderBlock


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
            MyOrder.set_disabled_one_order(sliderblock=self.sliblo, ban=[0, 1]),
            MyOrder.set_disabled_one_order(sliderblock=self.sliblo, ban=[2]),
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
