import numpy as np

# Define the state-space matrices
A = np.array([[0, 1, 0, 0],
              [0, 0, 1, 0],
              [0, 0, 0, 1],
              [-2, -3, -3, -3]])

B = np.array([[0],
              [0],
              [0],
              [1]])

C = np.array([[2, 1, 0, 0],
              [0, 1, 0, 1]])

D = np.array([[0],
              [0]])

# Function to compute transfer function for each output
def compute_transfer_function(A, B, C, D):
    s = np.linalg.eigvals(A)  # Get eigenvalues for s domain
    I = np.eye(A.shape[0])
    transfer_functions = []

    for i in range(C.shape[0]):  # Iterate over each output
        for j in range(B.shape[1]):  # Iterate over each input
            # Compute transfer function H(s) = C(sI - A)^-1 B + D
            C_i = C[i, :].reshape(1, -1)
            B_j = B[:, j].reshape(-1, 1)
            H_s = []

            for s_val in s:
                sI_minus_A = s_val * I - A
                sI_minus_A_inv = np.linalg.inv(sI_minus_A)
                H_s_val = np.dot(C_i, np.dot(sI_minus_A_inv, B_j)) + D[i, j]
                H_s.append(H_s_val[0, 0])

            transfer_functions.append(H_s)

    return transfer_functions

# Compute transfer functions
tf_list = compute_transfer_function(A, B, C, D)

# Print transfer functions
for i, tf in enumerate(tf_list):
    output_index = i // B.shape[1] + 1
    input_index = i % B.shape[1] + 1
    print(f"Transfer Function for output {output_index}, input {input_index}:")
    print(tf)
    print()
