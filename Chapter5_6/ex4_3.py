# Import necessary libraries
import numpy as np
from scipy.linalg import null_space

# Define the matrices
A = np.array([[-3/2, 1/2], [1/2, -3/2]])
C = np.array([[1, -1]])

# Compute the observability matrix
O = np.vstack([C, C @ A])

# Compute the rank of the observability matrix
rank_O = np.linalg.matrix_rank(O)

# Compute the null space of the observability matrix
null_O = null_space(O)

# Display the results
print("Observability Matrix (O):")
print(O)

print("\nRank of Observability Matrix (O):")
print(rank_O)

print("\nNull Space of Observability Matrix (O):")
print(null_O)
