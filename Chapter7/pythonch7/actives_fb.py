import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import StateSpace, impulse
from control import place  # Importing pole placement function from control module

# Define system matrices
A = np.array([[0,  0,  1, -1,  0],
              [0,  0,  1,  0,  0],
              [-10, 0, -2,  2,  0],
              [720, -660, 12, -12, 0],
              [1,  0,  0,  0,  0]])
b1 = np.array([0, 0, 0.00333, -0.02, 0]).reshape(-1, 1)  # Reshape to column vector
b2 = np.array([0, -1, 0, 0, 0]).reshape(-1, 1)  # Reshape to column vector
pd = np.array([-5, -25+25j, -25-25j, -3+3j, -3-3j])

# Compute gain matrix k using pole placement (equivalent to place in MATLAB)
k = place(A, b1, pd)

# Closed loop system
Acl = A - np.dot(b1, k)
Bcl = 0.1 * b2
C = np.array([1, 0, 0, 0, 0])
D = np.array([0])
ld = 0.1

# Define state-space system
active_fb = StateSpace(Acl, Bcl, C, D)

# Compute impulse response
t, y = impulse(active_fb)

# Plotting
plt.figure(figsize=(10, 6))

# Plot l1 (y + 0.1) in solid black line
plt.plot(t, y + 0.1, 'k', label='l1')

# Plot x (y - 0.574 * 0.1) in dashed black line
plt.plot(t, y - 0.574 * 0.1, 'k-.', label='x')

plt.grid(True)
plt.xlabel('Time (sec)')
plt.ylabel('State variables')
plt.legend()
plt.show()

