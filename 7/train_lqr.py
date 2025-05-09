import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from scipy.linalg import solve_continuous_are

# State matrix A
A = np.array([
    [0,     0,    0,     0,     1,    -1,     0,     0,     0,     0],
    [0,     0,    0,     0,     0,     1,    -1,     0,     0,     0],
    [0,     0,    0,     0,     0,     0,     1,    -1,     0,     0],
    [0,     0,    0,     0,     0,     0,     0,     1,    -1,     0],
    [-12.5,  0,    0,     0,    -0.75,  0.75,   0,     0,     0,     0],
    [62.5, -62.5,  0,     0,     3.75, -7.5,    3.75,  0,     0,     0],
    [0,    62.5, -62.5,  0,     0,     3.75,  -7.5,   3.75,  0,     0],
    [0,     0,    62.5, -62.5,  0,     0,     3.75, -7.5,   3.75,  0],
    [0,     0,    0,    62.5, -62.5,  0,     0,     0,     3.75, -3.75],
    [0,     0,    0,     0,     0,     0,     0,     0,     0,    -1/40]
])

# Input matrix B
B = np.array([0, 0, 0, 0, 0.005, 0, 0, 0, 0, 0]).reshape(-1, 1)

# Cost matrices Q and R
Q = np.diag([3.34**2, 3.34**2, 3.34**2, 3.34**2, 3**2 + 0.5**2,
             2 * 3**2, 2 * 3**2, 2 * 3**2, 3**2, 0.5**2])
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

R = 1 / 120**2
R1 = 35 * R

# Calculate the LQR gain matrix for R = 1/120^2
K = solve_continuous_are(A, B, Q, R)
# Calculate the LQR gain matrix for R1 = 35 * 1/120^2
K1 = solve_continuous_are(A, B, Q, R1)

# Print the results
print("LQR Gain Matrix K (R = 1/120^2):")
print(K)
print("\nLQR Gain Matrix K1 (R1 = 35 * 1/120^2):")
print(K1)
