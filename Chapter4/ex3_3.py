# Import necessary libraries
import sympy as sp

# Define the state-space matrix A
A = sp.Matrix([[0, 6], [-1, -5]])

# Define the symbolic variables
t = sp.symbols('t')

# Calculate the matrix exponential exp(A*t)
expm_A_t = sp.exp(A * t)

# Display the result
print("Matrix Exponential (exp(A*t)):")
print(expm_A_t)
