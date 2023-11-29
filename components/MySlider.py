import customtkinter


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
