import numpy as np
from scipy.integrate import odeint


# Global parameters
class Par:
    Tl = 0.01  # Disturbance torque parameter


# Function defining the dynamics of the DC motor and observer
def DC_motor_LTR1(t, X):
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
                   [0, 0, 0, -1]])

    Bh = np.array([[0], [0], [20], [0]])

    Ch = np.array([[1, 0, 0, 0]])

    # State feedback and observer gains
    k = np.array([3.0000, 0.8796, 0.1529, -1.8190])
    G = np.array([[-1.0000], [235.7440], [-978.1707], [-20.4870]])

    # Extract states from input vector X
    x = X[:3]  # [θ, ω, i]
    xh = X[3:]  # [θ, ω, i, Tl]

    # Desired angular position (not used in this example)
    theta_d = 0

    # Exponential disturbance torque
    Tl = Par.Tl * np.exp(-t)

    # State feedback control law
    v = -np.dot(k, xh)

    # Control input [v; Tl]
    u = np.array([v, Tl])

    # Observer update equation
    xhp = np.dot(Ah, xh) + np.dot(Bh, v) + np.dot(G.T, (np.dot(C.T, x) - np.dot(Ch, xh)))

    # System dynamics
    xp = np.dot(A, x) + np.dot(B, u)

    # Combined state derivatives
    Xp = np.concatenate((xp, xhp))

    return Xp


# Initial conditions and time span
X0 = np.array([0, 0, 0, 0, 0, 0, 0])  # Initial state [θ, ω, i, θ_hat, ω_hat, i_hat, Tl_hat]
t_span = np.linspace(0, 5, 500)  # Time span for simulation

# Solve the ODE system
sol = odeint(DC_motor_LTR1, X0, t_span)

# Extract results
theta = sol[:, 0]
omega = sol[:, 1]
current = sol[:, 2]

# Display or plot results as needed
