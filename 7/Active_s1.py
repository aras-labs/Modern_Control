import numpy as np
import scipy.signal as signal
import matplotlib.pyplot as plt

# Define system matrices
A = np.array([[0, 0, 1, 0],
              [0, 0, 0, 1],
              [-10, 10, -2, 2],
              [60, -660, 12, -12]])

b1 = np.array([[0],
               [0],
               [0.0033],
               [-0.02]])

b2 = np.array([[0],
               [0],
               [0],
               [600]])

B = np.hstack((b1, b2))

C = np.array([[1, 0, 0, 0]])
D = np.array([[0]])

# Create state-space system
active_suspension = signal.StateSpace(A, B, C, D)

# Simulation time
t = np.arange(0, 7, 0.01)

# Initial conditions
x0 = np.array([0.2, 0, 0, 0])

# Simulate initial response
t_initial, x_initial = signal.initial(active_suspension, X0=x0, T=t)

# Plot initial response
plt.figure(figsize=(10, 6))
plt.plot(t_initial, x_initial[:, 0], 'k', label='x_1')
plt.plot(t_initial, x_initial[:, 1], 'k-.', label='x_2')
plt.grid(True)
plt.xlabel('Time (sec)')
plt.ylabel('State variables')
plt.title('Initial Response of Active Suspension System')
plt.legend()
plt.show()

# Generate input signal u
u = 0.1 * (np.sin(5*t) + np.sin(9*t) + np.sin(13*t) + np.sin(17*t) + np.sin(21*t))

# Simulate the system with input signal u
t_simulation, x_simulation, _ = signal.lsim(active_suspension, u, t, X0=x0)

# Plot simulation results
plt.figure(figsize=(10, 6))
plt.plot(t_simulation, x_simulation[:, 0], 'k', label='x_1')
plt.plot(t_simulation, x_simulation[:, 1], 'k-.', label='x_2')
plt.grid(True)
plt.xlabel('Time (sec)')
plt.ylabel('State variables')
plt.title('Simulation of Active Suspension System')
plt.legend()
plt.show()
