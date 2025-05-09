import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import lsim, square

# Simulation of the DC motor
# Copyright Hamid D. Taghirad 2013

# Define system matrices
A = np.array([[0, 1, 0],
              [0, 0, 4.438],
              [0, -12, -24]])

b1 = np.array([[0], [0], [20]])
b2 = np.array([[0], [-7.396], [0]])
B = np.hstack((b1, b2))

C = np.array([[1, 0, 0],
              [0, 1, 0]])

D = np.array([[0]])

# Create state space system
DC_motor = (A, B, C, D)

# Define time vector
t = np.arange(0, 4.01, 0.01)
N = len(t)

# A Simple way to generate input u
u = np.zeros((2, N))
for i in range(N):
    if t[i] < 2:
        u[0, i] = 3
    else:
        u[0, i] = -3

# A Professional way to generate input u
u = 6 * square(2 * np.pi * 0.25 * t) - 3  # Generate square wave with period 4 and amplitude 6

# Simulate the system
t, y, x = lsim(DC_motor, u, t)

# Plot the result
plt.figure()
plt.plot(t, x[:, 0], 'k', label='theta')
plt.plot(t, x[:, 1], 'k-.', label='omega')
plt.plot(t, x[:, 2], 'k:', label='i')
plt.grid(True)
plt.xlabel('Time (sec)')
plt.ylabel('State variables')
plt.legend(['theta', 'omega', 'i'])
plt.title('Simulation Result - DC Motor')
plt.show()
