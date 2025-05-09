import numpy as np


def inverted_pendulum_luenburger(t, X):
    # State variable x=[x; v; theta; omega]
    x = X[0:4]
    psi = X[4]

    g = 9.8
    l = 1
    m = 1
    M = 1

    d1 = M + m * (1 - np.cos(x[2]) ** 2)
    d2 = l * d1

    k = np.array([-40.0000, -37.3693, -190.6669, -54.7283])

    dpsi = -40.0 * x[0] - 37.37 * x[1] - 405.9 * x[2] - 58.73 * psi
    omega_h = psi + 4 * x[3]
    xh = np.array([x[0:3], omega_h])

    F = -np.dot(k, x)  # State feedback
    # F = -np.dot(k, xh)  # Luenberger Observer Feedback

    xp = np.array([
        x[1],
        (F + m * l * x[3] ** 2 * np.sin(x[2]) - m * g * np.sin(x[2]) * np.cos(x[2])) / d1,
        x[3],
        (-F * np.cos(x[2]) - m * l * x[3] ** 2 * np.sin(x[2]) * np.cos(x[2]) +
         (M + m) * g * np.sin(x[2])) / d2
    ])

    Xp = np.concatenate((xp, [dpsi]))

    return Xp
