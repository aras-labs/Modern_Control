# Import necessary libraries
import numpy as np
import scipy.signal as signal

# Define the state-space matrices
A = np.array([[0, 1], [-2, -3]])
B = np.array([[1], [1]])
C = np.array([[1, 0]])
D = np.array([[0]])

# Create the state-space system
sys = signal.StateSpace(A, B, C, D)

# Compute eigenvalues of A
eigs = np.linalg.eigvals(A)

# Compute poles and zeros of the system
poles = sys.poles
zeros = signal.TransferFunction(*signal.ss2tf(A, B, C, D)).zeros

# Display the results
print("Eigenvalues of A:")
print(eigs)

print("\nPoles of the system:")
print(poles)

print("\nZeros of the system:")
print(zeros)
