import numpy as np
from scipy.signal import StateSpace, lsim
import matplotlib.pyplot as plt

# Define the system matrices
A = np.array([[0,    0,   0,   0,   0,    1,      0,      0,   0,   0],
              [0,    0,   0,   0,   0,    1,     -1,      0,   0,   0],
              [0,    0,   0,   0,   0,    0,      1,     -1,   0,   0],
              [0,    0,   0,   0,   0,    0,      0,      1,  -1,   0],
              [0,    0,   0,   0,   0,    0,      0,      0,   1,  -1],
              [0, -12.5,  0,   0,   0,  -0.75,   0.75,    0,   0,   0],
              [0,  62.5, -62.5, 0,  0,   3.75,  -7.5,   3.75,  0,   0],
              [0,   0,  62.5, -62.5, 0,   0,   3.75,  -7.5,   3.75,  0],
              [0,   0,   0,  62.5, -62.5,  0,     0,    3.75,  -7.5,  3.75],
              [0,   0,   0,   0,  62.5,  0,     0,     0,    3.75, -3.75]])

b1 = np.array([0,  0,  0,  0,  0, 0.005,   0,  0,  0,  0])
b2 = np.array([0,  0,  0,  0,  0, 250,  0,  0,  0,  -1250])
C = np.array([1, 0, 0, 0, 0, 0, 0, 0, 0, 0])
D = 0

# Combine b1 and b2 to form b
b = (b1[:, np.newaxis] * 750) + b2[:, np.newaxis]

# Create the StateSpace object
train_model = StateSpace(A, b, C, D)

# Time vector for simulation
t = np.linspace(0, 7, 1000)

# Initial state
x0 = np.zeros(10)

# Step input signal
u = np.ones(len(t)) * 750

# Simulate the response to the step input signal
t, y, x = lsim(train_model, u, t, X0=x0)

# Plotting the step response
plt.figure(1)
plt.plot(t, x[:, 1], 'k', t, x[:, 4], 'k-.')
plt.grid(True)
plt.xlabel('Time (sec)')
plt.ylabel('State variables')
plt.legend(['x_2', 'x_5'])
plt.show()
#############################################3
import numpy as np
from scipy.signal import StateSpace, lsim
import matplotlib.pyplot as plt

# Define the system matrices
A = np.array([[0,    0,   0,   0,   0,    1,      0,      0,   0,   0],
              [0,    0,   0,   0,   0,    1,     -1,      0,   0,   0],
              [0,    0,   0,   0,   0,    0,      1,     -1,   0,   0],
              [0,    0,   0,   0,   0,    0,      0,      1,  -1,   0],
              [0,    0,   0,   0,   0,    0,      0,      0,   1,  -1],
              [0, -12.5,  0,   0,   0,  -0.75,   0.75,    0,   0,   0],
              [0,  62.5, -62.5, 0,  0,   3.75,  -7.5,   3.75,  0,   0],
              [0,   0,  62.5, -62.5, 0,   0,   3.75,  -7.5,   3.75,  0],
              [0,   0,   0,  62.5, -62.5,  0,     0,    3.75,  -7.5,  3.75],
              [0,   0,   0,   0,  62.5,  0,     0,     0,    3.75, -3.75]])

b1 = np.array([0,  0,  0,  0,  0, 0.005,   0,  0,  0,  0])
b2 = np.array([0,  0,  0,  0,  0, 250,  0,  0,  0,  -1250])
C = np.array([1, 0, 0, 0, 0, 0, 0, 0, 0, 0])
D = 0

# Combine b1 and b2 to form b
b = (b1[:, np.newaxis] * 750) + b2[:, np.newaxis]

# Create the StateSpace object
train_model = StateSpace(A, b, C, D)

# Time vector for simulation
t = np.linspace(0, 7, 1000)

# Initial state
x0 = np.zeros(10)

# Define the input signal
u = 0.1 * (np.sin(5*t) + np.sin(9*t) + np.sin(13*t) + np.sin(17*t) + np.sin(21*t))

# Simulate the response to the sinusoidal input signal
t, y, x = lsim(train_model, u, t, X0=x0)

# Plotting the lsim response
plt.figure(2)
plt.plot(t, x[:, 0], 'k', t, x[:, 1], 'k-.')
plt.grid(True)
plt.xlabel('Time (sec)')
plt.ylabel('State variables')
plt.legend(['x_1', 'x_2'])
plt.show()
