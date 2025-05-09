import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt


def train_fb(t, x):
    A = np.array([
        [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, -1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, -1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, -1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1, -1],
        [-12.5, 0, 0, 0, 0, -0.75, 0.75, 0, 0, 0],
        [62.5, -62.5, 0, 0, 0, 3.75, -7.5, 3.75, 0, 0],
        [0, 62.5, -62.5, 0, 0, 0, 3.75, -7.5, 3.75, 0],
        [0, 0, 62.5, -62.5, 0, 0, 0, 3.75, -7.5, 3.75],
        [0, 0, 0, 62.5, -62.5, 0, 0, 0, 3.75, -3.75]
    ])

    b1 = np.array([0, 0, 0, 0, 0, 0.005, 0, 0, 0, 0]).reshape(-1, 1)  # Force input
    b2 = np.array([0, 0, 0, 0, 0, 250, 0, 0, 0, -1250]).reshape(-1, 1)  # Constant input

    vd = 25 * (1 - np.exp(-t / 40))  # Desired velocity

    k = np.array([54.5333, 16.2848, -1.3027, -4.3607, 191.7414,
                  -40.4841, -34.2067, -29.7070, -27.3437, 52.0886]).reshape(-1, 1)  # State feedback gains

    dx = np.array([x[1] - 20, x[2] - 20, x[3] - 20, x[4] - 20]).reshape(-1, 1)
    dv = np.array([x[6] - vd, x[7] - vd, x[8] - vd, x[9] - vd, x[10] - vd]).reshape(-1, 1)
    z = x[6] - vd

    X = np.vstack((dx, dv, z))

    u = np.dot(k.T, X)

    xp = np.dot(A, x) + np.dot(b1.T, u) + b2.flatten()

    return xp


# Initial conditions
x0 = [0, 20, 20, 20, 20, 0, 0, 0, 0, 0]  # Initial state [x1, x2, x3, x4, x5, v1, v2, v3, v4, v5]

# Time span
tspan = np.linspace(0, 300, 1001)  # 1001 points from t=0 to t=300

# Numerically integrate the system using odeint
sol = odeint(train_fb, x0, tspan)

# Desired velocity and input force calculation
vd = 25 * (1 - np.exp(-tspan / 40))
k = np.array([54.5333, 16.2848, -1.3027, -4.3607, 191.7414,
              -40.4841, -34.2067, -29.7070, -27.3437, 52.0886])

# Calculate forces
Fs = np.zeros((3, len(tspan)))
for i in range(len(tspan)):
    dx = sol[i, 1:5] - 20
    X = np.hstack((dx, sol[i, 6:11] - vd[i], sol[i, 6] - vd[i]))
    F = -np.dot(k, X)
    Fs[0, i] = F[0]
    Fs[1, i] = F[3]
    Fs[2, i] = 150 * (sol[i, 6] - sol[i, 7])

# Plotting
plt.figure(figsize=(12, 10))

plt.subplot(3, 1, 1)
plt.plot(tspan, sol[:, 0] / 1000, 'k')
plt.xlabel('Time (sec)')
plt.ylabel('Train Position (Km)')
plt.grid(True)

plt.subplot(3, 1, 2)
plt.plot(tspan, vd, 'k', label='Desired Velocity')
plt.plot(tspan, sol[:, 6], '-.k', label='Real Velocity')
plt.xlabel('Time (sec)')
plt.ylabel('Train Velocity (m)')
plt.legend()
plt.grid(True)

plt.subplot(3, 1, 3)
plt.plot(tspan, Fs[0], 'k', label='Input Force')
plt.plot(tspan, Fs[1], '-.k', label='Spring Force 1')
plt.plot(tspan, Fs[2], '--k', label='Damping Force 1')
plt.xlabel('Time (sec)')
plt.ylabel('Force (KN)')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()
