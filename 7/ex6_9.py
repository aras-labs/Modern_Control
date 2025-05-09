import numpy as np

# Define system matrices
A = np.array([[-2, -1, 2],
              [-1, -2, 2],
              [-2, 0, 2]])

B = np.array([[0, 0],
              [0, 1],
              [1, 0]])

f = np.array([[1],
              [1]])

# Calculate b and C
b = np.dot(B, f)
C = np.linalg.matrix_power(np.hstack((A, np.dot(B, f))), 3)

# Define Psi and delta matrices
Psi = np.array([[1, 2, -1],
                [0, 1, 2],
                [0, 0, 1]])

delta = np.array([4, 13, 10])

# Calculate M
M = np.dot(delta, np.linalg.inv(np.dot(C, Psi)))

# Calculate K1
K1 = np.dot(f.T, M)

# Desired closed-loop eigenvalues
pd = np.array([-2, -2, -2])

# Calculate the gain matrix k using Ackermann's formula
k = np.linalg.solve(np.transpose(b), np.poly(pd))

# Calculate K2
K2 = np.dot(f.T, k)

# Calculate Ac and its eigenvalues
Ac = A - np.dot(B, K1)
eigenvalues_Ac, _ = np.linalg.eig(Ac)

# Display results
print("M matrix:")
print(M)
print("\nK1 matrix:")
print(K1)
print("\nGain matrix k:")
print(k)
print("\nK2 matrix:")
print(K2)
print("\nEigenvalues of Ac:")
print(eigenvalues_Ac)
