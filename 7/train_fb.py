import numpy as np


def train_fb(t, x):
    # Parameters
    A = np.array([
        [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, -1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, -1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, -1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1, -1],
        [0, -12.5, 0, 0, 0, -0.75, 0.75, 0, 0, 0],
        [0, 62.5, -62.5, 0, 0, 3.75, -7.5, 3.75, 0, 0],
        [0, 0, 62.5, -62.5, 0, 0, 3.75, -7.5, 3.75, 0],
        [0, 0, 0, 62.5, -62.5, 0, 0, 3.75, -7.5, 3.75],
        [0, 0, 0, 0, 62.5, 0, 0, 0, 3.75, -3.75]
    ])

    b1 = np.array([0, 0, 0, 0, 0, 0.005, 0, 0, 0, 0]).reshape(-1, 1)  # Force input
    b2 = np.array([0, 0, 0, 0, 0, 250, 0, 0, 0, -1250]).reshape(-1, 1)  # Constant input

    vd = 25 * (1 - np.exp(-t / 40))

    # State feedback gains (taken from the MATLAB code)
    k = np.array([0.4559, 0.3331, 0.2170, 0.1069, 11.5387,
                  -0.2622, -0.3371, -0.3865, -0.4110, 5.3731]).reshape(-1, 1)

    dx = np.array([x[1] - 20, x[2] - 20, x[3] - 20, x[4] - 20]).reshape(-1, 1)
    dv = np.array([x[5] - vd, x[6] - vd, x[7] - vd, x[8] - vd, x[9] - vd]).reshape(-1, 1)
    z = x[5] - vd

    X = np.vstack((dx, dv, z))

    u = -np.dot(k.T, X)

    xp = np.dot(A, x) + np.dot(b1, u) + b2.flatten()

    return xp
