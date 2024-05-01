import numpy as np
import control as ctrl


# Define system matrices
A = np.array([[0, 1, 0], [0, 0, 4.438], [0, -12, -24]])
b1 = np.array([[0], [0], [20]])
b2 = np.array([[0], [-7.396], [0]])
B = np.hstack((b1, b2))
C = np.array([[1, 0, 0]])
D = np.array([[0, 0]])

# Create state-space system
DCM = ctrl.ss(A, B, C, D)

# Convert to transfer function
DCM_tf = ctrl.ss2tf(DCM)

# Convert to zero-pole-gain
DCM_zpk = ctrl.ss2zpk(DCM)

# Print the results
print("Transfer Function:")
print(DCM_tf)
print("\nZero-Pole-Gain:")
print(DCM_zpk)
