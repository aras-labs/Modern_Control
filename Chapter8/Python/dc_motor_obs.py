

import numpy as np

# Define global parameters
class Parameters:
    def __init__(self, Tl):
        self.Tl = Tl

Par = Parameters(Tl=0.1)  # Example value for Tl

def DC_motor_Obs(t, X):
    # Extract state variables
    x = X[:3]
    xh = X[3:]

    # Real System Matrices
    A = np.array([[0, 1, 0],
                  [0, 0, 4.438],
                  [0, -12, -24]])
    B = np.array([[0, 0],
                  [0, -7.396],
                  [20, 0]])
    C = np.array([1, 0, 0])

    Tl = Par.Tl  # Step disturbance
    v = 0
    u = np.array([v, Tl])

    # Real System Model
    xp = A @ x + B @ u
    y = C @ x

    # Observer Matrices
    Ah = np.array([[0, 1, 0, 0],
                   [0, 0, 4.438, -7.396],
                   [0, -12, -24, 0],
                   [0, 0, 0, 0]])
    Bh = np.array([0, 0, 20, 0])
    Ch = np.array([1, 0, 0, 0])
    G = np.array([0, 234.7440, -936.9136, -27.6050])

    # Observer Model
    xhp = Ah @ xh + Bh * v + G * (y - Ch @ xh)

    # Augment the real and estimated states
    Xp = np.concatenate((xp, xhp))

    return Xp
