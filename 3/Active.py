import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import StateSpace, lsim

# Define system matrices
A = np.array([[0, 0, 1, 0],
              [0, 0, 0, 1],
              [-10, 10, -2, 2],
              [60, -660, 12, -12]])

b1 = np.array([[0], [0], [0.0033], [-0.02]])
b2 = np.array([[0], [0], [0], [600]])
B = np.hstack((b1, b2))
C = np.array([[1, 0, 0, 0]])
D = np.array([[0]])

# Create state space system
active_suspension = StateSpace(A, B, C, D)

# Define time vector and initial conditions
t = np.arange(0, 7.01, 0.01)
x0 = np.array([0.2, 0, 0, 0])

# Initial response simulation
t, y, x = lsim(active_suspension, 0, t, X0=x0)

# Plot initial response
plt.figure()
plt.plot(t, x[:, 0], 'k', label='x1')
plt.plot(t, x[:, 1], 'k-.', label='x2')
plt.grid(True)
plt.xlabel('Time (sec)')
plt.ylabel('State variables')
plt.legend(['x1', 'x2'])
plt.title('Initial Response')
plt.show()

# Generate input signal u
u = 0.1 * (np.sin(5*t) + np.sin(9*t) + np.sin(13*t) + np.sin(17*t) + np.sin(21*t))

# Simulate the system with input u
t, y, x = lsim(active_suspension, u, t)

# Plot the simulation result
plt.figure()
plt.plot(t, x[:, 0], 'k', label='x1')
plt.plot(t, x[:, 1], 'k-.', label='x2')
plt.grid(True)
plt.xlabel('Time (sec)')
plt.ylabel('State variables')
plt.legend(['x1', 'x2'])
plt.title('Simulation Result')
plt.show()
