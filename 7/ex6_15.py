import numpy as np
from control import ss, lqr

# Define system matrices and parameters
A = np.array([[0, 1, 0, 0],
              [0, 0, 4.438, -7.396],
              [0, -12, -24, 0],
              [0, 0, 0, -1]])
b = np.array([[0],
              [0],
              [20],
              [0]])
Q1 = np.diag([9, 0, 0, 0])
R = 1

# Calculate LQR gain
k, _, _ = lqr(A, b, Q1, R)

# Display the LQR gain matrix
print("LQR Gain Matrix (k):")
print(k)
