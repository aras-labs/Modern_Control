import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# System parameters
M = 0.5  # Mass of the cart (kg)
m = 0.2  # Mass of the pendulum (kg)
b = 0.1  # Damping coefficient (N.s/m)
l = 0.3  # Length to the center of mass of the pendulum (m)
I = 0.006  # Inertia of the pendulum (kg.m^2)
g = 9.81  # Acceleration due to gravity (m/s^2)

# State feedback and observer gains
K = np.array([0.1291, 0.1446, -3.6742, -2.2147])
L = np.array([4.9672, 10.0391, 21.4149, 6.1251])

# State space matrices
A = np.array([[0, 1, 0, 0],
              [0, -(I + m * l ** 2) * (b / (I * (M + m) + m * M * l ** 2)),
               (m ** 2 * g * l ** 2) / (I * (M + m) + m * M * l ** 2), 0],
              [0, 0, 0, 1],
              [0, -(m * l * b) / (I * (M + m) + m * M * l ** 2), (m * g * l * (M + m)) / (I * (M + m) + m * M * l ** 2),
               0]])

B = np.array([[0], [(I + m * l ** 2) / (I * (M + m) + m * M * l ** 2)], [0], [m * l / (I * (M + m) + m * M * l ** 2)]])

C = np.array([[1, 0, 0, 0]])

# Luenberger observer matrix
A_observer = np.array([[0, 1, 0, 0],
                       [0, -(I + m * l ** 2) * (b / (I * (M + m) + m * M * l ** 2)),
                        (m ** 2 * g * l ** 2) / (I * (M + m) + m * M * l ** 2), 0],
                       [0, 0, 0, 1],
                       [0, -(m * l * b) / (I * (M + m) + m * M * l ** 2),
                        (m * g * l * (M + m)) / (I * (M + m) + m * M * l ** 2), 0]])

B_observer = np.array(
    [[0], [(I + m * l ** 2) / (I * (M + m) + m * M * l ** 2)], [0], [m * l / (I * (M + m) + m * M * l ** 2)]])

L_observer = np.array([[4.9672], [10.0391], [21.4149], [6.1251]])


# Function defining the dynamics of the inverted pendulum with Luenberger observer
def inverted_pendulum_Luenberger(X, t):
    x = X[:4]  # State variables [x, dx, theta, dtheta]
    xh = X[4:]  # Observer variables [xh, dxh, thetah, dthetah]

    # Control input
    u = -np.dot(K, xh)

    # System dynamics
    dx = np.dot(A, x) + B * u

    # Observer dynamics
    dxh = np.dot(A_observer, xh) + np.dot(B_observer, u) + np.dot(L_observer, (x - xh))

    # Combine state and observer derivatives
    dX = np.concatenate((dx, dxh))

    return dX


# Initial conditions
x0 = np.array([0, 0, 0.26, 0])  # Initial state [x, dx, theta, dtheta]
xh0 = np.array([0, 0, 0, 0])  # Initial observer state [xh, dxh, thetah, dthetah]
X0 = np.concatenate((x0, xh0))  # Initial total state vector

# Time span for simulation
t_span = np.linspace(0, 3, 300)  # 300 points from 0 to 3 seconds

# Numerically integrate the system
X = odeint(inverted_pendulum_Luenberger, X0, t_span)

# Extract states from the simulation results
x_cart = X[:, 0]
theta_pendulum = X[:, 2]
theta_observer = X[:, 6]

# Plotting the results
plt.figure(figsize=(10, 6))

plt.plot(t_span, theta_pendulum, 'k', label='Pendulum')
plt.plot(t_span, theta_observer, '-.k', label='Observer')
plt.grid(True)
plt.xlabel('Time (sec)')
plt.ylabel('Angular Position (rad)')
plt.legend()
plt.title('Inverted Pendulum: Angular Position')

plt.show()
