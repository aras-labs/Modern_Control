# Import necessary libraries
import numpy as np
from scipy import signal

# Define the state-space matrices
A = np.array([
    [0, 1, 0],
    [0, 0, 4.438],
    [0, -12, -24]
])
b1 = np.array([0, 0, 20]).reshape(-1, 1)
b2 = np.array([0, -7.396, 0]).reshape(-1, 1)
B = np.hstack((b1, b2))
C = np.array([
    [1, 0, 0],
    [0, 1, 0]
])
D = np.array([[0], [0]])

# Create the state-space model using signal.StateSpace
DC_motor = signal.StateSpace(A, b1, C, D)  # Note only first input is used

# Calculate the eigenvalues and right eigenvectors of A
eigenvalues, right_eigenvectors = np.linalg.eig(A)

# Calculate the left eigenvectors of A
_, left_eigenvectors = np.linalg.eig(A.T)

# Display the results
print("Right Eigenvectors (V):")
print(right_eigenvectors)
print("Eigenvalues (Lambda):")
print(eigenvalues)
print("Left Eigenvectors (W):")
print(left_eigenvectors)
