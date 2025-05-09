import numpy as np
from scipy.linalg import solve_continuous_are

# Define the system matrices
A = np.array([[0,    0,    0,    0,    1,   -1,    0,    0,    0,    0],
              [0,    0,    0,    0,    0,    1,   -1,    0,    0,    0],
              [0,    0,    0,    0,    0,    0,    1,   -1,    0,    0],
              [0,    0,    0,    0,    0,    0,    0,    1,   -1,    0],
              [-12.5, 0,    0,    0,   -0.75, 0.75,  0,    0,    0,    0],
              [62.5, -62.5, 0,    0,    3.75, -7.5,  3.75, 0,    0,    0],
              [0,    62.5, -62.5, 0,    0,    3.75, -7.5,  3.75, 0,    0],
              [0,    0,    62.5, -62.5, 0,    0,    3.75, -7.5,  3.75, 0],
              [0,    0,    0,    62.5, 0,    0,    0,    3.75, -3.75, 0],
              [0,    0,    0,    0,    0,    0,    0,    0,    0,   -1/40]])

B = np.array([[0], [0], [0], [0], [0.005], [0], [0], [0], [0], [0]])

Q = np.diag([3.34**2, 3.34**2, 3.34**2, 3.34**2,
             3**2 + 0.5**2, 2*3**2, 2*3**2, 2*3**2, 3**2, 0.5**2])
Q[5, 4] = -9
Q[4, 5] = -9
Q[6, 5] = -9
Q[5, 6] = -9
Q[7, 6] = -9
Q[6, 7] = -9
Q[8, 7] = -9
Q[7, 8] = -9
Q[9, 8] = -9
Q[8, 9] = -9
Q[9, 4] = 0.5**2
Q[4, 9] = 0.5**2

R = np.array([[1/120**2]])

# Solve the continuous-time Algebraic Riccati equation
P = solve_continuous_are(A, B, Q, R)

# Compute the control gain K
K = np.linalg.inv(R) @ B.T @ P

# Print the control gains K
print(K.flatten())

# Adjust R1 and solve again
R1 = 35 * R
P1 = solve_continuous_are(A, B, Q, R1)
K1 = np.linalg.inv(R1) @ B.T @ P1

# Print the adjusted control gains K1
print(K1.flatten())
