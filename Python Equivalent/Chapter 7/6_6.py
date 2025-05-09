import numpy as np
import control as ctrl

# Define the system matrices
A = np.array([[0, 1, 0, 0],
              [0, 0, -9.8, 0],
              [0, 0, 0, 1],
              [0, 0, 19.6, 0]])

b = np.array([[0],
              [1],
              [0],
              [-1]])

# Calculate eigenvalues of A
e = np.linalg.eigvals(A)
print("Eigenvalues of A:", e)

# Desired closed-loop poles
pd = np.array([-4.43, -4.43, -2-2j, -2+2j])

# Compute the state feedback gain using pole placement (Ackermann method)
k = ctrl.acker(A, b, pd)

print("State feedback gain (k):")
print(k)
