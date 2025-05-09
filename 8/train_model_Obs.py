import numpy as np
from scipy.integrate import odeint


# Define the train model function
def train_model1(X, t):
    global Par

    # Parameters and variables
    x = X[:10]
    xh = X[10:19]

    # System matrices
    A = np.array([
        [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, -1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, -1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, -1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1, -1],
        [0, -12.5, 0, 0, 0, -0.75, 0.75, 0, 0, 0],
        [0, 62.5, -62.5, 0, 0, 3.75, -7.5, 3.75, 0, 0],
        [0, 0, 62.5, -62.5, 0, 0, 3.75, -7.5, 3.75, 0],
        [0, 0, 0, 62.5, -62.5, 0, 0, 3.75, -7.5, 3.75],
        [0, 0, 0, 0, 62.5, 0, 0, 0, 3.75, -3.75]
    ])

    b1 = np.array([0, 0, 0, 0, 0, 0.005, 0, 0, 0, 0])  # Force input
    b2 = np.array([0, 0, 0, 0, 0, 250, 0, 0, 0, -1250])  # Constant input

    # Control law
    if t < 10:
        u = Par.F  # Constant Force
        uh = 0.5 * u
    else:
        u = 0
        uh = u

    xp = np.dot(A, x) + np.dot(b1, u) + np.dot(b2, u)

    # Output matrix
    C = np.array([
        [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 0, 0]
    ])
    y = np.dot(C, x)
    dy = np.array([y[0] - 20, y[1]])

    # Observer matrices
    Ah = A.copy()
    Bh = np.array([0, 0, 0, 0, 0.005, 0, 0, 0, 0])
    Ch = np.array([
        [1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0]
    ])

    # Observer gain matrix G
    G = np.array([
        [10.5008, 0.0472],
        [4.0624, 0.0100],
        [1.2245, 0.0004],
        [0.3222, -0.0007],
        [118.1098, 1.1441],
        [60.1867, 0.5240],
        [16.7939, 0.3003],
        [-0.0227, 0.2370],
        [-4.2587, 0.2213]
    ])

    # Observer dynamics
    yh = np.dot(Ch, xh)
    xhp = np.dot(Ah, xh) + np.dot(Bh, uh) + np.dot(G, (dy - yh))

    # Augment the real and estimated states
    Xp = np.concatenate((xp, xhp))

    return Xp


# Define initial conditions and time span
X0 = np.zeros(19)  # Initial state vector [x, xh]
t_span = np.linspace(0, 20, 1000)  # Time span for integration

# Perform integration using odeint
X = odeint(train_model1, X0, t_span)

# Print or plot results as desired
# Example: Print the final state
final_state = X[-1]
print("Final state vector:")
print(final_state)
