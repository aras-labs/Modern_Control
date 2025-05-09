import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Define the function representing the ODEs of the DC motor
def DC_motor(x, t):
    # Constants
    K = 0.1  # Motor constant
    R = 1    # Resistance
    L = 0.5  # Inductance
    J = 0.01 # Moment of inertia
    B = 0.1  # Damping coefficient

    # State variables
    theta = x[0]
    omega = x[1]
    i = x[2]

    # Controller (proportional control)
    Kp = 10  # Proportional gain
    V = Kp * (np.pi/2 - theta)  # Control input

    # Dynamic equations
    dtheta_dt = omega
    domega_dt = (-B/J) * omega + (K/J) * i
    di_dt = (-R/L) * i + (V/L)

    return [dtheta_dt, domega_dt, di_dt]

# Initial conditions and time span
x0 = [0, 0, 0]  # Initial state: theta(0) = 0, omega(0) = 0, i(0) = 0
t = np.linspace(0, 3, 300)  # Time span from 0 to 3 seconds

# Solve the ODEs using odeint
sol = odeint(DC_motor, x0, t)

# Extract results
theta_deg = sol[:, 0] * 180 / np.pi  # Convert theta from radians to degrees

# Plot the results
plt.figure(figsize=(10, 6))
plt.plot(t, theta_deg, 'k')
plt.grid(True)
plt.xlabel('Time (sec)')
plt.ylabel('Angular displacement $\\theta$ (degrees)')
plt.title('Closed-Loop DC Motor Simulation')
plt.xlim([0, 3])
plt.ylim([-10, 100])
plt.xticks(np.arange(0, 3.5, 0.5))
plt.yticks(np.arange(-10, 110, 10))
plt.gca().set_yticklabels(['{:.0f}'.format(x) for x in plt.gca().get_yticks()])
plt.tight_layout()
plt.show()
