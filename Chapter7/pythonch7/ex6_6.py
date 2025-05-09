import numpy as np
from scipy.linalg import eig
from control import acker

# Define A, b as given
A = np.array([[0, 1, 0, 0],
              [0, 0, -9.8, 0],
              [0, 0, 0, 1],
              [0, 0, 19.6, 0]])

b = np.array([[0], [1], [0], [-1]])  # Ensure b is a column vector

# Calculate eigenvalues of A
e, _ = eig(A)
print("Eigenvalues of A:")
print(e)

# Desired poles (desired eigenvalues)
pd = np.array([-4.43, -4.43, -2-2j, -2+2j])

# Compute gain matrix k using acker
k = acker(A, b, pd)
print("\nOptimal gain matrix k:")
print(k)
