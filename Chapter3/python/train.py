import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

A = np.array([
    [0,    0,   0,   0,   0,    1,      0,      0,   0,   0],
    [0,    0,   0,   0,   0,    1,     -1,      0,   0,   0],
    [0,    0,   0,   0,   0,    0,      1,     -1,   0,   0],
    [0,    0,   0,   0,   0,    0,      0,      1,  -1,   0],
    [0,    0,   0,   0,   0,    0,      0,      0,   1,  -1],
    [0, -12.5, 0,   0,   0, -0.75,   0.75,    0,   0,   0],
    [0,  62.5, -62.5, 0,  0,  3.75,  -7.5,  3.75,  0,   0],
    [0,   0,  62.5, -62.5,  0,   0,  3.75,  -7.5,  3.75,  0],
    [0,   0,   0,  62.5, -62.5,  0,    0,  3.75,  -7.5,  3.75],
    [0,    0,   0,   0,  62.5,  0,    0,    0,   3.75, -3.75]
])

b1 = np.array([0,  0,  0,  0,  0.005,  0,  0,  0,  0,  0])     # Force input
b2 = np.array([0,  0,  0,  0,  250,  0,  0,  0,  0,  -1250])   # constant input
B = np.column_stack((b1, b2))
C = np.array([1,   0,   0,   0,   0,   0,   0,   0,   0,   0])
D = 0
train_model = signal.StateSpace(A, B[:, 0:1], C, D)



t = np.arange(0, 7.01, 0.01)
N = len(t)




# Define the initial state vector x0
x0 = np.array([20, 20, 20, 20, 20, 0, 0, 0, 0, 0])

# Simulate the response
t, y, x = signal.lsim(train_model, None, t, X0=x0)


# Plot x1 and x5 against time t
plt.plot(t, x[:, 0], 'k', label='x1')
plt.plot(t, x[:, 4], 'k-.', label='x5')
plt.xlabel('Time (sec)')
plt.ylabel('State variables')
plt.grid(True)
plt.legend()
plt.setp(plt.gca().lines, linewidth=2)  # Set the linewidth of all lines in the current plot
plt.show()




u = 0.1 * (np.sin(5 * t) + np.sin(9 * t) + np.sin(13 * t) + np.sin(17 * t) + np.sin(21 * t))


# Simulate the response
t, y, x = signal.lsim(train_model, U=u, T=t)

import matplotlib.pyplot as plt

# Create a new figure
plt.figure()

# Plot x1 and x2 against time t
plt.plot(t, x[:, 0], 'k', label='x1')
plt.plot(t, x[:, 1], 'k-.', label='x2')

# Customize the plot
plt.xlabel('Time (sec)')
plt.ylabel('State variables')
plt.grid(True)
plt.legend()

# Increase line width
plt.setp(plt.gca().lines, linewidth=2)

# Display the plot
plt.show()
