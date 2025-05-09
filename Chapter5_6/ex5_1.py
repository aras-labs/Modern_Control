# Import necessary libraries
import numpy as np
import control

# Define the first state-space system
A1 = np.array([[0, 1, 0], [0, 0, 1], [-5, -11, -6]])
B1 = np.array([[0], [0], [1]])
C1 = np.array([[1, 0, 1]])
D1 = np.array([[0]])
sys1 = control.ss(A1, B1, C1, D1)
tf1 = control.ss2tf(sys1)

print("Transfer Function (sys1):")
print(tf1)

# Define the second state-space system
A2 = np.array([[0, 0, -5], [1, 0, -11], [0, 1, -6]])
B2 = np.array([[1], [0], [1]])
C2 = np.array([[0, 0, 1]])
D2 = np.array([[0]])
sys2 = control.ss(A2, B2, C2, D2)
tf2 = control.ss2tf(sys2)

print("\nTransfer Function (sys2):")
print(tf2)

# Define the third state-space system
A3 = np.array([[0, 1, 0], [0, 0, 1], [-5, -11, -6]])
B3 = np.array([[1], [-6], [26]])
C3 = np.array([[1, 0, 0]])
D3 = np.array([[0]])
sys3 = control.ss(A3, B3, C3, D3)
tf3 = control.ss2tf(sys3)

print("\nTransfer Function (sys3):")
print(tf3)

# Observability matrix
O3 = control.obsv(A3, C3)
rank_O3 = np.linalg.matrix_rank(O3)
print("\nObservability Matrix (sys3):")
print(O3)
print("Rank of Observability Matrix (sys3):", rank_O3)

# Define the fourth state-space system
A4 = np.array([[0, 0, -5], [1, 0, -11], [0, 1, -6]])
B4 = np.array([[1], [0], [0]])
C4 = np.array([[1, -6, 26]])
D4 = np.array([[0]])
sys4 = control.ss(A4, B4, C4, D4)
tf4 = control.ss2tf(sys4)

print("\nTransfer Function (sys4):")
print(tf4)

# Controllability matrix
C4 = control.ctrb(A4, B4)
rank_C4 = np.linalg.matrix_rank(C4)
print("\nControllability Matrix (sys4):")
print(C4)
print("Rank of Controllability Matrix (sys4):", rank_C4)

# Transfer function to state-space
num = [1, 0, 1]
den = [1, 6, 11, 5]
sys_tf = control.tf(num, den)
print(control.tf2ss(num, den))
sys5 = control.tf2ss(num, den)
sys_ss = control.ss(sys_tf)

print("\nState-Space Representation from Transfer Function:")
print("A matrix:\n", sys5.A)
print("B matrix:\n", sys5.B)
print("C matrix:\n", sys5.C)
print("D matrix:\n", sys5.D)
