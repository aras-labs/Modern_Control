import numpy as np
from scipy.signal import StateSpace, tf2ss
A1 = np.array([[0, 1, 0],
               [0, 0, 1],
               [-5, -11, -6]])
B1 = np.array([[0], [0], [1]])
C1 = np.array([[1, 0, 1]])
D1 = np.array([[0]])
sys1 = StateSpace(A1, B1, C1, D1)
A_tf1, B_tf1, C_tf1, D_tf1 = tf2ss([1, 0, 1], [1, 6, 11, 5])
my_sys1 = StateSpace(A_tf1, B_tf1, C_tf1, D_tf1)
A2 = np.array([[0, 0, -5],
               [1, 0, -11],
               [0, 1, -6]])
B2 = np.array([[1], [0], [1]])
C2 = np.array([[0, 0, 1]])
D2 = np.array([[0]])
sys2 = StateSpace(A2, B2, C2, D2)
A_tf2, B_tf2, C_tf2, D_tf2 = tf2ss([0, 0, 1], [1, 6, 11, 5])
my_sys2 = StateSpace(A_tf2, B_tf2, C_tf2, D_tf2)
A3 = np.array([[0, 1, 0],
               [0, 0, 1],
               [-5, -11, -6]])
B3 = np.array([[1], [-6], [26]])
C3 = np.array([[1, 0, 0]])
D3 = np.array([[0]])
sys3 = StateSpace(A3, B3, C3, D3)
A_tf3, B_tf3, C_tf3, D_tf3 = tf2ss([1, 0, 0], [1, 6, 11, 5])
my_sys3 = StateSpace(A_tf3, B_tf3, C_tf3, D_tf3)
A4 = np.array([[0, 0, -5],
               [1, 0, -11],
               [0, 1, -6]])
B4 = np.array([[1], [0], [0]])
C4 = np.array([[1, -6, 26]])
D4 = np.array([[0]])
sys4 = StateSpace(A4, B4, C4, D4)
A_tf4, B_tf4, C_tf4, D_tf4 = tf2ss([1, -6, 26], [1, 6, 11, 5])
my_sys4 = StateSpace(A_tf4, B_tf4, C_tf4, D_tf4)
print("System 1 - State-Space Representation:")
print(sys1)
print("\nMy System 1 - State-Space Representation:")
print(my_sys1)
print("\nSystem 2 - State-Space Representation:")
print(sys2)
print("\nMy System 2 - State-Space Representation:")
print(my_sys2)
print("\nSystem 3 - State-Space Representation:")
print(sys3)
print("\nMy System 3 - State-Space Representation:")
print(my_sys3)
print("\nSystem 4 - State-Space Representation:")
print(sys4)
print("\nMy System 4 - State-Space Representation:")
print(my_sys4)
