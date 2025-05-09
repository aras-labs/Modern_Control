import numpy as np

# Define system matrices and vector
A = np.array([[-2, -1, 2],
              [-1, -2, 2],
              [-2, 0, 2]])
B = np.array([[0, 0],
              [0, 1],
              [1, 0]])
f = np.array([[1],
              [1]])

# Calculate b
b = np.dot(B, f)

# Eigen decomposition of A
w, v = np.linalg.eig(A)
v_inv = np.linalg.inv(v)

# Calculate p
p = np.dot(v_inv[:2, :], b)

# Print results
print("Eigenvalues of A:")
print(w)
print("\nMatrix of eigenvectors W:")
print(w)
print("\nInverse of W:")
print(v_inv)
print("\np (projection of b onto the first two eigenvectors of A):")
print(p)
