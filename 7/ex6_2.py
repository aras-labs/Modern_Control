import numpy as np
from control import ss, place

# Define system matrices and desired poles
A = np.array([[0, 1, 0],
              [0, 0, 4.438],
              [0, -12, -24]])
b = np.array([[0],
              [0],
              [20]])
pd = np.array([-24, -3-3j, -3+3j])  # Desired poles

# Perform pole placement to find the gain matrix
k = place(A, b, pd)

# Display the gain matrix
print("Gain Matrix (k):")
print(k)
