import numpy as np

# Define the matrix A
A = np.array([[-1, -2],
              [1, -4]])

# Define the identity matrix Q (since Q = eye(2) in MATLAB)
Q = np.eye(2)

# Solve the Lyapunov equation P = A*P*A' + Q using numpy's continuous Lyapunov solver
P = np.linalg.solve(-A.T, Q)

# Compute the determinant of P
det_P = np.linalg.det(P)

# Display results
print("Matrix P:")
print(P)
print("\nDeterminant of P:", det_P)
