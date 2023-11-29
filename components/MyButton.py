import customtkinter
from core import one_order
import numpy as np
import matplotlib.pyplot as plt


class MyButton(customtkinter.CTkFrame):
    def __init__(self, master: any, **kwargs):
        super().__init__(master, **kwargs)
        self.button = [
            customtkinter.CTkButton(self, text="caculate", command=self.caculate),
            customtkinter.CTkButton(self, text="clear"),
            customtkinter.CTkButton(self, text="hold on"),
        ]
        for i, j in enumerate(self.button):
            j.grid(row=0, column=i, padx=5, pady=20)

    def caculate(self):
        if self.master.master.master.get() == "Pulse Input":
            v = 0
            T = self.master.slider_block.frame[2].x.get()
            self.master.canvas.f.figure
            o_np = one_order(v, T)
            x = np.linspace(0, 10, 100)
            plt.plot(x, o_np(x))
            plt.legend(["v=%s,T=%s" % (str(v), str(T))])
            plt.show()
