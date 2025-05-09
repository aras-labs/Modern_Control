import numpy as np
A = np.array([[-3/2, 1/2], [1/2, -3/2]])
B = np.array([[1/2], [1/2]])
C = np.array([[1, -1]])
def ctrb(A, B):
    n = A.shape[0]
    m = B.shape[1]
    C = np.hstack([np.linalg.matrix_power(A, i) @ B for i in range(n)])
    return C
def obsv(A, C):
    n = A.shape[0]
    m = C.shape[1]
    O = np.vstack([C @ np.linalg.matrix_power(A, i) for i in range(n)])
    return O
def null_space(A, tol=1e-15):
    u, s, vh = np.linalg.svd(A)
    null_mask = (s <= tol)
    null_space = np.compress(null_mask, vh, axis=0)
    return null_space.T
Cn = ctrb(A, B)
print("Controllability Matrix:")
print(Cn)
print("Rank of Controllability Matrix:", np.linalg.matrix_rank(Cn))
print("Null space of Controllability Matrix:")
print(null_space(Cn))
On = obsv(A, C)
print("\nObservability Matrix:")
print(On)
print("Rank of Observability Matrix:", np.linalg.matrix_rank(On))
print("Null space of Observability Matrix:")
print(null_space(On))
