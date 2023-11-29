import customtkinter
from components.MySlider import MySlider


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
