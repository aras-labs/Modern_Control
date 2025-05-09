import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from control import ss, lqr, initial_response

# Define system matrices and parameters
A = np.array([[0, 1, 0],
              [0, 0, 4.438],
              [0, -12, -24]])
b = np.array([[0],
              [0],
              [20]])
R = 1
C = np.array([[1, 0, 0]])
D = np.array([[0]])
x0 = np.array([[-1], [0], [0]])

# Define different Q matrices for LQR
Q1 = np.diag([4, 0, 0])
Q2 = np.diag([9, 0, 0])
Q3 = np.diag([20, 0, 0])

# Calculate gains for LQR controllers
k1, _, _ = lqr(A, b, Q1, R)
k2, _, _ = lqr(A, b, Q2, R)
k3, _, _ = lqr(A, b, Q3, R)

# Create closed-loop systems
Acl1 = A - np.dot(b, k1)
CL_sys1 = ss(Acl1, b, C, D)
Acl2 = A - np.dot(b, k2)
CL_sys2 = ss(Acl2, b, C, D)
Acl3 = A - np.dot(b, k3)
CL_sys3 = ss(Acl3, b, C, D)

# Simulate initial response for different Q matrices
t1, y1, x1 = initial_response(CL_sys1, T=np.linspace(0, 2, 100), X0=x0)
u1 = -np.dot(k1, x1.T)

t2, y2, x2 = initial_response(CL_sys2, T=np.linspace(0, 2, 100), X0=x0)
u2 = -np.dot(k2, x2.T)

t3, y3, x3 = initial_response(CL_sys3, T=np.linspace(0, 2, 100), X0=x0)
u3 = -np.dot(k3, x3.T)

# Plot results for angular error and motor voltage
plt.figure(figsize=(12, 6))
plt.subplot(121)
plt.plot(t1, y1.flatten(), 'k-.', label='Q11=4')
plt.plot(t2, y2.flatten(), 'k', label='Q11=9')
plt.plot(t3, y3.flatten(), 'k--', label='Q11=20')
plt.grid(True)
plt.xlabel('Time (sec)')
plt.ylabel('Angular Error (rad)')
plt.legend(loc='best')

plt.subplot(122)
plt.plot(t1, u1.flatten(), 'k-.', label='Q11=4')
plt.plot(t2, u2.flatten(), 'k', label='Q11=9')
plt.plot(t3, u3.flatten(), 'k--', label='Q11=20')
plt.grid(True)
plt.xlabel('Time (sec)')
plt.ylabel('Motor Voltage (V)')
plt.legend(loc='best')
plt.tight_layout()

# Additional Q matrix for comparison
Q4 = np.diag([9, 3, 0])
k4, _, _ = lqr(A, b, Q4, R)
Acl4 = A - np.dot(b, k4)
CL_sys4 = ss(Acl4, b, C, D)

# Simulate initial response for Q22=0 and Q22=3
t4, y4, x4 = initial_response(CL_sys4, T=np.linspace(0, 2, 100), X0=x0)
u4 = -np.dot(k4, x4.T)

# Plot results for angular error and angular velocity
plt.figure(figsize=(12, 6))
plt.subplot(121)
plt.plot(t2, y2.flatten(), 'k', label='Q22=0')
plt.plot(t4, y4.flatten(), 'k-.', label='Q22=3')
plt.grid(True)
plt.xlabel('Time (sec)')
plt.ylabel('Angular Error (rad)')
plt.legend(loc='best')

plt.subplot(122)
plt.plot(t2, x2[:, 1], 'k', label='Q22=0')
plt.plot(t4, x4[:, 1], 'k-.', label='Q22=3')
plt.grid(True)
plt.xlabel('Time (sec)')
plt.ylabel('Angular Velocity (rad/sec)')
plt.legend(loc='best')
plt.tight_layout()

plt.show()
