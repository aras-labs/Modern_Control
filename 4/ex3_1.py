import numpy as np
from scipy.linalg import obsv, null_space, matrix_rank

# Define the matrices
A = np.array([[-3/2, 1/2],
              [1/2, -3/2]])
C = np.array([[1, -1]])

# Compute observability matrix
O = obsv(A, C)

# Compute rank of observability matrix
rank_O = matrix_rank(O)

# Compute null space of observability matrix
null_O = null_space(O)

# Display results
print("Observability matrix O:")
print(O)

print("\nRank of O:", rank_O)

print("\nNull space of O:")
print(null_O)
