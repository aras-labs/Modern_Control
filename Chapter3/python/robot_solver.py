import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Define the robot model differential equation
def robot_model(x, t):
    # Parameters
    g = 9.81
    l1 = 1
    l2 = 0.5
    m1 = 2
    m2 = 1
    I1 = 1e-2
    I2 = 5e-3
    D = 2
    
    # Mass matrix M
    M = np.array([[m1*(l1/2)**2 + m2*(l1**2 + (l2/2)**2) + m2*l1*l2*np.cos(x[1]) + I1 + I2,
                   m2*(l2/2)**2 + 0.5*m2*l1*l2*np.cos(x[1]) + I2],
                  [m2*(l2/2)**2 + 0.5*m2*l1*l2*np.cos(x[1]) + I2,
                   m2*(l2/2)**2 + I2]])
    
    # Coriolis and centrifugal force vector V
    V = np.array([-m2*l1*l2*np.sin(x[1])*x[2]*x[3] - 0.5*m2*l1*l2*np.sin(x[1])*x[3]**2,
                  -0.5*m2*l1*l2*np.sin(x[1])*x[2]*x[3]])
    
    # Gravitational force vector G
    G = np.array([(m1*l1/2 + m2*l1)*g*np.cos(x[0]) + m2*g*l2/2*np.cos(x[0] + x[1]),
                  m2*g*l2/2*np.cos(x[0] + x[1])])
    
    # Input vector Q
    # Q = np.array([0, 0])  # No input
    # Q -= D * np.array([x[2], x[3]])
    # Input vector Q
    Q = np.array([0.0, 0.0])  # No input, ensure floats
    Q -= D * np.array([x[2], x[3]], dtype=float)  # Ensure floats

    
    
    # Compute acceleration
    xy = np.linalg.pinv(M).dot(Q - V - G)
    
    # Return time derivatives of state variables
    return np.array([x[2], x[3], xy[0], xy[1]])

# Define the time span
tspan = np.linspace(0, 5, 1000)

# Define the initial condition
x0 = [-np.pi/3, np.pi/3, 0, 0]

# Solve the ODE
x = odeint(robot_model, x0, tspan)

# Plot the joint angles against time
plt.plot(tspan, np.degrees(x[:, 0]), 'k', label=r'$\theta_1$ (degrees)')
plt.plot(tspan, np.degrees(x[:, 1]), '-.k', label=r'$\theta_2$ (degrees)')
plt.grid(True)
plt.xlabel('Time (sec)')
plt.ylabel('State Variables')
plt.legend()
plt.setp(plt.gca().lines, linewidth=2)  # Set the linewidth of all lines in the current plot
plt.show()
