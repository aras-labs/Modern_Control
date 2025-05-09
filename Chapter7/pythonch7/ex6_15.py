import numpy as np
from scipy.linalg import solve_continuous_are

# Define the system matrices
A = np.array([[0, 1, 0, 0],
              [0, 0, 4.438, -7.396],
              [0, -12, -24, 0],
              [0, 0, 0, -1]])

b = np.array([[0],
              [0],
              [20],
              [0]])

Q1 = np.diag([9, 0, 0, 0])
R = np.array([[1]])  # Define R as a 2D array (scalar case)

# Compute the LQR gain matrix K
P = solve_continuous_are(A, b, Q1, R)
K = np.linalg.inv(R) @ b.T @ P

print("LQR gain matrix K:")
print(K)
