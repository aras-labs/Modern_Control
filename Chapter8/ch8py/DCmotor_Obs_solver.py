import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# Define the global parameters
class Parameters:
    Tl = 1.0

Par = Parameters()

# Define the DC motor model and observer function
def DC_motor_Obs(t, X):
    global Par
    # Model of The Real System
    # State variable x=[\theta; \omega; i]
    x = X[:3]
    A = np.array([[0, 1, 0],
                  [0, 0, 4.438],
                  [0, -12, -24]])
    B = np.array([[0, 0],
                  [0, -7.396],
                  [20, 0]])
    C = np.array([1, 0, 0])
    Tl = Par.Tl  # step disturbance
    v = 0
    u = np.array([v, Tl])
    xp = np.dot(A, x) + np.dot(B, u)
    y = np.dot(C, x)

    # Model of The observer
    # State variable x=[\theta_hat; \omega_hat; i_hat, Tl_hat]
    xh = X[3:]
    Ah = np.array([[0, 1, 0, 0],
                   [0, 0, 4.438, -7.396],
                   [0, -12, -24, 0],
                   [0, 0, 0, 0]])
    Bh = np.array([0, 0, 20, 0])
    Ch = np.array([1, 0, 0, 0])
    G = np.array([0, 234.7440, -936.9136, -27.6050])
    xhp = np.dot(Ah, xh) + Bh * v + np.dot(G, (y - np.dot(Ch, xh)))

    # Augment the real and estimated states
    return np.concatenate((xp, xhp))

# Initial conditions
x0 = [1, 0, 0, 0, 0, 0, Par.Tl]
tspan = [0, 2]

# Solve the differential equations
sol = solve_ivp(DC_motor_Obs, tspan, x0, method='RK45', t_eval=np.linspace(0, 2, 100))

# Extract the solution
t = sol.t
x = sol.y

# Plot the results
plt.figure(figsize=(12, 8))

plt.subplot(221)
plt.plot(t, x[0], 'k', label='θ')
plt.plot(t, x[3], '--k', label='θ_hat')
plt.grid()
plt.xlabel('Time (sec)')
plt.ylabel('Angular displacement (rad)')
plt.legend()

plt.subplot(222)
plt.plot(t, x[1], 'k', label='ω')
plt.plot(t, x[4], '--k', label='ω_hat')
plt.grid()
plt.xlabel('Time (sec)')
plt.ylabel('Angular velocity (rad/sec)')
plt.legend()

plt.subplot(223)
plt.plot(t, x[2], 'k', label='i')
plt.plot(t, x[5], '--k', label='i_hat')
plt.grid()
plt.xlabel('Time (sec)')
plt.ylabel('Motor Current (Amp)')
plt.legend()

plt.subplot(224)
plt.plot(t, Par.Tl + np.zeros_like(t), 'k', label='Tl')
plt.plot(t, x[6], '--k', label='Tl_hat')
plt.grid()
plt.xlabel('Time (sec)')
plt.ylabel('Disturbance torque (N.m)')
plt.legend()

# Set linewidth of all lines
for line in plt.gcf().findobj(lambda x: isinstance(x, plt.Line2D)):
    line.set_linewidth(2)

plt.tight_layout()
plt.show()
