import customtkinter as ctk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure

app = ctk.CTk()
app.geometry("670x700")


def fun():
    print(one_order_if.get())


frame = ctk.CTkFrame(app)
one_order_if = ctk.IntVar(value=0)
button1 = ctk.CTkRadioButton(
    frame, text="One_order", variable=one_order_if, value=0, command=fun
)
button2 = ctk.CTkRadioButton(
    frame, text="Two_order", variable=one_order_if, value=1, command=fun
)
button1.grid(row=0, column=0)
button2.grid(row=1, column=0)
frame.grid(row=0, column=0)


app.mainloop()
