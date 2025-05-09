import numpy as np
from scipy.linalg import null_space
A = np.array([[-3/2, 1/2], [1/2, -3/2]])
C = np.array([[1, -1]])
O = np.vstack([C @ np.linalg.matrix_power(A, i) for i in range(A.shape[0])])
rank_O = np.linalg.matrix_rank(O)
null_O = null_space(O)
print("Observability matrix O:")
print(O)
print("\nRank of O:")
print(rank_O)
print("\nNull space of O:")
print(null_O)
