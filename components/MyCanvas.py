import customtkinter
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure


class MyPlotNavigation(customtkinter.CTkFrame):
    def __init__(self, master: any, canvas, height=250, width=30, **kwargs):
        kwargs = {"fg_color": master._fg_color, **kwargs}
        super().__init__(master, height, width, **kwargs)
        self.toolbar = NavigationToolbar2Tk(canvas, self)
        self.toolbar.place(x=190, y=20, anchor=customtkinter.CENTER)


class MyCanvas(customtkinter.CTkFrame):
    def __init__(self, master: any, **kwargs):
        super().__init__(master, **kwargs)
        self.f = Figure(figsize=(6, 6), dpi=100)
        plot = self.f.add_subplot(111)
        plot.grid()

        self.Canvas = FigureCanvasTkAgg(self.f, self)
        self.Canvas.get_tk_widget().grid(row=0, column=0, padx=20, pady=20)
        self.toolbar = MyPlotNavigation(self, canvas=self.Canvas)
        self.toolbar.grid(row=1, column=0, padx=20, pady=20)
