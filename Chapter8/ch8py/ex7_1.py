

import numpy as np
import control

# Define the system matrices
A = np.array([[0, 1, 0, 0],
              [0, 0, 4.438, -7.396],
              [0, -12, -24, 0],
              [0, 0, 0, 0]])

B = np.array([[0],
              [0],
              [20],
              [0]])

c = np.array([[1, 0, 0, 0]])  # Ensure c is 2D
pd = np.array([-5+5j, -5-5j, -7+7j, -7-7j])

# Calculate the observer gain using pole placement from control library
G = control.place(A.T, c.T, pd)

print("G =")
print(G)

