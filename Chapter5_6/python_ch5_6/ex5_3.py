import numpy as np
import control as ctrl

# Define numerator and denominator lists for each SISO system
num1 = [1]  # First transfer function numerator
den1 = np.convolve([1, 0, 1], [1, 1]).tolist()  # First transfer function denominator

num2 = [1, 0]  # Second transfer function numerator
den2 = [1, 3, 2]  # Second transfer function denominator

# Combine them into MIMO system
num = [[num1], [num2]]
den = [[den1], [den2]]

# Create transfer function
sys = ctrl.tf(num, den)

print(sys)
####################################
import numpy as np
import control as ctrl

# Define numerator and denominator lists for each SISO system
num1 = [1]  # First transfer function numerator
den1 = np.convolve([1, 0, 1], [1, 1]).tolist()  # First transfer function denominator

num2 = [1, 0]  # Second transfer function numerator
den2 = [1, 3, 2]  # Second transfer function denominator

# Combine them into MIMO system
num = [[num1], [num2]]
den = [[den1], [den2]]

# Create transfer function
sys = ctrl.tf(num, den)

# Convert transfer function to zero-pole-gain form
z1, p1, k1 = ctrl.tf2zpk(num[0][0], den[0][0])
z2, p2, k2 = ctrl.tf2zpk(num[1][0], den[1][0])

# Create zero-pole-gain system
sys1_1 = ctrl.ZerosPolesGain(z1, p1, k1)
sys1_2 = ctrl.ZerosPolesGain(z2, p2, k2)

print(sys1_1)
print(sys1_2)


