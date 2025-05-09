import numpy as np
import control as ctrl

# Define the system matrices
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

C = np.array([
    [1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 0]
])

# Define the weight matrices for the LQR observer design
W = np.diag([0, 0, 0, 0, 9, 0, 0, 0, 0])
V = np.diag([1e-2, 1])

# Calculate the LQR observer gain
G, _, _ = ctrl.lqr(A.T, C.T, W, V)

# Print the observer gain matrix
print("LQR Observer Gain (G):")
print(G)
