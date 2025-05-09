import numpy as np
from scipy.signal import StateSpace
from scipy.linalg import eig

# Define the state-space model matrices
A = np.array([
    [0, 1, 0],
    [0, 0, 4.438],
    [0, -12, -24]
])
b1 = np.array([0, 0, 20]).reshape(-1, 1)  # Reshape to column vector
b2 = np.array([0, -7.396, 0]).reshape(-1, 1)  # Reshape to column vector
B = np.hstack((b1, b2))  # Combine b1 and b2 into B
C = np.array([
    [1, 0, 0],
    [0, 1, 0]
])
D = np.array([[0, 0], [0, 0]])  # D matrix should be 2x2 zero matrix

# Create the state-space model
DC_motor = StateSpace(A, B, C, D)

# Compute the eigenvalues and eigenvectors
eigenvalues, v = eig(A)
eigenvalues_transposed, w = eig(A.T)

# Print the results
print("Eigenvalues and right eigenvectors:")
print(eigenvalues)
print(v)

print("Eigenvalues and left eigenvectors (transposed):")
print(eigenvalues_transposed)
print(w)
