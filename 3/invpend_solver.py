import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt


def inverted_pendulum(t, x):
    # State variable x = [x, theta, v, omega]
    g = 9.8
    l = 1
    m = 1
    M = 1
    d1 = M + m * (1 - np.cos(x[1]) ** 2)
    d2 = l * d1

    F = 0  # No input

    xp = np.zeros(4)
    xp[0] = x[2]
    xp[1] = x[3]
    xp[2] = (F + m * l * x[3] ** 2 * np.sin(x[1]) - m * g * np.sin(x[1]) * np.cos(x[1])) / d1
    xp[3] = (-F * np.cos(x[1]) - m * l * x[3] ** 2 * np.sin(x[1]) * np.cos(x[1]) + (M + m) * g * np.sin(x[1])) / d2

    return xp


# Initial conditions: x, theta, v, omega
x0 = [0, 0.1, 0, 0]

# Time span for the simulation
t_span = (0, 1)
t_eval = np.linspace(*t_span, 300)  # Generating 300 time points within the span

# Solve the differential equation
sol = solve_ivp(inverted_pendulum, t_span, x0, t_eval=t_eval, max_step=1e-2)

# Plotting the results
plt.figure(figsize=(10, 6))
plt.plot(sol.t, sol.y[0], 'k', label='x (m)')
plt.plot(sol.t, sol.y[1], '-.k', label='theta (rad)')
plt.grid(True)
plt.xlabel('Time (sec)')
plt.ylabel('State Variables')
plt.legend()
plt.title('Simulation of Inverted Pendulum')
plt.show()
