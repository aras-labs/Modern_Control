import numpy as np

# Define system matrices
A = np.array([[0, 1, 0, 0],
              [0, 0, -9.8, 0],
              [0, 0, 0, 1],
              [0, 0, 19.6, 0]])
b = np.array([[0],
              [1],
              [0],
              [-1]])

# Controllability matrix
C = np.hstack([b, np.dot(A, b), np.dot(A**2, b), np.dot(A**3, b)])

# Given values
a = np.array([0, -19.6, 0, 0])
alpha = np.array([12.86, 63.065, 149.38, 157.0])

# Psi_1 matrix
Psi_1 = np.array([[1, -a[0], a[0]**2 - a[1], -a[0]**3 + 2*a[0]*a[1] - a[2]],
                  [0, 1, -a[0], a[0]**2 - a[1]],
                  [0, 0, 1, -a[0]],
                  [0, 0, 0, 1]])

# Calculate the gain matrix k
k = np.dot((alpha - a), np.dot(Psi_1, np.linalg.inv(C)))

# Display the calculated gain matrix k
print("Calculated Gain Matrix (k):")
print(k)
