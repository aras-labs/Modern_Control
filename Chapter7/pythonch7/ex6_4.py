import numpy as np

# Define A, b as given
A = np.array([[0, 1, 0, 0],
              [0, 0, -9.8, 0],
              [0, 0, 0, 1],
              [0, 0, 19.6, 0]])

b = np.array([[0], [1], [0], [-1]])  # Note: b should be a column vector

# Calculate controllability matrix C
C = np.hstack([np.linalg.matrix_power(A, i) @ b for i in range(4)])

# Define vectors a and alpha
a = np.array([0, -19.6, 0, 0])
alpha = np.array([12.86, 63.065, 149.38, 157.0])

# Define Psi matrix
Psi = np.array([[1, a[0], a[1], a[2]],
                [0, 1, a[0], a[1]],
                [0, 0, 1, a[0]],
                [0, 0, 0, 1]])

# Calculate k
k = (alpha - a) @ np.linalg.inv(C @ Psi)

print("Optimal gain matrix k:")
print(k)
