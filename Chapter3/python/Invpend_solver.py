import numpy as np

tspan = np.array([0, 1])
x0 = np.array([0, 0.1, 0, 0])

import numpy as np

def inverted_pendulum(x, t):
    # Parameters
    g = 9.8
    l = 1
    m = 1
    M = 1
    
    # Compute intermediate terms
    d1 = M + m * (1 - np.cos(x[1])**2)
    d2 = l * d1
    
    # Input force
    F = 0  # No input
    
    # Compute time derivatives of state variables
    xp = np.array([
        x[2],  # x'
        x[3],  # theta'
        (F + m * l * x[3]**2 * np.sin(x[1]) - m * g * np.sin(x[1]) * np.cos(x[1])) / d1,  # v'
        (-F * np.cos(x[1]) - m * l * x[3]**2 * np.sin(x[1]) * np.cos(x[1]) +
         (M + m) * g * np.sin(x[1])) / d2  # omega'
    ])
    
    return xp

from scipy.integrate import odeint

# Define the time points at which you want the solution
t_eval = np.linspace(tspan[0], tspan[1], 100)  # Adjust the number of points as needed

# Solve the ODE using odeint
x = odeint(inverted_pendulum, x0, t_eval)



import matplotlib.pyplot as plt

# Plot the first and second columns of x against time
plt.plot(t_eval, x[:, 0], 'k', label='x (m)')
plt.plot(t_eval, x[:, 1], '-.k', label=r'$\theta$ (rad)')

# Add gridlines
plt.grid(True)

# Set labels for x-axis and y-axis
plt.xlabel('Time (sec)')
plt.ylabel('State Variables')

# Add legend
plt.legend()

# Set linewidth for all lines in the plot
plt.setp(plt.gca().lines, linewidth=2)

# Show the plot
plt.show()
