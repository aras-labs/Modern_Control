import numpy as np

# Define the system matrices
A = np.array([[-3/2, 1/2],
              [1/2, -3/2]])
B = np.array([[1/2],
              [1/2]])

# Compute controllability matrix and related operations
C = np.hstack((B, np.dot(A, B)))
rank_C = np.linalg.matrix_rank(C)
null_C = np.linalg.matrix_rank(C) == 0

# Print results
print("Controllability matrix C:")
print(C)
print("\nRank of controllability matrix C:", rank_C)
print("\nIs controllability matrix C null:", null_C)
