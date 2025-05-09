import numpy as np
import control as ctrl
import matplotlib.pyplot as plt

# State variable 
# x = [dx2   dx3 dx4 dx5 dv1    dv2  dv3  dv4   dv5];
A = np.array([
    [0,     0,    0,    0,    1,    -1,   0,    0,    0],
    [0,     0,    0,    0,    0,     1,  -1,    0,    0],
    [0,     0,    0,    0,    0,     0,   1,   -1,    0],
    [0,     0,    0,    0,    0,     0,   0,    1,   -1],
    [-12.5, 0,    0,    0,   -0.75,  0.75, 0,    0,    0],
    [62.5, -62.5, 0,    0,    3.75, -7.5,  3.75, 0,    0],
    [0,    62.5, -62.5, 0,    0,    3.75, -7.5,  3.75, 0],
    [0,     0,   62.5, -62.5, 0,    0,    3.75, -7.5,  3.75],
    [0,     0,    0,    62.5, 0,    0,    0,    3.75, -3.75]
])

C = np.array([
    [1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 0]
])

# Observability check
O = np.linalg.matrix_rank(ctrl.obsv(A, C))
print("Rank of observability matrix:", O)

# Weight matrices for LQR
W = np.diag([0, 0, 0, 0, 9, 0, 0, 0, 0])
V = np.diag([1e-2, 1])

# LQR design
K, _, _ = ctrl.lqr(A.T, C.T, W, V)

# Display the result
print("G =")
print(K.T)
