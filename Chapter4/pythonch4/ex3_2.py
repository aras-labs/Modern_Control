import numpy as np
import sympy as sp

# Define matrices and initial conditions
A = np.array([[1, 0], [1, 1]])
B = np.array([[1], [1]])
u = 1
x0 = np.array([[1], [1]])

# Define symbolic variable t
t = sp.symbols('t')

# Convert numpy arrays to sympy matrices
A_sym = sp.Matrix(A)
B_sym = sp.Matrix(B)
x0_sym = sp.Matrix(x0)

# Compute the matrix exponential exp(A*t) symbolically using sympy
phi = sp.exp(A_sym * t)

# Compute exp(-A*t) * B * u symbolically using sympy
exp_neg_A_t = sp.exp(-A_sym * t)
x1 = exp_neg_A_t * B_sym * u

# Integrate x1 with respect to t symbolically
x_zs = sp.integrate(x1, t)

# Compute phi * x0 symbolically
x_zi = phi * x0_sym

# Compute the final result x symbolically
x = x_zi + x_zs

# Print results in the desired format
print("phi (expm(A*t)):")
sp.pprint(phi)
print("\nx1 (expm(-A*t) * B * u):")
sp.pprint(x1)
print("\nx_zs (integral of x1):")
sp.pprint(x_zs)
print("\nx_zi (phi * x0):")
sp.pprint(x_zi)
print("\nx (x_zi + x_zs):")
sp.pprint(x)
