import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# Define the global parameters
class Parameters:
    Tl = 0.01

Par = Parameters()

# Define the DC motor model and observer function
def DC_motor_LTR1(t, X):
    global Par
    # Model of The Real System
    # State variable x=[\theta; \omega; i]
    x = X[:3]
    A = np.array([[0, 1, 0], [0, 0, 4.438], [0, -12, -24]])
    B = np.array([[0], [0], [20]])
    Bd = np.array([[0], [-7.396], [0]])
    C = np.array([1, 0, 0])
    y = np.dot(C, x)

    # Model of the observer with disturbance Tl=0.01*exp(-t)
    # State variable xh=[\theta_h; \omega_h; i_h; Tl_h]
    xh = X[3:]
    Ah = np.array([[0, 1, 0, 0], [0, 0, 4.438, -7.396], [0, -12, -24, 0], [0, 0, 0, -1]])
    Bh = np.array([0, 0, 20, 0]).reshape((4, 1))
    Ch = np.array([1, 0, 0, 0])

    # State feedback and state observer gains
    k = np.array([3.0000, 0.8796, 0.1529, -1.8190])
    G = np.array([-1.0000, 235.7440, -978.1707, -20.4870]).reshape((4, 1))

    # Final Equations
    theta_d = 0  # Desired angular position
    Tl = Par.Tl * np.exp(-t)  # exponential disturbance
    v = -np.dot(k, xh)
    u = v + Tl

    xhp = np.dot(Ah, xh) + Bh.flatten() * v + G.flatten() * (y - np.dot(Ch, xh))
    xp = np.dot(A, x) + B.flatten() * v + Bd.flatten() * Tl
    return np.concatenate((xp, xhp))

# Initial conditions
x0 = [0, 0, 0, 0, 0, 0, 0]
tspan = [0, 5]

# Solve the differential equations
sol = solve_ivp(DC_motor_LTR1, tspan, x0, max_step=0.01, t_eval=np.arange(0, 5, 0.01))

# Extract the solution
t = sol.t
x = sol.y

# Plot the results
plt.figure(figsize=(12, 8))

plt.subplot(221)
plt.plot(t, x[0], 'k', label='θ')
plt.plot(t, x[3], '--k', label='θ_h')
plt.grid()
plt.xlabel('Time (sec)')
plt.ylabel('Angular displacement (rad)')
plt.legend()

plt.subplot(222)
plt.plot(t, x[1], 'k', label='ω')
plt.plot(t, x[4], '--k', label='ω_h')
plt.grid()
plt.xlabel('Time (sec)')
plt.ylabel('Angular velocity (rad/sec)')
plt.legend()

plt.subplot(223)
plt.plot(t, x[2], 'k', label='i')
plt.plot(t, x[5], '--k', label='i_h')
plt.grid()
plt.xlabel('Time (sec)')
plt.ylabel('Motor Current (Amp)')
plt.legend()

Tl = Par.Tl * np.exp(-t)
plt.subplot(224)
plt.plot(t, Tl, 'k', label='Tl')
plt.plot(t, x[6], '--k', label='Tl_h')
plt.grid()
plt.xlabel('Time (sec)')
plt.ylabel('Disturbance torque (N.m)')
plt.legend()

# Set linewidth of all lines
for line in plt.gcf().findobj(lambda x: isinstance(x, plt.Line2D)):
    line.set_linewidth(2)

plt.tight_layout()
plt.show()
