from scipy.integrate import odeint

# Initial state
x0 = [0, 0, 0.6, 0]  # Example initial condition: [x=0, v=0, theta=0.6 rad, omega=0]

# Time span for simulation
tspan = np.linspace(0, 4, 401)  # 401 points from t=0 to t=4

# Numerically integrate the system
sol = odeint(inverted_pendulum_k2, x0, tspan)

# Plot results (example)
import matplotlib.pyplot as plt

plt.plot(tspan, sol[:, 0], 'k', label='x (m)')
plt.plot(tspan, sol[:, 2], 'k-.', label='theta (rad)')
plt.xlabel('Time (sec)')
plt.ylabel('State Variables')
plt.legend()
plt.grid(True)
plt.show()
