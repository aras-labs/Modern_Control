import numpy as np
import scipy.signal as signal

# Define system matrices for sys1
A1 = np.array([[0, 1, 0],
               [0, 0, 1],
               [-5, -11, -6]])
B1 = np.array([[0],
               [0],
               [1]])
C1 = np.array([[1, 0, 1]])
D1 = np.array([[0]])

# Create state-space system sys1
sys1 = signal.StateSpace(A1, B1, C1, D1)

# Convert sys1 to transfer function
tf1 = signal.ss2tf(sys1.A, sys1.B, sys1.C, sys1.D)

# Display results for sys1
print("System 1 (sys1):")
print("State-space representation (A, B, C, D):")
print(sys1.A)
print(sys1.B)
print(sys1.C)
print(sys1.D)
print("\nTransfer function:")
print(tf1)

# Define system matrices for sys2
a2 = np.array([[0, 0, -5],
               [1, 0, -11],
               [0, 1, -6]])
b2 = np.array([[1],
               [0],
               [1]])
c2 = np.array([[0, 0, 1]])
d2 = np.array([[0]])

# Create state-space system sys2
sys2 = signal.StateSpace(a2, b2, c2, d2)

# Convert sys2 to transfer function
tf2 = signal.ss2tf(sys2.A, sys2.B, sys2.C, sys2.D)

# Display results for sys2
print("\nSystem 2 (sys2):")
print("State-space representation (a, b, c, d):")
print(sys2.A)
print(sys2.B)
print(sys2.C)
print(sys2.D)
print("\nTransfer function:")
print(tf2)

# Define system matrices for sys3
A3 = np.array([[0, 1, 0],
               [0, 0, 1],
               [-5, -11, -6]])
B3 = np.array([[1],
               [-6],
               [26]])
C3 = np.array([[1, 0, 0]])
D3 = np.array([[0]])

# Create state-space system sys3
sys3 = signal.StateSpace(A3, B3, C3, D3)

# Convert sys3 to transfer function
tf3 = signal.ss2tf(sys3.A, sys3.B, sys3.C, sys3.D)

# Display results for sys3
print("\nSystem 3 (sys3):")
print("State-space representation (A, B, C, D):")
print(sys3.A)
print(sys3.B)
print(sys3.C)
print(sys3.D)
print("\nTransfer function:")
print(tf3)

# Compute observability for sys3
O3 = signal.obsv(sys3)
print("\nObservability matrix (O3):")
print(O3)

# Define system matrices for sys4
a4 = np.array([[0, 0, -5],
               [1, 0, -11],
               [0, 1, -6]])
b4 = np.array([[1],
               [0],
               [0]])
c4 = np.array([[1, -6, 26]])
d4 = np.array([[0]])

# Create state-space system sys4
sys4 = signal.StateSpace(a4, b4, c4, d4)

# Convert sys4 to transfer function
tf4 = signal.ss2tf(sys4.A, sys4.B, sys4.C, sys4.D)

# Display results for sys4
print("\nSystem 4 (sys4):")
print("State-space representation (a, b, c, d):")
print(sys4.A)
print(sys4.B)
print(sys4.C)
print(sys4.D)
print("\nTransfer function:")
print(tf4)

# Compute controllability for sys4
C4 = signal.ctrb(sys4)
print("\nControllability matrix (C4):")
print(C4)

# Transfer function representation
num = [1, 0, 1]
den = [1, 6, 11, 5]

# Convert transfer function to state-space
A_tf, B_tf, C_tf, D_tf = signal.tf2ss(num, den)
sys_tf = signal.StateSpace(A_tf, B_tf, C_tf, D_tf)

# Convert state-space back to transfer function
tf_tf = signal.ss2tf(sys_tf.A, sys_tf.B, sys_tf.C, sys_tf.D)

# Display results for transfer function conversion
print("\nTransfer function representation:")
print("State-space representation (A_tf, B_tf, C_tf, D_tf):")
print(A_tf)
print(B_tf)
print(C_tf)
print(D_tf)
print("\nTransfer function:")
print(tf_tf)
