import logging

import customtkinter

from components.TabView import MyTab


class App(customtkinter.CTk):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.tab_view = MyTab(master=self, width=1000, height=500)
        self.tab_view.grid(row=0, column=0, padx=20, pady=20)


customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("blue")
logging.basicConfig(level=logging.INFO)
app = App()
app.title("The parameter changes impact on arbitrary order system output")
app.geometry("1100x650+100+50")
app.mainloop()
