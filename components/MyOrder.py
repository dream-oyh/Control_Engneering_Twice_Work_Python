import customtkinter
import MySliderBlock


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

    # For test
    def set_disabled_one_order(sliderblock: MySliderBlock, ban: list[int]):
        # if self.orders[num]._value == num:
        for banner in ban:
            sliderblock.frame[banner].x_slider.configure(state="disabled")
            sliderblock.frame[banner].x_entry.configure(state="disabled")