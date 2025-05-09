# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 12:11:09 2024

@author: Lenovo
"""

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

# Define the weighting matrices
Q = np.diag([4, 0, 8.16, 0])
R = 1 / 400

# Compute the LQR gain
k, _, _ = ctrl.lqr(A, b, Q, R)

print("State feedback gain (k):")
print(k)
