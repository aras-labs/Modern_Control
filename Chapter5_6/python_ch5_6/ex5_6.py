import numpy as np
from scipy.linalg import solve_continuous_lyapunov

A = np.array([[-1, -2], [1, -4]])
Q = np.eye(2)
P = solve_continuous_lyapunov(A.T, -Q)
P *= 60  # Scale P by 60 as in the MATLAB code

print("P =\n", np.round(P).astype(int))
print("\ndet(P) =", int(round(np.linalg.det(P))))
