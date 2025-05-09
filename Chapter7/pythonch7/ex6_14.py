import numpy as np
from scipy.linalg import solve_continuous_are

# Define the system matrices
A = np.array([[0, 1, 0, 0],
              [0, 0, -9.8, 0],
              [0, 0, 0, 1],
              [0, 0, 19.6, 0]])

b = np.array([[0],
              [1],
              [0],
              [-1]])

Q = np.diag([4, 0, 8.16, 0])

# Define R as a 2D array
R = np.array([[1 / 400]])

# Compute the LQR gain matrix K
P = solve_continuous_are(A, b, Q, R)
K = np.linalg.inv(R) @ b.T @ P

print("LQR gain matrix K:")
print(K)
