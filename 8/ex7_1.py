import numpy as np
from scipy.linalg import solve_continuous_are

# System matrices
A = np.array([[0, 1, 0, 0],
              [0, 0, 4.438, -7.396],
              [0, -12, -24, 0],
              [0, 0, 0, 0]])

C = np.array([[1, 0, 0, 0]])

# Desired closed-loop eigenvalues
pd = np.array([-5 + 5j, -5 - 5j, -7 + 7j, -7 - 7j])

# Compute the optimal gain matrix G using pole placement
G = solve_continuous_are(A.T, C.T, np.eye(4), np.diag(pd.real**2 + pd.imag**2))

# Transpose G to match MATLAB's convention (optional step)
G = G.T

print("Optimal gain matrix G:")
print(G)
