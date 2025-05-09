
import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import solve_continuous_are
from scipy.signal import StateSpace
from scipy.integrate import solve_ivp

# Define the system matrices
A = np.array([[0, 1, 0],
              [0, 0, 4.438],
              [0, -12, -24]])

b = np.array([[0],
              [0],
              [20]])

R = np.array([[1]])  # Define R as a 2D array (scalar case)

# Define different values of Q
Q1 = np.diag([4, 0, 0])
Q2 = np.diag([9, 0, 0])
Q3 = np.diag([20, 0, 0])
Q4 = np.diag([9, 3, 0])  # Added Q4

# Function to compute LQR gain matrix K
def compute_lqr_gain(A, b, Q, R):
    P = solve_continuous_are(A, b, Q, R)
    K = np.linalg.inv(R) @ b.T @ P
    return K

# Compute the LQR gains
k1 = compute_lqr_gain(A, b, Q1, R)
k2 = compute_lqr_gain(A, b, Q2, R)
k3 = compute_lqr_gain(A, b, Q3, R)
k4 = compute_lqr_gain(A, b, Q4, R)  # Compute k4

# Define C, D, and x0
C = np.array([[1, 0, 0]])
D = np.array([[0]])
x0 = np.array([-1, 0, 0])

# Closed-loop systems
Acl1 = A - b @ k1
CL_sys1 = StateSpace(Acl1, b, C, D)

Acl2 = A - b @ k2
CL_sys2 = StateSpace(Acl2, b, C, D)

Acl3 = A - b @ k3
CL_sys3 = StateSpace(Acl3, b, C, D)

Acl4 = A - b @ k4  # Acl4
CL_sys4 = StateSpace(Acl4, b, C, D)  # CL_sys4

# Function to simulate initial response
def simulate_initial_response(sys, x0, t_end):
    def system_eq(t, x):
        return np.dot(sys.A, x) + np.dot(sys.B, -np.dot(k1, x))

    sol = solve_ivp(system_eq, [0, t_end], x0, t_eval=np.linspace(0, t_end, 100))
    return sol.y, sol.t, sol

# Simulate initial responses for CL_sys1, CL_sys2, CL_sys3
y1, t1, sol1 = simulate_initial_response(CL_sys1, x0, 2)
u1 = -np.dot(k1, sol1.y)

y2, t2, sol2 = simulate_initial_response(CL_sys2, x0, 2)
u2 = -np.dot(k2, sol2.y)

y3, t3, sol3 = simulate_initial_response(CL_sys3, x0, 2)
u3 = -np.dot(k3, sol3.y)

# Simulate initial response for CL_sys4 (Q4)
y4, t4, sol4 = simulate_initial_response(CL_sys4, x0, 2)
u4 = -np.dot(k4, sol4.y)

# Plotting
plt.figure(1, figsize=(12, 6))

# Plot for angular error
plt.subplot(121)
plt.plot(t1, y1[0], 'k-.', label='Q_{11}=4', linewidth=2)
plt.plot(t2, y2[0], 'k', label='Q_{11}=9', linewidth=2)
plt.plot(t3, y3[0], 'k--', label='Q_{11}=20', linewidth=2)
plt.grid(True)
plt.axis([0, 2, -1, 0.2])
plt.xlabel('Time (sec)')
plt.ylabel('Angular Error (rad)')
plt.legend(loc='best')

# Plot for motor voltage
plt.subplot(122)
plt.plot(t1, u1[0], 'k-.', label='Q_{11}=4', linewidth=2)
plt.plot(t2, u2[0], 'k', label='Q_{11}=9', linewidth=2)
plt.plot(t3, u3[0], 'k--', label='Q_{11}=20', linewidth=2)
plt.grid(True)
plt.xlabel('Time (sec)')
plt.ylabel('Motor Voltage (V)')
plt.legend(loc='best')

# Adjust layout and display plot
plt.tight_layout()
plt.show()

# Figure 2 for Q4
plt.figure(2, figsize=(12, 6))

# Plot for angular error with Q22=0 and Q22=3
plt.subplot(121)
plt.plot(t2, y2[0], 'k', label='Q_{22}=0', linewidth=2)
plt.plot(t4, y4[0], 'k-.', label='Q_{22}=3', linewidth=2)
plt.grid(True)
plt.axis([0, 2, -1, 0.2])
plt.xlabel('Time (sec)')
plt.ylabel('Angular Error (rad)')
plt.legend(loc='best')

# Plot for angular velocity with Q22=0 and Q22=3
plt.subplot(122)
plt.plot(t2, sol2.y[1], 'k', label='Q_{22}=0', linewidth=2)
plt.plot(t4, sol4.y[1], 'k-.', label='Q_{22}=3', linewidth=2)
plt.grid(True)
plt.xlabel('Time (sec)')
plt.ylabel('Angular Velocity (rad/sec)')
plt.legend(loc='best')

# Adjust layout and display plot
plt.tight_layout()
plt.show()

print("k1=", k1)
print("k2=",k2)
print("k3=",k3)
print("k4=",k4)