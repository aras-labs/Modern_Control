# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 11:59:31 2024

@author: Lenovo
"""

import numpy as np
from scipy.signal import place_poles

# Define the system matrices
A = np.array([[0, 1, 0],
              [0, 0, 4.438],
              [0, -12, -24]])

b = np.array([[0],
              [0],
              [20]])

# Desired closed-loop poles
pd = np.array([-24, -3 - 3j, -3 + 3j])

# Compute the state feedback gain using pole placement
k = place_poles(A, b, pd)

print("State feedback gain (k):")
print(k.gain_matrix)  # Print the state feedback gain matrix
