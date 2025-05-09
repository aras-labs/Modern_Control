import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint


# Define the function for the inverted pendulum dynamics
def inverted_pendulum_k2(x, t):
    # Parameters and system matrices
    A = np.array([[0, 0, 1, 0],
                  [0, 0, 0, 1],
                  [-10, 10, -2, 2],
                  [60, -660, 12, -12]])

    b1 = np.array([0, 0, 0.0033, -0.02])
    b2 = np.array([0, 0, 0, 600])
    B = np.column_stack((b1, b2))

    # Control input
    u = np.array([0])  # No control input defined in the MATLAB script

    # State-space equations
    xp = np.dot(A, x) + np.dot(B, u)

    return xp


# Initial conditions and time span
x0 = np.array([0, 0, 0.6, 0])
t = np.linspace(0, 3, 301)  # Time points for simulation

# Solve the differential equation using odeint
x = odeint(inverted_pendulum_k2, x0, t)

# Plot the results
plt.plot(t, x[:, 0], 'k', label='x (m)')
plt.plot(t, x[:, 2], '-.k', label='theta (rad)')
plt.grid(True)
plt.xlabel('Time (sec)')
plt.ylabel('State Variables')
plt.legend()
plt.show()
