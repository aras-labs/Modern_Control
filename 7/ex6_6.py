import numpy as np

# Define system matrices
A = np.array([[0, 1, 0, 0],
              [0, 0, -9.8, 0],
              [0, 0, 0, 1],
              [0, 0, 19.6, 0]])
b = np.array([[0],
              [1],
              [0],
              [-1]])

# Eigenvalues of A
e, _ = np.linalg.eig(A)
print("Eigenvalues of A:")
print(e)

# Desired closed-loop eigenvalues
pd = np.array([-4.43, -4.43, -2-2j, -2+2j])

# Calculate the gain matrix k using Ackermann's formula
k = np.linalg.solve(np.transpose(b), np.poly(pd))
print("\nCalculated Gain Matrix (k):")
print(k)
