import logging

import customtkinter

from components.MySliderBlock import MySliderBlock


class Sin_MyOrder(customtkinter.CTkFrame):
    """
    具有多个 RadioButton 的组件
    :param title: 组件标签
    :param button_name: 按钮的名字列表，决定了按钮的数量
    """

    def __init__(
        self,
        master,
        title: str,
        button_name: list[str],
        ban: list[list[int]],
        sliderblock: MySliderBlock,
        **kwargs,
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
                command=self.callback,
                variable=self.selected,
                text=j,
                value=i,
            )
            for i, j in enumerate(button_name)
        ]
        for i, j in enumerate(self.orders):
            j.grid(row=i + 1, column=0, padx=5, pady=10)

        self.callback()  # 在界面开启时立即执行一次 callback，将 slider 禁用

    # 回调函数，禁用滑条与输入框
    def callback(self):
        logging.info("callback triggered， status:%d", self.selected.get())
        match self.selected.get():
            case 0:
                self.master.slider_block.set_enabled([False, False, True, True])
            case _:
                self.master.slider_block.set_enabled([True, True, False, True])
