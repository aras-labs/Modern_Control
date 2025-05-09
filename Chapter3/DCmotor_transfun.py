# Import necessary libraries
import sympy as sp

# Define symbolic variables
s = sp.symbols('s')

# Define the system matrices (DC motor example)
A = sp.Matrix([[0, 1, 0],
               [0, 0, 4.438],
               [0, -12, -24]])
b1 = sp.Matrix([[0], [0], [20]])
b2 = sp.Matrix([[0], [-7.396], [0]])
B = sp.Matrix.hstack(b1, b2)
C = sp.Matrix([[1, 0, 0]])  # Only theta is used as output
D = sp.Matrix([[0, 0]])     # Two inputs, so D is 1x2 matrix

# Calculate (sI - A)^(-1)
sI_A_inv = (s*sp.eye(A.shape[0]) - A).inv()

# Calculate the transfer function G(s) = C(sI - A)^(-1)B + D
G = C*sI_A_inv*B + D

# Simplify expressions
sI_A_inv_simp = sp.simplify(sI_A_inv)
G_simp = sp.simplify(G)

# Print the results
print("(sI - A)^(-1) =")
sp.pprint(sI_A_inv_simp)
print("\nG(s) =")
sp.pprint(G_simp)

# Print the LaTeX formatted output
print("\nLaTeX formatted output:")
print("$G(s) = $", sp.latex(G_simp))
print("$[sI - A]^{-1} = $", sp.latex(sI_A_inv_simp))
