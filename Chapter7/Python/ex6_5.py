# -*- coding: utf-8 -*-
"""ex6_5.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1JiGVZoYXGH4GN1C9SnkXEEI1FnETFk-r
"""

import numpy as np
from scipy.linalg import inv, solve_continuous_lyapunov

# Define matrices and vectors
A = np.array([[0, 1, 0, 0],
              [0, 0, -9.8, 0],
              [0, 0, 0, 1],
              [0, 0, 19.6, 0]])
b = np.array([[0],
              [1],
              [0],
              [-1]])

# Compute controllability matrix
C = np.hstack([b, np.dot(A, b), np.dot(A, np.dot(A, b)), np.dot(A, np.dot(A, np.dot(A, b)))])

# Define other variables
a = np.array([0, -19.6, 0, 0])
alpha = np.array([12.86, 63.065, 149.38, 157.0])

# Construct Psi_1 matrix
Psi_1 = np.array([[1, -a[0], a[0]**2 - a[1], -a[0]**3 + 2*a[0]*a[1] - a[2]],
                  [0, 1, -a[0], a[0]**2 - a[1]],
                  [0, 0, 1, -a[0]],
                  [0, 0, 0, 1]])

# Compute gain matrix k
k = np.dot(np.dot((alpha - a), Psi_1), inv(C))

print("Gain matrix k:")
print(k)