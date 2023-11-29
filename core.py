import customtkinter
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import sympy
from sympy import inverse_laplace_transform, exp, sin, plot
from sympy.abc import t, s, a


def one_order_ilaplace(v, T):
    """
    一阶系统的反拉普拉斯变换：
    v：决定信号类型，v=0单位脉冲响应，v=1单位阶跃响应，v=2单位斜坡响应
    T:时间常数
    """
    G_s = 1 / (T * s + 1)
    Signal = 1 / s**v
    Out = G_s * Signal
    F = inverse_laplace_transform(Out, s, t)
    return F


v = 0
T = 2
F = one_order_ilaplace(v, T)
f = Figure(figsize=(6, 6), dpi=100)
plota = f.add_subplot(111)
# t = sympy.Symbol("t")
plot(F, (t, 0, 10), label=["T=", str(T)])
plt.legend(loc="upper left")
