import numpy as np
import control

# Transfer functions for the DC motor

# Define the state-space matrices
A = np.array([[0, 1, 0],
              [0, 0, 4.438],
              [0, -12, -24]])

b1 = np.array([[0],
               [0],
               [20]])

b2 = np.array([[0],
               [-7.396],
               [0]])

B = np.hstack((b1, b2))
C = np.array([[1, 0, 0]])  # Note only \theta is used as output
D = np.array([[0, 0]])

# Create state-space system
DCM = control.ss(A, B, C, D)

# Conversion to transfer function
DCM_tf = control.tf(DCM)

# Conversion to zero-pole-gain form
DCM_zpk = control.zpk(DCM)

# Display the results
print("Transfer Function:")
print(DCM_tf)

print("\nZero-Pole-Gain:")
print(DCM_zpk)
