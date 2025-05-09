import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint


# Define the train model function
def train_model1(x, t):
    # State matrix A
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

    # Input matrices b1 and b2
    b1 = np.array([0, 0, 0, 0, 0.005, 0, 0, 0, 0, 0]).reshape(-1, 1)
    b2 = np.array([0, 0, 0, 0, 250, 0, 0, 0, 0, -1250]).reshape(-1, 1)

    # Constant input
    u = 750

    # State equations
    xp = np.dot(A, x) + b1 * u + b2
    return xp.flatten()


# Initial conditions
x0 = np.array([0, 20, 20, 20, 20, 0, 0, 0, 0, 0])

# Time span for simulation
t = np.linspace(0, 10, 1000)  # Adjust the end time and number of time points as needed

# Solve the ODE system
x = odeint(train_model1, x0, t)

# Plotting results
plt.figure(figsize=(10, 6))

plt.plot(t, x[:, 1], 'k', label='x2')
plt.plot(t, x[:, 4], 'k-.', label='x5')
plt.grid(True)
plt.xlabel('Time (sec)')
plt.ylabel('State Variables')
plt.legend()
plt.title('Simulation of Train Model')
plt.show()
