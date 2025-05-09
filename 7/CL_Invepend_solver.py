import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint


# Define the function for the inverted pendulum dynamics
def inverted_pendulum_k1(x, t):
    # Parameters
    m = 0.5  # Mass of the pendulum
    M = 1.0  # Mass of the cart
    L = 0.5  # Length to the center of mass of the pendulum
    g = 9.81  # Acceleration due to gravity

    # State variables
    theta = x[2]
    theta_dot = x[3]

    # Controller gains
    k1 = 8.1563
    k2 = 1.4653

    # State-space representation
    A = np.array([[0, 1, 0, 0],
                  [0, 0, -m * g / M, 0],
                  [0, 0, 0, 1],
                  [0, 0, (M + m) * g / (L * M), 0]])

    B = np.array([[0],
                  [1 / M],
                  [0],
                  [-1 / (L * M)]])

    C = np.array([[1, 0, 0, 0],
                  [0, 0, 1, 0]])

    D = np.zeros((2, 1))

    # Controller input
    u = -k1 * x[0] - k2 * x[1]

    # State-space equations
    dxdt = np.dot(A, x) + np.dot(B, u)

    return dxdt


# Initial conditions and time span
x0 = np.array([0, 0, 0.26, 0])
tspan = np.linspace(0, 4, 401)

# Solve the differential equations using odeint
x = odeint(inverted_pendulum_k1, x0, tspan)

# Plotting the results
plt.figure(figsize=(10, 6))

plt.plot(tspan, x[:, 0], 'k', label='x (m)')
plt.plot(tspan, x[:, 2] * 180 / np.pi, '-.k', label=r'$\theta$ (degrees)')
plt.grid(True)
plt.xlabel('Time (sec)')
plt.ylabel('State Variables')
plt.legend()
plt.title('Simulation of closed-loop Inverted Pendulum')
plt.show()
