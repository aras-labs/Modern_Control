from scipy.integrate import odeint
import numpy as np
# Initial state
x0 = [0, 0, 0, 0, 0, 20, 20, 20, 20, 20]  # Example initial condition

# Time span for simulation
tspan = np.linspace(0, 100, 1001)  # 1001 points from t=0 to t=100

# Numerically integrate the system
sol = odeint(train_fb, x0, tspan)

# Plot results (example)
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))

plt.subplot(2, 1, 1)
plt.plot(tspan, sol[:, 0], 'k', label='x1')
plt.plot(tspan, sol[:, 1], 'b', label='x2')
plt.plot(tspan, sol[:, 2], 'g', label='x3')
plt.plot(tspan, sol[:, 3], 'r', label='x4')
plt.plot(tspan, sol[:, 4], 'c', label='x5')
plt.xlabel('Time (sec)')
plt.ylabel('State Variables')
plt.legend()
plt.grid(True)

plt.subplot(2, 1, 2)
plt.plot(tspan, sol[:, 5], 'k', label='v1')
plt.plot(tspan, sol[:, 6], 'b', label='v2')
plt.plot(tspan, sol[:, 7], 'g', label='v3')
plt.plot(tspan, sol[:, 8], 'r', label='v4')
plt.plot(tspan, sol[:, 9], 'c', label='v5')
plt.xlabel('Time (sec)')
plt.ylabel('State Variables')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()
