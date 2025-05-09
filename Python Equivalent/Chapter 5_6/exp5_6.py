import numpy as np
from scipy.linalg import solve_continuous_lyapunov
A = np.array([[-1, -2], [1, -4]])
Q = np.eye(2)
P = solve_continuous_lyapunov(A.T, -Q)
det_P = np.linalg.det(P)
print("Matrix P (Lyapunov equation solution):")
print(P)
print("\nDeterminant of P:", det_P)