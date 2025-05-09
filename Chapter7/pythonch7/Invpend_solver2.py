import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def inverted_pendulum_k2(x, t):
    # System parameters
    g = 9.81  # gravitational acceleration (m/s^2)
    L = 1.0   # length of the pendulum (m)
    m = 1.0   # mass of the pendulum (kg)
    b = 0.1   # damping coefficient
    
    # Extract state variables
    x1, x2, x3, x4 = x  # x1 = x, x2 = x_dot, x3 = theta, x4 = theta_dot
    
    # Equations of motion
    dx1 = x2
    dx2 = (m * g * np.sin(x3) - b * x2) / (m * L**2)
    dx3 = x4
    dx4 = (-m * g * np.cos(x3) * np.sin(x3) - b * x4) / (m * L**2)
    
    return [dx1, dx2, dx3, dx4]

# Initial conditions and time span
t_span = np.linspace(0, 3, 300)  # from 0 to 3 seconds
x0 = [0, 0, 0.6, 0]  # initial conditions [x, x_dot, theta, theta_dot]

# Solve the differential equation
x = odeint(inverted_pendulum_k2, x0, t_span)

# Plot results
plt.figure(figsize=(10, 6))
plt.plot(t_span, x[:, 0], 'k', label='x (m)')
plt.plot(t_span, x[:, 2], '-.k', label='theta (rad)')
plt.xlabel('Time (sec)')
plt.ylabel('State Variables')
plt.grid(True)
plt.legend()
plt.show()
