import numpy as np
import matplotlib.pyplot as plt

# Parameters
k = np.arange(0.02, 5.02, 0.02)
k = k.reshape(-1, 1)
x = np.array([[1], [0]])

# Initialize arrays to store results
J = np.zeros((len(k), 4))

# Compute J values for different r values
for idx, r in enumerate([0, 1, 2]):
    p11 = 0.5 / k + 0.5 + (r + 1) * k / 2 + r * k**2 / 2
    p12 = 0.0 / (5 * k) + r * k / 2
    p22 = 0.5 / k + 0.5 + r * k / 2
    J[:, idx] = p11.flatten() * x[0]**2 + 2 * p12.flatten() * x[0] * x[1] + p22.flatten() * x[1]**2

# Plotting
plt.figure(figsize=(10, 5))

# Plot J vs k for r = 0, 1, 2
plt.subplot(1, 2, 1)
plt.plot(k, J[:, 0], 'k', label='r=0', linewidth=2)
plt.plot(k, J[:, 1], '-.', label='r=1', linewidth=2)
plt.plot(k, J[:, 2], '--', label='r=2', linewidth=2)
plt.xlabel('k')
plt.ylabel('J')
plt.grid(True)
plt.legend()

# Compute J for x = [0, 1] and r = 2
x = np.array([[0], [1]])
p11 = 0.5 / k + 0.5 + (2 + 1) * k / 2 + 2 * k**2 / 2
p12 = 0.0 / (5 * k) + 2 * k / 2
p22 = 0.5 / k + 0.5 + 2 * k / 2
J2 = p11.flatten() * x[0]**2 + 2 * p12.flatten() * x[0] * x[1] + p22.flatten() * x[1]**2

# Plot J vs k for r = 2 and x = [0, 1]
plt.subplot(1, 2, 2)
plt.plot(k, J[:, 2], 'k', label='r=2', linewidth=2)
plt.plot(k, J2, '-.', label='x=[0, 1]', linewidth=2)
plt.xlabel('k')
plt.ylabel('J')
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()
