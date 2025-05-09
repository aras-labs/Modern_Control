import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Define system parameters
k = np.array([54.5333, 16.2848, -1.3027, -4.3607, 191.7414,
              -40.4841, -34.2067, -29.7070, -27.3437])  # Design parameters

Ks = 2.5e3  # Spring coefficient (KN/m)
Ds = 1.5e2  # Damper coefficient (KN/m/s)

def train_fb(x, t):
    # Define system parameters
    vd = 25 * (1 - np.exp(-t / 40))  # Desired velocity function
    
    # Extract state variables
    dx = x[1:5] - 20  # x2-x11 - 20
    dv = x[6:10] - vd  # x12-x16 - vd
    
    # Calculate input force
    z = x[6] - vd
    X = np.concatenate((dx, dv, [z]))
    F = -np.dot(k, X)
    Fs = np.array([Ks * dx[0], Ks * dx[3]])  # Spring forces 1 and 4
    
    # Calculate damping forces
    D1 = Ds * (x[6] - x[7])
    D4 = Ds * (x[8] - x[9])
    
    # Return derivatives
    return [x[1], F, Fs[0], x[3], Fs[1], x[5], x[7], x[9], D1, D4]

# Initial conditions and time span
t_span = np.linspace(0, 300, 1000)  # from 0 to 300 seconds
x0 = np.array([0, 20, 20, 20, 20, 0, 0, 0, 0, 0])

# Solve the differential equation
x = odeint(train_fb, x0, t_span)

# Extract results for plotting
t = t_span
vd = 25 * (1 - np.exp(-t / 40))
F = np.zeros_like(t)
Fs1 = np.zeros_like(t)
Fs4 = np.zeros_like(t)
D1 = np.zeros_like(t)
D4 = np.zeros_like(t)

for i in range(len(t)):
    dx = x[i, 1:5] - 20
    dv = x[i, 6:10] - vd[i]
    z = x[i, 6] - vd[i]
    X = np.concatenate((dx, dv, [z]))
    F[i] = -np.dot(k, X)
    Fs1[i] = Ks * dx[0]
    Fs4[i] = Ks * dx[3]
    D1[i] = Ds * (x[i, 6] - x[i, 7])
    D4[i] = Ds * (x[i, 8] - x[i, 9])

# Plotting
plt.figure(figsize=(12, 10))

# Train position and velocity
plt.subplot(321)
plt.plot(t, x[:, 0] / 1000, 'k')
plt.grid(True)
plt.xlabel('Time (sec)')
plt.ylabel('Train Position (Km)')

plt.subplot(322)
plt.plot(t, vd, 'k', label='Desired Velocity')
plt.plot(t, x[:, 5], '-.k', label='Real Velocity')
plt.grid(True)
plt.xlabel('Time (sec)')
plt.ylabel('Train Velocity (m)')
plt.legend()

# Forces
plt.subplot(323)
plt.plot(t, F, 'k', label='Input Force')
plt.plot(t, Fs1, '-.k', label='Spring Force 1')
plt.plot(t, Fs4, '--k', label='Spring Force 4')
plt.grid(True)
plt.xlabel('Time (sec)')
plt.ylabel('Force (KN)')
plt.legend()

plt.subplot(324)
plt.plot(t, D1, 'k', label='Damping Force 1')
plt.plot(t, D4, '-.k', label='Damping Force 4')
plt.grid(True)
plt.xlabel('Time (sec)')
plt.ylabel('Force (KN)')
plt.legend()

plt.tight_layout()
plt.show()
