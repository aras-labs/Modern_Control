# Import necessary libraries
import sympy as sp

# Define the matrices for Inverted Pendulum
A1 = sp.Matrix([
    [0, 1, 0, 0],
    [0, 0, -9.8, 0],
    [0, 0, 0, 1],
    [0, 0, 19.6, 0]
])
B1 = sp.Matrix([0, 1, 0, 1])
C1 = sp.Matrix([
    [1, 0, 0, 0],
    [0, 0, 1, 0]
])

# Compute the Jordan form
T1, J1 = A1.jordan_form()

# Compute transformed B and C
Bn1 = T1.inv() * B1
Cn1 = C1 * T1

# Display the results
print("Inverted Pendulum Jordan Form:")
sp.pretty_print(J1)
print("\nTransformation Matrix T:")
sp.pretty_print(T1)
print("\nTransformed B (Bn):")
sp.pretty_print(Bn1)
print("\nTransformed C (Cn):")
sp.pretty_print(Cn1)

# Define the matrices for Example 3-13
A2 = sp.Matrix([
    [0, 1, 0, 3],
    [0, -1, 1, 10],
    [0, 0, 0, 1],
    [0, 0, -1, -2]
])

# Compute the Jordan form
T2, J2 = A2.jordan_form()

# Display the results
print("\nExample 3-13 Jordan Form:")
sp.pretty_print(J2)
print("\nTransformation Matrix T:")
sp.pretty_print(T2)
