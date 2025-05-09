import numpy as np

# Define the system matrices
A = np.array([[-3/2, 1/2],
              [1/2, -3/2]])
C = np.array([[1, -1]])

# Compute observability matrix and related operations
O = np.vstack((C, np.dot(C, A)))
rank_O = np.linalg.matrix_rank(O)
null_O = np.linalg.matrix_rank(O) == 0

# Print results
print("Observability matrix O:")
print(O)
print("\nRank of observability matrix O:", rank_O)
print("\nIs observability matrix O null:", null_O)
