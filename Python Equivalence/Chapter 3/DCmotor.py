import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import lsim

# Define system matrices
A = np.array([[0, 1, 0], [0, 0, 4.438], [0, -12, -24]])
b1 = np.array([[0], [0], [20]])
b2 = np.array([[0], [-7.396], [0]])
B = np.hstack((b1, b2))
C = np.array([[1, 0, 0], [0, 1, 0]])
D = 0

# Time vector
t = np.arange(0, 4, 0.01)

# Define the input signal
u1 = 3 - 6 * square(2 * np.pi * 4 * t)

# Perform simulation
t, y, x = lsim((A, B, C, D), U=u1, T=t)

# Plot the results
plt.plot(t, x[:, 0], 'k', label='theta')
plt.plot(t, x[:, 1], 'k-.', label='omega')
plt.plot(t, x[:, 2], 'k:', label='i')
plt.grid(True)
plt.xlabel('Time (sec)')
plt.ylabel('State variable')
plt.legend()
plt.show()
