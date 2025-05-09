import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint


# Define global parameter
class Par:
    Tl = 0.01


# Define the DC motor model function with observer
def DC_motor_LTR1(x, t):
    # System parameters
    R = 1.5  # Ohms
    L = 0.5  # Henry
    J = 0.01  # kg.m^2
    b = 0.1  # N.m.s
    Ke = 0.01  # V/rad/sec
    Kt = 0.01  # N.m/Amp

    # Observer gains
    L1 = 15
    L2 = 12
    L3 = 10

    # State variables
    theta = x[0]
    omega = x[1]
    i = x[2]

    theta_h = x[3]
    omega_h = x[4]
    i_h = x[5]

    # Disturbance torque
    Tl = Par.Tl * np.exp(-t)
    Tl_h = x[6]

    # System dynamics (state equations)
    dtheta_dt = omega
    domega_dt = (-b / J) * omega + (Kt / J) * (i - i_h)
    di_dt = (-R / L) * i - (Ke / L) * omega + (1 / L) * Tl

    # Observer dynamics
    dtheta_h_dt = omega_h
    domega_h_dt = (-b / J) * omega_h + (Kt / J) * (i_h - L1 * (theta_h - theta))
    di_h_dt = (-R / L) * i_h - (Ke / L) * omega_h + L2 * (omega_h - omega) - L3 * (i_h - i)

    # Disturbance torque estimate dynamics
    dTl_h_dt = L3 * (i_h - i)

    return [dtheta_dt, domega_dt, di_dt, dtheta_h_dt, domega_h_dt, di_h_dt, dTl_h_dt]


# Initial conditions
x0 = [0, 0, 0, 0, 0, 0, 0]

# Time span for simulation
t = np.linspace(0, 5, 500)  # Adjust the number of time points as needed

# Solve the ODE system
x = odeint(DC_motor_LTR1, x0, t)

# Plotting results
plt.figure(figsize=(12, 10))

# Subplot for Angular displacement
plt.subplot(221)
plt.plot(t, x[:, 0], 'k', label=r'$\theta$')
plt.plot(t, x[:, 3], '-.k', label=r'$\theta_h$')
plt.grid(True)
plt.xlabel('Time (sec)')
plt.ylabel('Angular displacement (rad)')
plt.legend()

# Subplot for Angular velocity
plt.subplot(222)
plt.plot(t, x[:, 1], 'k', label=r'$\omega$')
plt.plot(t, x[:, 4], '-.k', label=r'$\omega_h$')
plt.grid(True)
plt.xlabel('Time (sec)')
plt.ylabel('Angular velocity (rad/sec)')
plt.legend()

# Subplot for Motor Current
plt.subplot(223)
plt.plot(t, x[:, 2], 'k', label='i')
plt.plot(t, x[:, 5], '-.k', label='i_h')
plt.grid(True)
plt.xlabel('Time (sec)')
plt.ylabel('Motor Current (Amp)')
plt.legend()

# Subplot for Disturbance Torque
plt.subplot(224)
plt.plot(t, Par.Tl * np.exp(-t), 'k', label='Tl')
plt.plot(t, x[:, 6], '-.k', label='Tl_h')
plt.grid(True)
plt.xlabel('Time (sec)')
plt.ylabel('Disturbance torque (N.m)')
plt.legend()

plt.tight_layout()
plt.show()
