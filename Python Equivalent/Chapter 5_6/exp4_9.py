import numpy as np
from scipy.linalg import null_space
A = np.array([[-3/2, 1/2],
              [1/2, -3/2]])
B = np.array([[1/2], [1/2]])
n = A.shape[0]
C = np.zeros((n, n))
Cb = B
for i in range(n):
    C[:, i:i+1] = Cb
    Cb = A @ Cb
rank_C = np.linalg.matrix_rank(C)
null_C = null_space(C)
print("Controllability matrix C:")
print(C)

print("\nRank of C:")
print(rank_C)

print("\nNull space of C:")
print(null_C)
