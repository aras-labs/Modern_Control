import numpy as np
from scipy.linalg import eig
from scipy.signal import StateSpace

# Define matrices
A = np.array([[0, 1, 0], [0, 0, 4.438], [0, -12, -24]])
b1 = np.array([[0], [0], [20]])
b2 = np.array([[0], [-7.396], [0]])
B = np.hstack((b1, b2))
C = np.array([[1, 0, 0], [0, 1, 0]])
D = np.zeros((2, 1))  # Ensure D is a 2x1 matrix to match the dimensions of C

# Define state-space system (note only first input is used)
DC_motor = StateSpace(A, b1, C, D)

# Calculate eigenvalues and eigenvectors
e, v = eig(A)
ee, w = eig(A.T)

# Sort eigenvalues and corresponding eigenvectors to match MATLAB output
idx = np.argsort(e)
e = np.diag(e[idx])
v = v[:, idx]

idx_ee = np.argsort(ee)
ee = np.diag(ee[idx_ee])
w = w[:, idx_ee]

print("Eigenvalues and eigenvectors of A:")
print("Eigenvalues (e):")
print(e)
print("Eigenvectors (v):")
print(v)

print("\nEigenvalues and eigenvectors of A^T:")
print("Eigenvalues (ee):")
print(ee)
print("Eigenvectors (w):")
print(w)
