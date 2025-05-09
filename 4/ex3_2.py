import numpy as np
from sympy import symbols, exp, integrate

# Define the matrices and variables
A = np.array([[1, 0],
              [1, 1]])
B = np.array([[1],
              [1]])
u = 1
x0 = np.array([[1],
               [1]])
t = symbols('t')

# Compute phi = expm(A*t)
phi = np.array(exp(A * t), dtype='float')

# Compute x1 = expm(-A*t) * B * u
x1 = np.dot(np.dot(exp(-A * t), B), u)

# Compute x_zs = int(x1)
x_zs = integrate(x1, t)

# Compute x_zi = phi * x0
x_zi = np.dot(phi, x0)

# Compute x = x_zi + x_zs
x = x_zi + x_zs

# Print the results
print("phi =")
print(phi)

print("\nx_zs =")
print(x_zs)

print("\nx_zi =")
print(x_zi)

print("\nx =")
print(x)
