from typing import Optional, Tuple, Union
import customtkinter


class metric(customtkinter.CTkFrame):
    def __init__(self, master: any, text: list[str], **kwargs):
        super().__init__(master, **kwargs)
        self.metric_text = [customtkinter.CTkLabel(self, text=j) for j in text]
        self.metric_val = [customtkinter.CTkLabel(self, text="") for j in text]
        for i, j in enumerate(self.metric_text):
            j.grid(row=i, column=0, sticky="w")
        for i, j in enumerate(self.metric_val):
            j.grid(row=i, column=1, sticky="w")
