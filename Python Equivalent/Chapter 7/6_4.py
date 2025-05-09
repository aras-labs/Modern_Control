# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 12:11:09 2024

@author: Lenovo
"""

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

# Construct Psi matrix
Psi = np.array([[1, a[0], a[1], a[2]],
                [0, 1, a[0], a[1]],
                [0, 0, 1, a[0]],
                [0, 0, 0, 1]])

# Compute the state feedback gain k
k = (alpha - a) @ np.linalg.inv(C @ Psi)

print("State feedback gain (k):")
print(k)
