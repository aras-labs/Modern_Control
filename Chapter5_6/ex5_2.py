# Import necessary libraries
import numpy as np
import control

# Define the first state-space system
A1 = np.array([[-1, 1, 0], [0, -1, 0], [0, 0, -2]])
B1 = np.array([[0], [1], [1]])
C1 = np.array([[4, -8, 9]])
D1 = np.array([[0]])
sys1 = control.ss(A1, B1, C1, D1)
tf1 = control.ss2tf(sys1)

print("Transfer Function (sys1):")
print(tf1)

# Define the second state-space system
A2 = np.array([[-1, 0, 0], [1, -1, 0], [0, 0, -2]])
B2 = np.array([[4], [-8], [9]])
C2 = np.array([[0, 1, 1]])
D2 = np.array([[0]])
sys2 = control.ss(A2, B2, C2, D2)
tf2 = control.ss2tf(sys2)

print("\nTransfer Function (sys2):")
print(tf2)
