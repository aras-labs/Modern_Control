import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import StateSpace, lsim

# Define the state-space model
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
b1 = np.array([0, 0, 0, 0, 0, 0.005, 0, 0, 0, 0]).reshape(-1, 1)  # Force input
b2 = np.array([0, 0, 0, 0, 0, 250, 0, 0, 0, -1250]).reshape(-1, 1)  # Constant input
C = np.array([1, 0, 0, 0, 0, 0, 0, 0, 0, 0])
D = np.array([0])

# Constant input
u = 750
b = b1 * u + b2

# Define the state-space system
train_model = StateSpace(A, b, C, D)

# Time vector
t = np.arange(0, 7.001, 0.001)

# Initial conditions
x0 = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

# Simulate the forced response
_, y, x = lsim(train_model, T=t, U=np.zeros_like(t), X0=x0)

# Plot the forced response
plt.figure()
plt.plot(t, x[:, 1], 'k', label='x2')
plt.plot(t, x[:, 4], 'k-.', label='x5')
plt.grid(True)
plt.xlabel('Time (sec)')
plt.ylabel('State variables')
plt.legend()
plt.title('Forced Response')
plt.show()

# Generate input u
u = 0.1 * (np.sin(5*t) + np.sin(9*t) + np.sin(13*t) + np.sin(17*t) + np.sin(21*t))

# Simulate the system with the generated input
active_suspension = StateSpace(A, b1, C, D)  # Using the same state-space model for lsim
_, y, x = lsim(active_suspension, U=u, T=t, X0=x0)

# Plot the result
plt.figure()
plt.plot(t, x[:, 0], 'k', label='x1')
plt.plot(t, x[:, 1], 'k-.', label='x2')
plt.grid(True)
plt.xlabel('Time (sec)')
plt.ylabel('State variables')
plt.legend()
plt.title('Response to Input u')
plt.show()
