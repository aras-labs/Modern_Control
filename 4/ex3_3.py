from sympy import symbols, exp
import numpy as np

# Define the matrix A and symbolic variable t
A = np.array([[0, 6],
              [-1, -5]])
t = symbols('t')

# Compute the matrix exponential expm(A*t)
exp_A_t = exp(t * A)

# Print the result
print("Matrix exponential expm(A*t):")
print(exp_A_t)
