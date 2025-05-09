import matplotlib.pyplot as plt

plt.clf()
print("tspan=[0, 100]")
print("x0=[100]")
import numpy as np
from scipy.integrate import odeint

# Define the tank model differential equation
def tank_model(x, t):
    # Parameters
    k1 = 0.1
    k2 = 0.2
    
    # System of differential equations
    dxdt = -k1*x + k2
    
    return dxdt

# Define the time span
tspan = np.linspace(0, 100, 1000)  # Adjust the number of time points as needed

# Define the initial condition
x0 = [100]

# Solve the ODE
x = odeint(tank_model, x0, tspan)

import matplotlib.pyplot as plt

# Plot the tank level against time
plt.plot(tspan, x[:, 0], 'k')
plt.grid(True)
plt.xlabel('Time (sec)')
plt.ylabel('Tank Level (m)')
plt.setp(plt.gca().lines, linewidth=2)  # Set the linewidth of all lines in the current plot
plt.show()
