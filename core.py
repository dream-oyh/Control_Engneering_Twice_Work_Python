import customtkinter
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import numpy as np
from sympy import *
from sympy.abc import t, s


def one_order(v, T):
    fun_input = 1 / s**v
    G = 1 / (T * s + 1)
    o = inverse_laplace_transform(fun_input * G, s, t)
    o_np = lambdify(t, o, "numpy")
    return o_np


def Sin_one_order(omega: float, T):
    sin_input = omega / (s**2 + omega**2)
    G = 1 / (T * s + 1)
    out = inverse_laplace_transform(sin_input * G, s, t)
    out_np = lambdify(t, out, "numpy")
    return out_np


def two_order(v, w, c):
    fun_input = 1 / s**v
    G = w / (s**2 + 2 * c * w * s + w**2)
    out = inverse_laplace_transform(fun_input * G, s, t)
    out_np = lambdify(t, out, "numpy")
    return out_np


def Sin_two_order(omega: float, w, c):
    sin_input = omega / (s**2 + omega**2)
    G = w / (s**2 + 2 * c * w * s + w**2)
    out = inverse_laplace_transform(sin_input * G, s, t)
    out_np = lambdify(t, out, "numpy")
    return out_np


# a = Figure(figsize=(6.4, 6.4), dpi=100)
# v1 = 0
# v2 = 1
# T = 1
# T1 = one_order(v=v1, T=T)
# T1v0 = Sin_one_order(omega=v2, T=T)
# x = np.linspace(1, 10, 100)
# l1 = plt.plot(x, T1(x))
# l2 = plt.plot(x, T1v0(x))
# # plt.legend(
# #     handles=[l1, l2],
# #     labels=["v=%s,T=%s" % (str(v1), str(T)), "omega=%s,T=%s" % (str(v2), str(T))],
# # )
# plt.legend(
#     labels=["v=%s,T=%s" % (str(v1), str(T)), "omega=%s,T=%s" % (str(v2), str(T))],
# )
# plt.show()

# a = Figure(figsize=(6.4, 6.4), dpi=100)
# f = (1) / (1 * s + 1)
# F = inverse_laplace_transform(f, s, t)
# F_np = lambdify(t, F, "numpy")
# x = np.linspace(0, 10, 100)
# l = plt.plot(x, F_np(x), label="sss")
# plt.legend()
# plt.show()
