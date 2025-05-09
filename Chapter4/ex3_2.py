# Import necessary libraries
import sympy as sp

# Define the state-space matrices
A = sp.Matrix([[1, 0], [1, 1]])
B = sp.Matrix([[1], [1]])
u = 1  # Step input
x0 = sp.Matrix([[1], [1]])

# Define the symbolic variable for time
t = sp.symbols('t')

# Calculate the state transition matrix (phi)
phi = sp.exp(A * t)

# Calculate the zero-state response
x1 = sp.exp(-A * t) * B * u
x_zs = sp.integrate(x1, (t))

# Calculate the zero-input response
x_zi = phi * x0

# Calculate the total response
x = x_zi + x_zs

# Display the results
print("State Transition Matrix (phi):")
print(phi)

print("\nZero-State Response (x_zs):")
print(x_zs)

print("\nZero-Input Response (x_zi):")
print(x_zi)

print("\nTotal Response (x):")
print(x)
