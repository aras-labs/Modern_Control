import numpy as np
from scipy.signal import StateSpace, ss2tf
A1 = np.array([[-1, 1, 0],
               [0, -1, 0],
               [0, 0, -2]])
B1 = np.array([[0], [1], [1]])
C1 = np.array([[4, -8, 9]])
D1 = np.array([[0]])
sys1 = StateSpace(A1, B1, C1, D1)
num1, den1 = ss2tf(A1, B1, C1, D1)
print("System 1 - Transfer Function:")
print(num1, "/", den1)
a2 = np.array([[-1, 0, 0],
               [1, -1, 0],
               [0, 0, -2]])
b2 = np.array([[4], [-8], [9]])
c2 = np.array([[0, 1, 1]])
d2 = np.array([[0]])
sys2 = StateSpace(a2, b2, c2, d2)
num2, den2 = ss2tf(a2, b2, c2, d2)
print("\nSystem 2 - Transfer Function:")
print(num2, "/", den2)
