import numpy as np
from scipy.integrate import odeint


# Global parameter
class Par:
    Tl = 0.01  # Step disturbance torque parameter


# Function defining the dynamics of the DC motor and observer
def DC_motor_Obs(t, X):
    global Par

    # System matrices
    A = np.array([[0, 1, 0],
                  [0, 0, 4.438],
                  [0, -12, -24]])

    B = np.array([[0, 0],
                  [0, -7.396],
                  [20, 0]])

    C = np.array([[1, 0, 0]])

    # Observer matrices
    Ah = np.array([[0, 1, 0, 0],
                   [0, 0, 4.438, -7.396],
                   [0, -12, -24, 0],
                   [0, 0, 0, 0]])

    Bh = np.array([[0], [0], [20], [0]])

    Ch = np.array([[1, 0, 0, 0]])

    # Observer gain matrix
    G = np.array([[0, 234.7440, -936.9136, -27.6050]]).T

    # Extract states from input vector X
    x = X[:3]  # [θ, ω, i]
    xh = X[3:]  # [θ_hat, ω_hat, i_hat, Tl_hat]

    # Step disturbance torque
    Tl = Par.Tl

    # Control input [v; Tl]
    v = 0  # Since v is not used in the observer model

    # State equations
    xp = np.dot(A, x) + np.dot(B, np.array([v, Tl]))
    y = np.dot(C, x)

    # Observer update equation
    xhp = np.dot(Ah, xh) + np.dot(Bh, v) + np.dot(G, (y - np.dot(Ch, xh)))

    # Augment the real and estimated states
    Xp = np.concatenate((xp, xhp))

    return Xp
