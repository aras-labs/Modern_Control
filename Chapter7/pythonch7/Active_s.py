import numpy as np
import control as ctrl
import matplotlib.pyplot as plt

A = np.array([[0, 0, 1, 0],
              [0, 0, 0, 1],
              [-10, 10, -2, 2],
              [60, -660, 12, -12]])
b1 = np.array([[0], [0], [0.0033], [-0.02]])
b2 = np.array([[0], [0], [0], [600]])
B = np.hstack((b1, b2))
C = np.array([[1, 0, 0, 0]])
D = np.array([[0]])

# Create state-space system
active_suspension = ctrl.ss(A, b2, C, D)

# Time vector
t = np.arange(0, 7, 0.01)
N = len(t)


# Initial state
x0 = np.array([[0.2], [0], [0], [0]])

# Simulate initial response
response = ctrl.forced_response(active_suspension, T=t, X0=x0)


# Plot state variables x1 and x2
plt.plot(t, response.states[0], 'k', label='x1')
plt.plot(t, response.states[1], 'k-.', label='x2')
plt.xlabel('Time (sec)')
plt.ylabel('State variables')
plt.grid(True)
plt.legend()
plt.show()

# Generate input signal u
u = 0.1 * (np.sin(5 * t) + np.sin(9 * t) + np.sin(13 * t) + np.sin(17 * t) + np.sin(21 * t))

# Simulate the response of the system
# Simulate the response of the system with the provided input signal
response = ctrl.forced_response(active_suspension, T=t, U=u)

import matplotlib.pyplot as plt

# Plot state variables x1 and x2
plt.plot(t, response.states[0], 'k', label='x1')
plt.plot(t, response.states[1], 'k-.', label='x2')
plt.xlabel('Time (sec)')
plt.ylabel('State variables')
plt.grid(True)
plt.legend()
plt.show()
