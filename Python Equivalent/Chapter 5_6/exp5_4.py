import numpy as np
num = [[1, 2], [-1, 1]]
den = [[1, 1], [1, 2], [1, 1], [1, 3]]
def nested_lists_to_arrays(nested_list):
    return [np.array(coeff) for coeff in nested_list]
num_np = nested_lists_to_arrays(num)
den_np = nested_lists_to_arrays(den)
def tf(num, den):
    num_poly = np.poly1d(num)
    den_poly = np.poly1d(den)
    return num_poly, den_poly
num_tf, den_tf = tf(num_np[0], den_np[0])
print("Transfer Function (num/den):")
print(num_tf)
print("---")
print(den_tf)
A = np.array([[-1]])
B = np.array([[1], [2]])
C = np.array([[1, 2]])
D = np.array([[0]])
def ss2tf(A, B, C, D):
    return np.linalg.inv(s*np.eye(A.shape[0]) - A) @ B + D
s = np.array([[0, 1], [-1, 0]])
my_sys = np.array([[1/(s+1), 2/(s+2)], [-1/(s+1), 1/(s+3)]])
A_ss = np.array([[0, 1], [-1, -4]])
B_ss = np.array([[0], [0], [1]])
C_ss = np.array([[1, 2]])
D_ss = np.array([[0]])
print("\nState-Space Matrices:")
print("A_ss:\n", A_ss)
print("B_ss:\n", B_ss)
print("C_ss:\n", C_ss)
print("D_ss:\n", D_ss)
