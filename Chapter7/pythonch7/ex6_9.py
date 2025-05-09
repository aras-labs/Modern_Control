
import control
import numpy as np

# Define the matrices and vectors
A = np.array([[-2, -1, 2], [-1, -2, 2], [-2, 0, 2]])
B = np.array([[0, 0], [0, 1], [1, 0]])
f = np.array([[1], [1]])

# Compute b
b = B @ f

# Compute the controllability matrix C
def ctrb(A, b):
    n = A.shape[0]
    C = b
    for i in range(1, n):
        C = np.hstack((C, np.linalg.matrix_power(A, i) @ b))
    return C

C = ctrb(A, b)

# Define Psi and delta
Psi = np.array([[1, 2, -1], [0, 1, 2], [0, 0, 1]])
delta = np.array([4, 13, 10]).reshape(1, -1)  # reshape delta to 1x3

# Compute M
M = delta @ np.linalg.inv(C @ Psi)

print(M)
# Compute K1
K1 = f @ M
print("K1 =\n", K1)

pd = [-2, -2, -2]
# Compute K using acker
K = control.acker(A, b, pd)
print("K =\n", K)

# Compute K2
K2 = f * K 
print("K2 =\n", K2)

Ac = A - B @ K1
print("Ac =\n", Ac)

eigenvalues = np.linalg.eigvals(Ac)
print("Eigenvalues of Ac =\n", eigenvalues)


