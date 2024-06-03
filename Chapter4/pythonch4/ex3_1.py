import numpy as np
from scipy.linalg import svd, null_space

# Define matrices
A = np.array([[-3/2, 1/2], [1/2, -3/2]])
C = np.array([[1, -1]])

# Observability matrix
def obsv(A, C):
    n = A.shape[0]
    O = C
    for i in range(1, n):
        O = np.vstack((O, np.dot(C, np.linalg.matrix_power(A, i))))
    return O

O = obsv(A, C)

# Rank of the observability matrix
rank_O = np.linalg.matrix_rank(O)

# Null space of the observability matrix
null_O = null_space(O)

print("Observability matrix (O):")
print(O)
print("\nRank of the observability matrix:")
print(rank_O)
print("\nNull space of the observability matrix:")
print(null_O)
