import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

def robot_model(t, x):
    # State variable x = [theta_1, theta_2, omega_1, omega_2]
    g = 9.81
    l1 = 1
    l2 = 0.5
    m1 = 2
    m2 = 1
    I1 = 1e-2
    I2 = 5e-3
    D = 2

    M = np.zeros((2, 2))
    M[0, 0] = m1 * (l1 / 2)**2 + m2 * (l1**2 + (l2 / 2)**2) + m2 * l1 * l2 * np.cos(x[1]) + I1 + I2
    M[0, 1] = m2 * (l2 / 2)**2 + 0.5 * m2 * l1 * l2 * np.cos(x[1]) + I2
    M[1, 0] = M[0, 1]
    M[1, 1] = m2 * (l2 / 2)**2 + I2

    V = np.zeros((2, 1))
    V[0, 0] = -m2 * l1 * l2 * np.sin(x[1]) * x[2] * x[3] - 0.5 * m2 * l1 * l2 * np.sin(x[1]) * x[3]**2
    V[1, 0] = -0.5 * m2 * l1 * l2 * np.sin(x[1]) * x[2] * x[3]

    G = np.zeros((2, 1))
    G[0, 0] = (m1 * l1 / 2 + m2 * l1) * g * np.cos(x[0]) + m2 * g * l2 / 2 * np.cos(x[0] + x[1])
    G[1, 0] = m2 * g * l2 / 2 * np.cos(x[0] + x[1])

    Q = np.zeros((2, 1))  # No input
    Q = Q - D * np.array([[x[2]], [x[3]]])

    # Solve for the accelerations
    xy = np.linalg.pinv(M).dot(Q - V - G)

    xp = np.array([x[2], x[3], xy[0, 0], xy[1, 0]])
    return xp

# Initial conditions: theta1, theta2, omega1, omega2
x0 = [-np.pi / 3, np.pi / 3, 0, 0]

# Time span for the simulation
t_span = (0, 5)
t_eval = np.linspace(*t_span, 300)  # Generate 300 time points within the span

# Solve the differential equation
sol = solve_ivp(robot_model, t_span, x0, t_eval=t_eval)

# Plotting the results
plt.figure(figsize=(10, 6))
plt.plot(sol.t, np.degrees(sol.y[0]), 'k', label='theta_1 (degrees)')
plt.plot(sol.t, np.degrees(sol.y[1]), '-.k', label='theta_2 (degrees)')
plt.grid(True)
plt.xlabel('Time (sec)')
plt.ylabel('State Variables')
plt.legend()
plt.title('Simulation of 2R Robot')
plt.show()
