import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import ss, place_poles, lsim

# Define system matrices
A = np.array([[0, 0, 1, -1, 0],
              [0, 0, 1, 0, 0],
              [-10, 0, -2, 2, 0],
              [720, -660, 12, -12, 0],
              [1, 0, 0, 0, 0]])

b1 = np.array([[0], [0], [0.00333], [-0.02], [0]])
b2 = np.array([[0], [-1], [0], [0], [0]])
b3 = np.array([[0], [0], [0], [0], [1]])

pd = np.array([-5, -25 + 25j, -25 - 25j, -3 + 3j, -3 - 3j])

# Perform pole placement
k = place_poles(A.T, b1.T, pd).gain_matrix.T

# Closed-loop system
Acl = A - np.dot(b1, k)
Bcl = 0.1 * b2  # Assuming a scaling factor of 0.1 for b2
C = np.array([[1, 0, 0, 0, 0]])
D = np.array([[0]])
ld = 0.1

# Create state-space system
active_fb = ss(Acl, Bcl, C, D)

# Simulate impulse response
t = np.linspace(0, 5, 1000)  # Time vector
t, x, _ = lsim(active_fb, T=t)

# Plot the result
plt.plot(t, x[:, 0] + ld, 'k', label='l_1')
plt.plot(t, x[:, 4] - 0.574 * ld, 'k-.', label='x')
plt.grid(True)
plt.xlabel('Time (sec)')
plt.ylabel('State Variables')
plt.legend()
plt.show()
