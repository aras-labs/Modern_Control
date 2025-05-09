import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# Define the function for the inverted pendulum with Luenberger observer
def inverted_pendulum_luenburger(t, X):
    # State variables: x=[x; v; theta; omega], psi
    x = X[0:4]
    psi = X[4]
    
    g = 9.8
    l = 1
    m = 1
    M = 1
    
    # Constants for dynamics
    d1 = M + m * (1 - np.cos(x[2])**2)
    d2 = l * d1
    
    # State feedback gain
    k = [-40.0, -37.3693, -190.6669, -54.7283]
    
    # Luenberger observer dynamics
    dpsi = -40.0 * x[0] - 37.37 * x[1] - 405.9 * x[2] - 58.73 * psi
    omega_h = psi + 4 * x[2]
    
    # Estimated state vector
    xh = np.concatenate((x[0:3], [omega_h]))
    
    # State feedback control law
    F = -np.dot(k, x)
    # Use the Luenberger observer feedback instead
    # F = -np.dot(k, xh)
    
    # Dynamics of the inverted pendulum
    xp = np.array([
        x[1],
        (F + m * l * x[3]**2 * np.sin(x[2]) - m * g * np.sin(x[2]) * np.cos(x[2])) / d1,
        x[3],
        (-F * np.cos(x[2]) - m * l * x[3]**2 * np.sin(x[2]) * np.cos(x[2]) +
         (M + m) * g * np.sin(x[2])) / d2
    ])
    
    # Return the derivative of the state vector
    return np.concatenate((xp, [dpsi]))

# Initial conditions and time span
x0 = np.array([0, 0, 0.26, 0])
psi0 = 0  # Initial value of psi

# Combine initial conditions
X0 = np.concatenate((x0, [psi0]))

t_span = [0, 3]

# Solve the ODE system using solve_ivp
sol = solve_ivp(inverted_pendulum_luenburger, t_span, X0, method='RK45', t_eval=np.linspace(t_span[0], t_span[1], 100))

# Extract results
t = sol.t
x = sol.y[0:4, :]
psi = sol.y[4, :]
omega = x[3, :]
omega_h = psi + 4 * x[2, :]

# Plotting results
plt.figure()
plt.plot(t, omega, 'k', label='omega')
plt.plot(t, omega_h, '-.k', label='omega_h')
plt.xlabel('Time (sec)')
plt.ylabel('Angular velocity (rad/sec)')
plt.legend()
plt.grid(True)
plt.show()
