import customtkinter as ctk
import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure


def ini_fun():
    global y0, y1, y2, y3, y4, y5, y6, y7, y8, y9, inter_width, inter_width_entry, slope

    y0_label = tk.Label(root, text="y0").place(x=15, y=550, width=50, height=20)
    y1_label = tk.Label(root, text="y1").place(x=80, y=550, width=50, height=20)
    y2_label = tk.Label(root, text="y2").place(x=145, y=550, width=50, height=20)
    y3_label = tk.Label(root, text="y3").place(x=210, y=550, width=50, height=20)
    y4_label = tk.Label(root, text="y4").place(x=275, y=550, width=50, height=20)
    y5_label = tk.Label(root, text="y5").place(x=340, y=550, width=50, height=20)
    y6_label = tk.Label(root, text="y6").place(x=405, y=550, width=50, height=20)
    y7_label = tk.Label(root, text="y7").place(x=470, y=550, width=50, height=20)
    y8_label = tk.Label(root, text="y8").place(x=535, y=550, width=50, height=20)
    y9_label = tk.Label(root, text="y9").place(x=600, y=550, width=50, height=20)

    slope1_label = tk.Label(root, text="slope1").place(x=80, y=610, width=50, height=20)
    slope2_label = tk.Label(root, text="slope2").place(
        x=145, y=610, width=50, height=20
    )
    slope3_label = tk.Label(root, text="slope3").place(
        x=210, y=610, width=50, height=20
    )
    slope4_label = tk.Label(root, text="slope4").place(
        x=275, y=610, width=50, height=20
    )
    slope5_label = tk.Label(root, text="slope5").place(
        x=340, y=610, width=50, height=20
    )
    slope6_label = tk.Label(root, text="slope6").place(
        x=405, y=610, width=50, height=20
    )
    slope7_label = tk.Label(root, text="slope7").place(
        x=470, y=610, width=50, height=20
    )
    slope8_label = tk.Label(root, text="slope8").place(
        x=535, y=610, width=50, height=20
    )
    slope9_label = tk.Label(root, text="slope9").place(
        x=600, y=610, width=50, height=20
    )

    inter_width_label = tk.Label(root, text="inter_width:").place(
        x=100, y=650, width=70, height=20
    )
    inter_width_entry = tk.Entry(root)
    inter_width_entry.place(x=175, y=650, width=50, height=20)
    inter_width_entry.insert(1, "10")

    slope = ["0.0", "0.0", "0.0", "0.0", "0.0", "0.0", "0.0", "0.0", "0.0", "0.0"]
    (y0, y1, y2, y3, y4, y5, y6, y7, y8, y9) = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0)


def show_y():
    global y0_entry, y1_entry, y2_entry, y3_entry, y4_entry, y5_entry, y6_entry, y7_entry, y8_entry, y9_entry
    global y0, y1, y2, y3, y4, y5, y6, y7, y8, y9, inter_width
    y0_entry = tk.Entry(root)
    y0_entry.place(x=15, y=530, width=50, height=20)
    y0_entry.insert(1, y0)
    y1_entry = tk.Entry(root)
    y1_entry.insert(1, y1)
    y1_entry.place(x=80, y=530, width=50, height=20)
    y2_entry = tk.Entry(root)
    y2_entry.place(x=145, y=530, width=50, height=20)
    y2_entry.insert(1, y2)
    y3_entry = tk.Entry(root)
    y3_entry.place(x=210, y=530, width=50, height=20)
    y3_entry.insert(1, y3)
    y4_entry = tk.Entry(root)
    y4_entry.place(x=275, y=530, width=50, height=20)
    y4_entry.insert(1, y4)
    y5_entry = tk.Entry(root)
    y5_entry.place(x=340, y=530, width=50, height=20)
    y5_entry.insert(1, y5)
    y6_entry = tk.Entry(root)
    y6_entry.place(x=405, y=530, width=50, height=20)
    y6_entry.insert(1, y6)
    y7_entry = tk.Entry(root)
    y7_entry.place(x=470, y=530, width=50, height=20)
    y7_entry.insert(1, y7)
    y8_entry = tk.Entry(root)
    y8_entry.place(x=535, y=530, width=50, height=20)
    y8_entry.insert(1, y8)
    y9_entry = tk.Entry(root)
    y9_entry.place(x=600, y=530, width=50, height=20)
    y9_entry.insert(1, y9)


def show_slope():
    global slope

    slope1_num = tk.Label(root, text=slope[0], bg="#cccccc").place(
        x=80, y=590, width=50, height=20
    )
    slope2_num = tk.Label(root, text=slope[1], bg="#cccccc").place(
        x=145, y=590, width=50, height=20
    )
    slope3_num = tk.Label(root, text=slope[2], bg="#cccccc").place(
        x=210, y=590, width=50, height=20
    )
    slope4_num = tk.Label(root, text=slope[3], bg="#cccccc").place(
        x=275, y=590, width=50, height=20
    )
    slope5_num = tk.Label(root, text=slope[4], bg="#cccccc").place(
        x=340, y=590, width=50, height=20
    )
    slope6_num = tk.Label(root, text=slope[5], bg="#cccccc").place(
        x=405, y=590, width=50, height=20
    )
    slope7_num = tk.Label(root, text=slope[6], bg="#cccccc").place(
        x=470, y=590, width=50, height=20
    )
    slope8_num = tk.Label(root, text=slope[7], bg="#cccccc").place(
        x=535, y=590, width=50, height=20
    )
    slope9_num = tk.Label(root, text=slope[8], bg="#cccccc").place(
        x=600, y=590, width=50, height=20
    )


def get_num():
    global y0, y1, y2, y3, y4, y5, y6, y7, y8, y9, inter_width, inter_width_entry

    y0 = int(y0_entry.get())
    y1 = int(y1_entry.get())
    y2 = int(y2_entry.get())
    y3 = int(y3_entry.get())
    y4 = int(y4_entry.get())
    y5 = int(y5_entry.get())
    y6 = int(y6_entry.get())
    y7 = int(y7_entry.get())
    y8 = int(y8_entry.get())
    y9 = int(y9_entry.get())
    inter_width = int(inter_width_entry.get())


def calculate():
    global y0, y1, y2, y3, y4, y5, y6, y7, y8, y9, inter_width

    get_num()

    x = range(0, inter_width * 10, inter_width)
    y = [y0, y1, y2, y3, y4, y5, y6, y7, y8, y9]

    for k in range(0, 9):
        slope[k] = (y[k + 1] - y[k]) / inter_width
        slope[k] = round(slope[k], 1)

    show_slope()

    f_plot.clear()
    f_plot.plot(x, y)
    f_plot.grid()
    canvs.draw()


def clear():
    ini_fun()
    show_y()
    show_slope()


def main():
    global root, f, f_plot, canvs
    root = tk.Tk()
    root.geometry("670x700+30+30")
    root.title("tkinter and matplotlib")
    f = Figure(figsize=(6.4, 4.6), dpi=100)
    f_plot = f.add_subplot(111)
    f_plot.grid()

    canvs = FigureCanvasTkAgg(f, root)
    canvs.get_tk_widget().place(x=15, y=15)
    tk.Button(root, text="calculate", command=calculate).place(
        x=500, y=650, width=70, height=30
    )
    tk.Button(root, text="clear", command=clear).place(
        x=580, y=650, width=70, height=30
    )
    toolbar = NavigationToolbar2Tk(canvs, root)
    toolbar.place(x=15, y=475, width=200, height=40)
    y_frame = tk.Frame(root, highlightbackground="gray", highlightthickness=2).place(
        x=10, y=520, width=650, height=2
    )
    slope_frame = tk.Frame(
        root, highlightbackground="gray", highlightthickness=2
    ).place(x=60, y=580, width=600, height=2)
    button_frame = tk.Frame(
        root, highlightbackground="gray", highlightthickness=2
    ).place(x=60, y=640, width=600, height=2)

    ini_fun()
    show_y()
    show_slope()

    root.mainloop()


if __name__ == "__main__":
    main()
