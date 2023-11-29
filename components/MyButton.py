import customtkinter


class MyButton(customtkinter.CTkFrame):
    def __init__(self, master: any, **kwargs):
        super().__init__(master, **kwargs)
        self.caculate = customtkinter.CTkButton(self, text="caculate")
        self.clear = customtkinter.CTkButton(self, text="clear")
        self.hold_on = customtkinter.CTkButton(self, text="hold on")
        self.caculate.grid(row=0, column=0, padx=20, pady=20)
        self.clear.grid(row=0, column=1, padx=20, pady=20)
        self.hold_on.grid(row=0, column=2, padx=20, pady=20)
