import numpy as np
from control import ss, lqr

# Define system matrices and cost weights
A = np.array([[0, 1, 0, 0],
              [0, 0, -9.8, 0],
              [0, 0, 0, 1],
              [0, 0, 19.6, 0]])
b = np.array([[0],
              [1],
              [0],
              [-1]])
Q = np.diag([4, 0, 8.16, 0])
R = 1 / 400

# Calculate the LQR gain matrix
k, _, _ = lqr(A, b, Q, R)

# Display the LQR gain matrix
print("LQR Gain Matrix (k):")
print(k)
