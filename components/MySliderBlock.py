import customtkinter

from components.MySlider import MySlider


class MySliderBlock(customtkinter.CTkFrame):
    """
    多个 slider 组成的 slider block
    """

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
        assert len(text) == len(max) and len(text) == len(
            min
        ), "arguments must have same length"
        self.frame = [MySlider(self, *i) for i in zip(text, max, min)]
        for i, j in enumerate(self.frame):
            j.grid(row=i + 1, column=0, padx=20, pady=5, sticky="e")

    def set_enabled(self, enabled: list[bool]):
        assert len(enabled) == len(self.frame), "arguments must have same length"
        for i, j in enumerate(self.frame):
            j.set_enabled(enabled[i])
