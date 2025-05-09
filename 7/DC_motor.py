import numpy as np


# Define the function for the DC motor dynamics with disturbance
def DC_motor_w(t, x):
    # Parameters and system matrices
    A = np.array([[0, 1, 0, 0],
                  [0, 0, 4.438, -7.396],
                  [0, -12, -24, 0],
                  [0, 0, 0, -1]])

    B = np.array([[0, 0],
                  [0, -7.396],
                  [20, 0],
                  [0, 0]])

    k = np.array([3.0000, 0.8796, 0.1529, -1.8190])

    theta_d = 0  # Desired angular position
    Tl = 0.01  # Step disturbance

    # Calculate control input v1
    v1 = 2.255 * Tl - k[0] * (x[0] - theta_d) - k[1] * x[1] - k[2] * x[2]

    # Calculate control input v2 (assuming this was intended)
    v2 = 2.255 * Tl - np.dot(k, x)

    u = np.array([v1, Tl])

    # State-space equations
    xp = np.dot(A, x) + np.dot(B, u)

    return xp
