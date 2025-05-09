import numpy as np
from scipy.signal import place_poles

# Define A, b, and pd
A = np.array([[0, 1, 0],
              [0, 0, 4.438],
              [0, -12, -24]])

b = np.array([[0],
              [0],
              [20]])

pd = np.array([-24, -3-3j, -3+3j])

# Place poles using scipy.signal.place_poles
k = place_poles(A, b, pd)

print("Gain matrix k:", k.gain_matrix)
