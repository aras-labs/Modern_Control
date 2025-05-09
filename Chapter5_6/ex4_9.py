# Import necessary libraries
import numpy as np
from scipy.linalg import null_space

# Define the matrices
A = np.array([[-3/2, 1/2], [1/2, -3/2]])
B = np.array([[1/2], [1/2]])

# Compute the controllability matrix
C = np.hstack([B, A @ B])

# Compute the rank of the controllability matrix
rank_C = np.linalg.matrix_rank(C)

# Compute the null space of the controllability matrix
null_C = null_space(C)

# Display the results
print("Controllability Matrix (C):")
print(C)

print("\nRank of Controllability Matrix (C):")
print(rank_C)

print("\nNull Space of Controllability Matrix (C):")
print(null_C)
