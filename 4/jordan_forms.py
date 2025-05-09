import numpy as np

# Example 1: Inverted Pendulum
A1 = np.array([[0, 1, 0, 0],
               [0, 0, -9.8, 0],
               [0, 0, 0, 1],
               [0, 0, 19.6, 0]])
B1 = np.array([[0],
               [1],
               [0],
               [1]])
C1 = np.array([[1, 0, 0, 0],
               [0, 0, 1, 0]])

# Compute the Jordan form and transformation matrices for Example 1
T1, J1 = np.linalg.eig(A1)

# Transform B and C using the Jordan transformation matrix T1
T1_inv = np.linalg.inv(T1)
B1n = np.dot(T1_inv, B1)
C1n = np.dot(C1, T1)

# Print results for Example 1
print("Example 1: Inverted Pendulum")
print("Jordan form T:")
print(T1)
print("\nTransformed Bn:")
print(B1n)
print("\nTransformed Cn:")
print(C1n)

print("\n----------------------------------------\n")

# Example 2: Example 3-13
A2 = np.array([[0, 1, 0, 3],
               [0, -1, 1, 10],
               [0, 0, 0, 1],
               [0, 0, -1, -2]])

# Compute the Jordan form and transformation matrices for Example 2
T2, J2 = np.linalg.eig(A2)

# Print results for Example 2
print("Example 2: Example 3-13")
print("Jordan form T:")
print(T2)
