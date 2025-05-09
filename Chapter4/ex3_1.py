# Import necessary libraries
import numpy as np
from scipy.linalg import null_space

# Define the state-space matrices
A = np.array([
    [-3/2, 1/2],
    [1/2, -3/2]
])
C = np.array([[1, -1]])

# Function to compute the observability matrix
def observability_matrix(A, C):
    n = A.shape[0]
    O = C
    for i in range(1, n):
        O = np.vstack((O, np.dot(C, np.linalg.matrix_power(A, i))))
    return O

# Calculate the observability matrix
O = observability_matrix(A, C)

# Calculate the rank of the observability matrix
rank_O = np.linalg.matrix_rank(O)

# Calculate the null space of the observability matrix
null_O = null_space(O)

# Display the results
print("Observability Matrix (O):")
print(O)
print("\nRank of Observability Matrix:")
print(rank_O)
print("\nNull Space of Observability Matrix:")
print(null_O)
