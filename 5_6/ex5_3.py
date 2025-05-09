import numpy as np
import scipy.signal as signal

# Define numerator and denominator arrays for transfer function
num1 = [1]
num2 = [1, 0]
den1 = np.convolve([1, 0, 1], [1, 1])
den2 = [1, 3, 2]

# Create transfer function sys
sys = signal.TransferFunction(num1, den1)
sys.num = num2  # Assign the second numerator

# Display sys as a transfer function
print("Transfer function (sys):")
print(sys)

# Convert sys to zero-pole-gain form (ZPK)
sys1 = signal.TransferFunction(num1, den1).to_zpk()
print("\nZero-pole-gain form (sys1):")
print(sys1)

# Convert sys to state-space form (SS)
sys2 = signal.TransferFunction(num1, den1).to_ss()
sys2_minreal = signal.minreal(sys2)  # Compute minimal realization of SS form

print("\nState-space form (sys2):")
print(sys2)
print("\nMinimal realization (sys2_minreal):")
print(sys2_minreal)

# Define symbolic variable 's'
s = signal.TransferFunction([1, 0], [1])

# Define and simplify symbolic system mysys
mysys = [1/((s**2 + 1)*(s + 1)), s/((s + 1)*(s + 2))]
myss = signal.minreal(signal.TransferFunction(mysys))

print("\nSymbolic system (mysys):")
print(mysys)
print("\nMinimal realization (myss):")
print(myss)

# Define state-space matrices for sys
A = np.array([[0, 1, 0, 0],
              [0, 0, 1, 0],
              [0, 0, 0, 1],
              [-2, -3, -3, -3]])
B = np.array([[0],
              [0],
              [0],
              [1]])
C = np.array([[2, 1, 0, 0],
              [0, 1, 0, 1]])
D = np.array([[0],
              [0]])

# Create state-space system sys
sys = signal.StateSpace(A, B, C, D)

# Convert sys to transfer function
tf_sys = signal.ss2tf(sys.A, sys.B, sys.C, sys.D)

# Display results for sys
print("\nState-space representation (sys):")
print("A:\n", sys.A)
print("B:\n", sys.B)
print("C:\n", sys.C)
print("D:\n", sys.D)

print("\nTransfer function (tf_sys):")
print(tf_sys)

# Convert sys to zero-pole-gain form (ZPK)
zpk_sys = signal.ss2zpk(sys.A, sys.B, sys.C, sys.D)
print("\nZero-pole-gain form (zpk_sys):")
print(zpk_sys)
