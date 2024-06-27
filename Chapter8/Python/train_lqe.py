

import numpy as np
from scipy.linalg import solve_continuous_are, eigvals

# Define the system matrix A
A = np.array([
    [0, 0, 0, 0, 1, -1, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, -1, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, -1, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, -1],
    [-12.5, 0, 0, 0, -0.75, 0.75, 0, 0, 0],
    [62.5, -62.5, 0, 0, 3.75, -7.5, 3.75, 0, 0],
    [0, 62.5, -62.5, 0, 0, 3.75, -7.5, 3.75, 0],
    [0, 0, 62.5, -62.5, 0, 0, 3.75, -7.5, 3.75],
    [0, 0, 0, 62.5, 0, 0, 0, 3.75, -3.75]
])

# Define the output matrix C
C = np.array([
    [1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 0]
])

# Compute the observability matrix
O = np.hstack([np.dot(np.linalg.matrix_power(A, i), C.T) for i in range(A.shape[0])])

# Check the rank of the observability matrix
rank_O = np.linalg.matrix_rank(O)
print("Rank of observability matrix:", rank_O)

# Define the weight matrices W and V
W = np.diag([0, 0, 0, 0, 9, 0, 0, 0, 0])
V = np.diag([1e-2, 1])

# Solve the continuous-time Algebraic Riccati Equation (ARE)
P = solve_continuous_are(A.T, C.T, W, V)

# Compute the observer gain matrix G
G = np.dot(np.linalg.inv(V), np.dot(C, P)).T

print("Observer gain matrix G:")
print(G)
