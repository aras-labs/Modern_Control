import numpy as np
from scipy.signal import ss2tf, tf2ss, place_poles, tf2ss

# Define the state-space system matrices
A = np.array([[0, 1],
              [-2, -3]])
B = np.array([[1],
              [1]])
C = np.array([[1, 0]])
D = np.array([[0]])

# Create the state-space system
sys = ss(A, B, C, D)

# Compute eigenvalues of matrix A
eigs = np.linalg.eigvals(A)

# Compute poles of the system
poles = sys.pole()

# Compute transmission zeros of the system
zeros = sys.zero()

# Print results
print("Eigenvalues of A:")
print(eigs)

print("\nPoles of the system:")
print(poles)

print("\nTransmission zeros of the system:")
print(zeros)
