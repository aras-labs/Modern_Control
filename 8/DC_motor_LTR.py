import numpy as np
from scipy.signal import place_poles
from control.matlab import *

# System matrices
A = np.array([[0, 1, 0, 0],
              [0, 0, 4.438, -7.396],
              [0, -12, -24, 0],
              [0, 0, 0, -1]])

b = np.array([[0], [0], [20], [0]])
c = np.array([[1, 0, 0, 0]])

# LQR Design
Q1 = np.diag([9, 0, 0, 0])
R = 1.0
K, S, E = lqr(A, b, Q1, R)

# LQE Design
pd = [-5-5j, -5+5j, -7+7j, -7-7j]
G = place_poles(A.T, c.T, pd).gain_matrix.T

# Display results
print("LQR gain matrix K:")
print(K)
print("\nLQE gain matrix G:")
print(G)
