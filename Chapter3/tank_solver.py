# Import necessary libraries
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Define the model of the tank
def tank_model(x, t):
    A = 1.0
    C = 2.0
    F_in = 0.0  # No disturbance input
    u = 0.1     # Constant opening for valve
    
    x = np.maximum(x, 0)  # Ensure tank level is non-negative
    
    xp = (F_in - C * u * np.sqrt(x)) / A
    
    return xp

# Initial condition: Tank level
x0 = [100.0]  # Initial level of the tank

# Time vector for the simulation
tspan = np.linspace(0, 100, 1000)  # From 0 to 100 seconds, 1000 points

# Solve the system of ODEs
x = odeint(tank_model, x0, tspan)

# Plot the results
plt.figure(figsize=(10, 6))
plt.plot(tspan, x, 'k', linewidth=2)
plt.grid(True)
plt.xlabel('Time (sec)')
plt.ylabel('Tank Level (m)')
plt.title('Tank Model Simulation')
plt.show()
