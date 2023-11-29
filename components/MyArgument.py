import customtkinter


class MyArgument(customtkinter.CTkFrame):
    """
    显示当前参数的 Label。
    可以传入 width, height 修改其属性。
    """

    def __init__(self, master: any, text: str, **kwargs):
        super().__init__(master, **kwargs)
        self.argument_display = customtkinter.CTkLabel(
            self,
            text=text,
            width=kwargs.get("width") or 420,
            height=kwargs.get("height") or 20,
        )
        self.argument_display.grid(row=0, column=0, padx=5, pady=10, sticky="wn")

    def set_text(self, s: str):
        self.argument_display.config(text=s)
