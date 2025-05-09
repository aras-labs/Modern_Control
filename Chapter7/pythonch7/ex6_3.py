import numpy as np
import control

# Define A, b, Q, R as previously defined
A = np.array([[0, 1, 0, 0],
              [0, 0, -9.8, 0],
              [0, 0, 0, 1],
              [0, 0, 19.6, 0]])

b = np.array([0, 1, 0, -1])

Q = np.diag([4, 0, 8.16, 0])
R = 1 / 400

# Compute optimal gain matrix k using LQR
k, _, _ = control.lqr(A, b[:, np.newaxis], Q, R)

print("Optimal gain matrix k:")
print(k)
