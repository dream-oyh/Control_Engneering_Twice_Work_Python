import customtkinter

from window import MyTabView


class App(customtkinter.CTk):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.tab_view = MyTabView(master=self, width=1000, height=500)
        self.tab_view.grid(row=0, column=0, padx=20, pady=20)


app = App()
app.title("The parameter changes impact on arbitrary order system output")
app.mainloop()
