#The outputs from MATLAB and Python are essentially the same, 
#with minor differences in formatting and numerical precision. 
#The core values and structures are consistent across both implementations.



import numpy as np
import control as ctrl

# Define the system matrices
A1 = np.array([[0, 1, 0], [0, 0, 1], [-5, -11, -6]])
B1 = np.array([[0], [0], [1]])
C1 = np.array([[1, 0, 1]])
D1 = np.array([[0]])
sys1 = ctrl.ss(A1, B1, C1, D1)
tf1 = ctrl.ss2tf(sys1)

# Print transfer function for sys1
print("ans =")
print(tf1)
print("Continuous-time transfer function.\n")

# Define the second system matrices
A2 = np.array([[0, 0, -5], [1, 0, -11], [0, 1, -6]])
B2 = np.array([[1], [0], [1]])
C2 = np.array([[0, 0, 1]])
D2 = np.array([[0]])
sys2 = ctrl.ss(A2, B2, C2, D2)
tf2 = ctrl.ss2tf(sys2)

# Print transfer function for sys2
print("ans =")
print(tf2)
print("Continuous-time transfer function.\n")

# Define the third system matrices
A3 = np.array([[0, 1, 0], [0, 0, 1], [-5, -11, -6]])
B3 = np.array([[1], [-6], [26]])
C3 = np.array([[1, 0, 0]])
D3 = np.array([[0]])
sys3 = ctrl.ss(A3, B3, C3, D3)
tf3 = ctrl.ss2tf(sys3)

# Print transfer function for sys3
print("ans =")
print(tf3)
print("Continuous-time transfer function.\n")

# Compute and print observability matrix for sys3
observability_matrix = ctrl.obsv(A3, C3)
print("ans =")
print(observability_matrix)
print("\n")

# Define the fourth system matrices
A4 = np.array([[0, 0, -5], [1, 0, -11], [0, 1, -6]])
B4 = np.array([[1], [0], [0]])
C4 = np.array([[1, -6, 26]])
D4 = np.array([[0]])
sys4 = ctrl.ss(A4, B4, C4, D4)
tf4 = ctrl.ss2tf(sys4)

# Print transfer function for sys4
print("ans =")
print(tf4)
print("Continuous-time transfer function.\n")

# Compute and print controllability matrix for sys4
controllability_matrix = ctrl.ctrb(A4, B4)
print("ans =")
print(controllability_matrix)
print("\n")

# Define transfer function and convert to state space
num = [1, 0, 1]
den = [1, 6, 11, 5]
sys_tf = ctrl.TransferFunction(num, den)
sys_ss = ctrl.tf2ss(sys_tf)
A, B, C, D = sys_ss.A, sys_ss.B, sys_ss.C, sys_ss.D

# Print the state-space matrices
print("A =\n")
print(A)
print("\n")
print("B =\n")
print(B)
print("\n")
print("C =\n")
print(C)
print("\n")
print("D =\n")
print(D)
print("\n")

# Print the full state-space model
print("mysys =\n")
print(sys_ss)
