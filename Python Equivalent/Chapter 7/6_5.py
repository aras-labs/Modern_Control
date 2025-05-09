import numpy as np

# Define the system matrices
A = np.array([[0, 1, 0, 0],
              [0, 0, -9.8, 0],
              [0, 0, 0, 1],
              [0, 0, 19.6, 0]])

b = np.array([[0],
              [1],
              [0],
              [-1]])

# Controllability matrix
C = np.hstack([b, A @ b, A @ A @ b, A @ A @ A @ b])

# Given parameters
a = np.array([0, -19.6, 0, 0])
alpha = np.array([12.86, 63.065, 149.38, 157.0])

# Construct Psi_1 matrix
Psi_1 = np.array([[1, -a[0], a[0]**2 - a[1], -a[0]**3 + 2*a[0]*a[1] - a[2]],
                  [0, 1, -a[0], a[0]**2 - a[1]],
                  [0, 0, 1, -a[0]],
                  [0, 0, 0, 1]])

# Compute the state feedback gain k
k = (alpha - a) @ Psi_1 @ np.linalg.inv(C)

print("State feedback gain (k):")
print(k)

