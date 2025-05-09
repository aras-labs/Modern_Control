import numpy as np


def inverted_pendulum_k1(t, x):
    # Parameters
    g = 9.8
    l = 1
    m = 1
    M = 1

    # State feedback gains (taken from the MATLAB code)
    k = [-16.0203, -15.2428, -98.6852, -28.1028]

    # Compute control input F (state feedback)
    F = -np.dot(k, x)

    # Intermediate variables for dynamics
    d1 = M + m * (1 - np.cos(x[2]) ** 2)
    d2 = l * d1

    # State equations
    xp = np.array([
        x[1],
        (F + m * l * x[3] ** 2 * np.sin(x[2]) - m * g * np.sin(x[2]) * np.cos(x[2])) / d1,
        x[3],
        (-F * np.cos(x[2]) - m * l * x[3] ** 2 * np.sin(x[2]) * np.cos(x[2])
         + (M + m) * g * np.sin(x[2])) / d2
    ])

    return xp
