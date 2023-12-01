import numpy as np
from components.metric import metric


def chaotiao(o_np):
    return np.max(np.abs(o_np))


def tp(x, o_np):
    return x[np.argmax(np.abs(o_np))]


def tr(x, o_np):
    return x[np.min(np.argmin(np.abs(o_np - 1)))]


def ts(x: np.ndarray, o_np):
    i = 0
    while sum(o_np[i:99] >= 0.02) != 0:
        i = i + 1
    return x[i]


def ts_step(T):
    return 4 * T


def update(metric: metric, x, o_np):
    metric.metric_val[0].configure(text=str(format(chaotiao(o_np), ".2f")))
    metric.metric_val[1].configure(text=str(format(tr(x, o_np), ".2f")))
    metric.metric_val[2].configure(text=str(format(tp(x, o_np), ".2f")))
    if metric.master.master.master.get() == "Step Input":
        T = metric.master.slider_block.frame[2].x.get()
        metric.metric_val[3].configure(text=str(format(4 * T, ".2f")))
    else:
        metric.metric_val[3].configure(text=str(format(ts(x, o_np), ".2f")))
