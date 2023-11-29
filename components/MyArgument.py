import customtkinter


class MyArgument(customtkinter.CTkFrame):
    def __init__(self, master: any, **kwargs):
        super().__init__(master, **kwargs)
        self.argument_display = customtkinter.CTkLabel(
            self, text="超调量： \n 收敛时间：", width=420, height=50
        )
        self.argument_display.grid(row=0, column=0, padx=5, pady=10, sticky="wn")
