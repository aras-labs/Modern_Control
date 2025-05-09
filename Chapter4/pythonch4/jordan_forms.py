#Eigenvalues and Eigenvectors
import numpy as np
from scipy.linalg import eig

# Matrix A
A = np.array([[0, 1, 0, 0],
              [0, 0, -9.8, 0],
              [0, 0, 0, 1],
              [0, 0, 19.6, 0]])

# Compute eigenvalues and eigenvectors
eigenvalues, eigenvectors = eig(A)

# Diagonal matrix of eigenvalues
J = np.diag(eigenvalues)

# T is the matrix of eigenvectors
T = eigenvectors

print("T (eigenvectors):")
print(T)
print("\nJ (Jordan form):")
print(J)
####################
#Transformation of B
import numpy as np
from scipy.linalg import eig

# Matrix A and vector B
A = np.array([[0, 1, 0, 0],
              [0, 0, -9.8, 0],
              [0, 0, 0, 1],
              [0, 0, 19.6, 0]])
B = np.array([0, 1, 0, 1]).reshape(-1, 1)

# Compute eigenvalues and eigenvectors
eigenvalues, eigenvectors = eig(A)
J = np.diag(eigenvalues)
T = eigenvectors

# Compute Bn = inv(T) * B
T_inv = np.linalg.inv(T)
Bn = np.dot(T_inv, B)

print("Bn:")
print(Bn)
#################33
#Transformation of C
import numpy as np
from scipy.linalg import eig

# Matrix A, vector B, and matrix C
A = np.array([[0, 1, 0, 0],
              [0, 0, -9.8, 0],
              [0, 0, 0, 1],
              [0, 0, 19.6, 0]])
B = np.array([0, 1, 0, 1]).reshape(-1, 1)
C = np.array([[1, 0, 0, 0],
              [0, 0, 1, 0]])

# Compute eigenvalues and eigenvectors
eigenvalues, eigenvectors = eig(A)
J = np.diag(eigenvalues)
T = eigenvectors

# Compute Bn = inv(T) * B
T_inv = np.linalg.inv(T)
Bn = np.dot(T_inv, B)

# Compute Cn = C * T
Cn = np.dot(C, T)

print("Cn:")
print(Cn)
#####################
#Eigenvalues and Eigenvectors for a Different Matrix A
import numpy as np
from scipy.linalg import eig

# Matrix A
A = np.array([[0, 1, 0, 3],
              [0, -1, 1, 10],
              [0, 0, 0, 1],
              [0, 0, -1, -2]])

# Compute eigenvalues and eigenvectors
eigenvalues, eigenvectors = eig(A)
J = np.diag(eigenvalues)
T = eigenvectors

print("T (eigenvectors):")
print(T)
print("\nJ (Jordan form):")
print(J)
#############
#Jordan Form Using SymPy
import numpy as np
import sympy as sp

# Matrix A
A = np.array([[0, 1, 0, 3],
              [0, -1, 1, 10],
              [0, 0, 0, 1],
              [0, 0, -1, -2]])

# Convert the numpy array to a SymPy Matrix
A_sym = sp.Matrix(A)
# Compute the Jordan form using SymPy
J, P = A_sym.jordan_form()

# Convert back to numpy arrays if needed
J_np = np.array(J).astype(np.float64)
P_np = np.array(P).astype(np.float64)

print("P (Transformation matrix):")
print(P_np)
print("\nJ (Jordan form):")
print(J_np)
