import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt


# Define the train model function
def train_model(X, t):
    # Parameters and variables
    x = X[:10]

    # System matrices
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

    b1 = np.array([0, 0, 0, 0, 0, 0.005, 0, 0, 0, 0])  # Force input
    b2 = np.array([0, 0, 0, 0, 0, 250, 0, 0, 0, -1250])  # Constant input

    # Control law
    if t < 10:
        u = 1000  # Constant Force (adjust as needed)
    else:
        u = 0

    xp = np.dot(A, x) + np.dot(b1, u) + np.dot(b2, u)

    # Augment the real and estimated states
    Xp = xp

    return Xp


# Set initial conditions and parameters
x0 = np.array([0, 20, 20, 20, 20, 0, 0, 0, 0, 0])  # Initial state vector
t_span = np.linspace(0, 100, 1000)  # Time span for integration

# Perform integration using odeint
X = odeint(train_model, x0, t_span)

# Plotting results
plt.figure(figsize=(10, 8))

# Plot locomotive position
plt.subplot(211)
plt.plot(t_span, X[:, 0], 'k', label='x_1')
plt.grid(True)
plt.xlabel('Time (sec)')
plt.ylabel('Locomotive Position (m)')
plt.legend()

# Plot wagons distance
plt.subplot(212)
plt.plot(t_span, X[:, 1], 'k', label='x_2')
plt.plot(t_span, X[:, 4], 'k-.', label='x_5')
plt.grid(True)
plt.xlabel('Time (sec)')
plt.ylabel('Wagons Distance (m)')
plt.legend()

plt.tight_layout()
plt.show()
