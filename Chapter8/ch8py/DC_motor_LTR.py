import numpy as np
from scipy.linalg import solve_continuous_are, inv, eig
import control

# Define the system matrices
A = np.array([[0, 1, 0, 0],
              [0, 0, 4.438, -7.396],
              [0, -12, -24, 0],
              [0, 0, 0, -1]])

b = np.array([0, 0, 20, 0]).reshape(-1, 1)
c = np.array([1, 0, 0, 0]).reshape(1, -1)

# State feedback design
R = np.array([[1]])
Q1 = np.diag([9, 0, 0, 0])

# Calculate the LQR gain
k, _, _ = control.lqr(A, b, Q1, R)

# State observer design
pd = [-5-5j, -5+5j, -7+7j, -7-7j]

# Calculate the observer gain
G = control.place(A.T, c.T, pd).T

print("k =")
print(k)

print("\nG =")
print(G)
