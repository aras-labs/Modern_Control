import numpy as np
import control as ctrl

# Define the first system matrices
A1 = np.array([[-1, 1, 0], [0, -1, 0], [0, 0, -2]])
B1 = np.array([[0], [1], [1]])
C1 = np.array([[4, -8, 9]])
D1 = np.array([[0]])
sys1 = ctrl.ss(A1, B1, C1, D1)
tf1 = ctrl.ss2tf(sys1)

# Print transfer function for sys1
print("ans =")
print(tf1)
print("Continuous-time transfer function.\n")

# Define the second system matrices
A2 = np.array([[-1, 0, 0], [1, -1, 0], [0, 0, -2]])
B2 = np.array([[4], [-8], [9]])
C2 = np.array([[0, 1, 1]])
D2 = np.array([[0]])
sys2 = ctrl.ss(A2, B2, C2, D2)
tf2 = ctrl.ss2tf(sys2)

# Print transfer function for sys2
print("ans =")
print(tf2)
print("Continuous-time transfer function.\n")
