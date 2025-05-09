import numpy as np
from scipy.signal import StateSpace, tf2zpk

# Define matrices
A = np.array([[0, 1], [-2, -3]])
B = np.array([[1], [1]])
C = np.array([[1, 0]])
D = np.array([[0]])

# Convert to state-space representation
sys = StateSpace(A, B, C, D)

# Get eigenvalues
eigs = np.linalg.eigvals(A)

# Get poles
poles = sys.poles

# Get transfer function representation
tf = sys.to_tf()

# Calculate zeros
zeros, _, _ = tf2zpk(tf.num, tf.den)

# Print results
print("Eigenvalues:", eigs)
print("Poles:", poles)
print("Zeros:", zeros)
