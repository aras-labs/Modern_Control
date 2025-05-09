import numpy as np
import matplotlib.pyplot as plt

# Define range of k values
k = np.arange(0.02, 5.02, 0.02)

# Initialize x vector
x = np.array([1, 0])

# Calculate J1, J2, J3 for different values of r
r_values = [0, 1, 2]
colors = ['k', 'k-.', 'k--']

plt.figure(figsize=(10, 6))

for i, r in enumerate(r_values):
    p11 = 0.5 / k + 0.5 + (r + 1) * k / 2 + r * k ** 2 / 2
    p12 = 0 / (5 * k) + r * k / 2
    p22 = 0.5 / k + 0.5 + r * k / 2

    J = p11 * x[0] ** 2 + 2 * p12 * x[0] * x[1] + p22 * x[1] ** 2
    plt.plot(k, J, colors[i], linewidth=2, label=f'r={r}')

plt.grid(True)
plt.xlabel('k')
plt.ylabel('J')
plt.legend()
plt.show()

# Plotting the second figure
plt.figure(figsize=(10, 6))

x = np.array([0, 1])
r = 2
p11 = 0.5 / k + 0.5 + (r + 1) * k / 2 + r * k ** 2 / 2
p12 = 0 / (5 * k) + r * k / 2
p22 = 0.5 / k + 0.5 + r * k / 2

J = p11 * x[0] ** 2 + 2 * p12 * x[0] * x[1] + p22 * x[1] ** 2
plt.plot(k, J, 'k', linewidth=2, label=f'r={r}')
plt.plot(k, J2, 'k-.', linewidth=2, label='r=1')

plt.grid(True)
plt.xlabel('k')
plt.ylabel('J')
plt.legend()
plt.show()
