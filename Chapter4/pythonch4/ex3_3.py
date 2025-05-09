import sympy as sp

# Define matrix A
A = sp.Matrix([[0, 6], [-1, -5]])

# Define symbolic variables
t = sp.symbols('t')

# Compute the matrix exponential exp(A*t)
exp_A_t = sp.exp(A * t)

# Print the result
print("expm(A*t):")
sp.pprint(exp_A_t)
