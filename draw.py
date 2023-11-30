import customtkinter
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import numpy as np
from sympy import *
from sympy.abc import t, s
from core import one_order, Sin_one_order, two_order

global legend_on
legend_on = []


def draw(canvas, f_plot, slider_block, status, v):
    if status == 0:
        T = slider_block.frame[2].x.get()
        o_np = one_order(v, T)
    if status == 1:
        w = slider_block.frame[0].x.get()
        c = slider_block.frame[1].x.get()
        o_np = two_order(v, w, c)
    x = np.linspace(0, 10, 100)
    f_plot.plot(x, o_np(x))
    if status == 0:
        legend_on.append("v=%s,T=%s" % (str(v), str(T)))
    if status == 1:
        legend_on.append("v = %s,w=%s,ksai=%s" % (str(v), str(w), str(c)))
    f_plot.legend(legend_on)
    canvas.draw()


def draw_slider(Switch, canvas, f_plot, status, v, T, w, c):
    if status == 0:
        o_np = one_order(v, T)
    if status == 1:
        o_np = two_order(v, w, c)
    if Switch == 0:
        f_plot.clear()
        x = np.linspace(0, 10, 100)
        f_plot.plot(x, o_np(x))

        if status == 0:  # 不需要hold on 也一阶
            legend_on = ["v=%s,T=%s" % (str(v), str(format(T, ".2f")))]
            f_plot.legend(legend_on)
        if status == 1:  # 不需要hold—on 但是二阶
            legend_on = [
                "v = %s,w=%s,ksai=%s"
                % (str(v), str(format(w, ".2f")), str(format(c, ".2f")))
            ]
            f_plot.legend(legend_on)
        canvas.draw()
