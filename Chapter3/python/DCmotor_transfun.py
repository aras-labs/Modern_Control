import numpy as np
from scipy import signal

# Define system matrices
A = np.array([[0, 1, 0], [0, 0, 4.438], [0, -12, -24]])
b1 = np.array([[0], [0], [20]])
b2 = np.array([[0], [-7.396], [0]])
B = np.hstack((b1, b2))
C = np.array([[1, 0, 0]])
D = np.array([[0, 0]])

# Convert to transfer function
num, den = signal.ss2tf(A, B, C, D)
DCM_tf = signal.TransferFunction(num[0, :], den[0])

# Convert to zero-pole-gain form
DCM_zpk = signal.ss2zpk(A, B, C, D)

# Print transfer function
print("Transfer Function:")
print(DCM_tf)

# Print zero-pole-gain form
print("\nZero-Pole-Gain Form:")
print(DCM_zpk)
