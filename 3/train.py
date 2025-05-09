import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from scipy.signal import lsim, StateSpace

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
b1 = np.array([0, 0, 0, 0, 0.005, 0, 0, 0, 0, 0]).reshape(-1, 1)  # Force input
b2 = np.array([0, 0, 0, 0, 250, 0, 0, 0, 0, -1250]).reshape(-1, 1)  # Constant input
B = np.hstack((b1, b2))
C = np.array([1, 0, 0, 0, 0, 0, 0, 0, 0, 0])
D = 0

train_model = StateSpace(A, b1, C, D)  # Note only the first input is used
t = np.arange(0, 7.01, 0.01)  # Time vector

# Initial conditions
x0 = np.array([20, 20, 20, 20, 20, 0, 0, 0, 0, 0])

# Simulate the initial response
_, y, x = lsim(train_model, U=0, T=t, X0=x0)

# Plot the initial response
plt.figure()
plt.plot(t, x[:, 0], 'k', label='x1')
plt.plot(t, x[:, 4], 'k-.', label='x5')
plt.grid(True)
plt.xlabel('Time (sec)')
plt.ylabel('State variables')
plt.legend()
plt.title('Initial Response')
plt.show()

# Generate input u
u = 0.1 * (np.sin(5*t) + np.sin(9*t) + np.sin(13*t) + np.sin(17*t) + np.sin(21*t))

# Simulate the system with the generated input
active_suspension = StateSpace(A, b1, C, D)  # Using the same state-space model for lsim
_, y, x = lsim(active_suspension, U=u, T=t)

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
