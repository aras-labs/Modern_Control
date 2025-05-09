import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Define the model function
def train_model(x, t):
    # Model parameters
    A = np.array([
        [0,    0,    0,    0,    0,    1,    0,    0,    0,    0],
        [0,    0,    0,    0,    0,    1,   -1,    0,    0,    0],
        [0,    0,    0,    0,    0,    0,    1,   -1,    0,    0],
        [0,    0,    0,    0,    0,    0,    0,    1,   -1,    0],
        [0,    0,    0,    0,    0,    0,    0,    0,    1,   -1],
        [0, -12.5,  0,    0,    0,   -0.75, 0.75,  0,    0,    0],
        [0,  62.5, -62.5, 0,    0,    3.75, -7.5,  3.75, 0,    0],
        [0,    0,   62.5, -62.5, 0,    0,    3.75, -7.5,  3.75, 0],
        [0,    0,    0,   62.5, -62.5, 0,    0,    3.75, -7.5,  3.75],
        [0,    0,    0,    0,   62.5, 0,    0,    0,    3.75, -3.75]
    ])
    b1 = np.array([0, 0,  0,  0,  0,  0.005,  0,  0,  0,  0])      # Force input
    b2 = np.array([0, 0,  0,  0,  0,  250,    0,  0,  0, -1250])   # constant input
    
    u = 1000  # Constant Force
    xp = np.dot(A, x) + b1 * u + b2
    
    return xp

# Initial conditions and time span
x0 = np.array([0, 20, 20, 20, 20, 0, 0, 0, 0, 0])
tspan = np.linspace(0, 100, 1000)  # 1000 points from 0 to 100 seconds

# Solve the ODE
sol = odeint(train_model, x0, tspan)

# Extract results for plotting
t = tspan
x = sol[:, :]

# Plotting
plt.figure(figsize=(10, 8))

plt.subplot(211)
plt.plot(t, x[:, 0], 'k')
plt.grid(True)
plt.xlabel('Time (sec)')
plt.ylabel('Locomotive Position (m)')
plt.legend(['x_1'])

plt.subplot(212)
plt.plot(t, x[:, 1], 'k', label='x_2')
plt.plot(t, x[:, 4], 'k-.', label='x_5')
plt.grid(True)
plt.xlabel('Time (sec)')
plt.ylabel('Wagons Distance (m)')
plt.legend()

plt.tight_layout()
plt.show()
