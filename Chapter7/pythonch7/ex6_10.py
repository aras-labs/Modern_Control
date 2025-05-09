import numpy as np

# Define matrices A, B, and f
A = np.array([[-2, -1, 2], [-1, -2, 2], [-2, 0, 2]])
B = np.array([[0, 0], [0, 1], [1, 0]])
f = np.array([[1], [1]])

# Compute b
b = B @ f

# Compute eigenvalues and eigenvectors of A
eigenvalues, eigenvectors = np.linalg.eig(A)

# Compute inverse of eigenvectors matrix
v = np.linalg.inv(eigenvectors)

# Compute p
p = v[:2, :] @ b

print("p =\n", p)
