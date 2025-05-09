# import numpy as np
# import matplotlib.pyplot as plt
# from scipy.integrate import odeint

# # Define global parameters
# class Par:
#     F = 1000

# # Define the model function
# def train_model1(X, t):
#     global Par
#     # Model parameters
#     A = np.array([
#         [0,    0,    0,    0,    0,    1,    0,    0,    0,    0],
#         [0,    0,    0,    0,    0,    1,   -1,    0,    0,    0],
#         [0,    0,    0,    0,    0,    0,    1,   -1,    0,    0],
#         [0,    0,    0,    0,    0,    0,    0,    1,   -1,    0],
#         [0,    0,    0,    0,    0,    0,    0,    0,    1,   -1],
#         [0, -12.5,  0,    0,    0,   -0.75, 0.75,  0,    0,    0],
#         [0,  62.5, -62.5, 0,    0,    3.75, -7.5,  3.75, 0,    0],
#         [0,    0,   62.5, -62.5, 0,    0,    3.75, -7.5,  3.75, 0],
#         [0,    0,    0,   62.5, -62.5, 0,    0,    3.75, -7.5,  3.75],
#         [0,    0,    0,    0,   62.5, 0,    0,    0,    3.75, -3.75]
#     ])
#     b1 = np.array([0, 0,  0,  0,  0,  0.005,  0,  0,  0,  0])      # Force input
#     b2 = np.array([0, 0,  0,  0,  0,  250,    0,  0,  0, -1250])   # constant input
    
#     if t < 10:
#         u = Par.F  # Constant Force
#         uh = 0.5 * u
#     else:
#         u = 0
#         uh = u
    
#     xp = np.dot(A, X[:10]) + b1 * u + b2
    
#     C = np.array([
#         [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 1, 0, 0, 0, 0]
#     ])
    
#     y = np.dot(C, X[:10])
#     dy = np.array([y[0] - 20, y[1]])
    
#     # Observer model
#     xh = X[10:19]
#     Ah = np.array([
#         [0,    0,    0,    0,    1,   -1,    0,    0,    0],
#         [0,    0,    0,    0,    0,    1,   -1,    0,    0],
#         [0,    0,    0,    0,    0,    0,    1,   -1,    0],
#         [0,    0,    0,    0,    0,    0,    0,    1,   -1],
#         [-12.5, 0,    0,    0,   -0.75, 0.75,  0,    0,    0],
#         [62.5, -62.5, 0,    0,    3.75, -7.5,  3.75, 0,    0],
#         [0,   62.5, -62.5, 0,    0,    3.75, -7.5,  3.75, 0],
#         [0,    0,   62.5, -62.5, 0,    0,    3.75, -7.5,  3.75],
#         [0,    0,    0,   62.5, -62.5, 0,    0,    0,    3.75]
#     ])
#     Bh = np.array([0, 0,  0,  0,  0.005,  0,  0,  0,  0])
    
#     Ch = np.array([
#         [1, 0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 1, 0, 0, 0, 0]
#     ])
    
#     yh = np.dot(Ch, xh)
#     G = np.array([
#         [10.5008,  0.0472],
#         [ 4.0624,  0.0100],
#         [ 1.2245,  0.0004],
#         [ 0.3222, -0.0007],
#         [118.1098,  1.1441],
#         [60.1867,  0.5240],
#         [16.7939,  0.3003],
#         [-0.0227,  0.2370],
#         [-4.2587,  0.2213]
#     ])
    
#     xhp = np.dot(Ah, xh) + Bh * uh + np.dot(G, (dy - yh))
    
#     Xp = np.concatenate((xp, xhp))
    
#     return Xp

# # Initial conditions and time span
# x0 = np.array([0, 20, 20, 20, 20, 0, 0, 0, 0, 0,
#                0, 0, 0, 0, 0, 0, 0, 0, 0])
# tspan = np.linspace(0, 20, 100)  # 100 points from 0 to 20 seconds

# # Solve the ODE
# sol = odeint(train_model1, x0, tspan)

# # Extract results for plotting
# x = sol[:, :10]
# xh = sol[:, 10:19]

# # Plotting
# plt.figure(figsize=(10, 8))

# plt.subplot(211)
# plt.plot(tspan, x[:, 1] - 20, 'k', label='Real x_2')
# plt.plot(tspan, xh[:, 0], 'k-.', label='Est x_2')
# plt.grid(True)
# plt.xlabel('Time (sec)')
# plt.ylabel('State variables')
# plt.legend()

# plt.subplot(212)
# plt.plot(tspan, x[:, 5], 'k', label='Real v_1')
# plt.plot(tspan, xh[:, 4], 'k-.', label='Est v_1')
# plt.grid(True)
# plt.xlabel('Time (sec)')
# plt.ylabel('State variables')
# plt.legend()

# plt.tight_layout()
# plt.show()
###########################

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Define global parameters
class Par:
    F = 1000

# Define the model function
def train_model1(X, t):
    global Par
    # Model parameters
    A = np.array([
        [0,    0,    0,    0,    0,    1,    0,    0,    0,    0],
        [0,    0,    0,    0,    0,    1,   -1,    0,    0,    0],
        [0,    0,    0,    0,    0,    0,    1,   -1,    0,    0],
        [0,    0,    0,    0,    0,    0,    0,    1,   -1,    0],
        [0,    0,    0,    0,    0,    0,    0,    0,    1,   -1],
        [0, -12.5,  0,    0,    0,   -0.75, 0.75,  0,    0,    0],
        [0,  62.5, -62.5, 0,    0,    3.75, -7.5,  3.75, 0,    0],
        [0,    0,   62.5, -62.5, 0,    0,    3.75, -7.5,  3.75, 0],
        [0,    0,    0,   62.5, -62.5, 0,    0,    3.75, -7.5,  3.75],
        [0,    0,    0,    0,   62.5, 0,    0,    0,    3.75, -3.75]
    ])
    b1 = np.array([0, 0,  0,  0,  0,  0.005,  0,  0,  0,  0])      # Force input
    b2 = np.array([0, 0,  0,  0,  0,  250,    0,  0,  0, -1250])   # constant input
    
    if t < 10:
        u = Par.F  # Constant Force
        uh = 0.5 * u
    else:
        u = 0
        uh = u
    
    xp = np.dot(A, X[:10]) + b1 * u + b2
    
    C = np.array([
        [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 0, 0]
    ])
    
    y = np.dot(C, X[:10])
    dy = np.array([y[0] - 20, y[1]])
    
    # Observer model
    xh = X[10:19]
    Ah = np.array([
        [0,    0,    0,    0,    1,   -1,    0,    0,    0],
        [0,    0,    0,    0,    0,    1,   -1,    0,    0],
        [0,    0,    0,    0,    0,    0,    1,   -1,    0],
        [0,    0,    0,    0,    0,    0,    0,    1,   -1],
        [-12.5, 0,    0,    0,   -0.75, 0.75,  0,    0,    0],
        [62.5, -62.5, 0,    0,    3.75, -7.5,  3.75, 0,    0],
        [0,   62.5, -62.5, 0,    0,    3.75, -7.5,  3.75, 0],
        [0,    0,   62.5, -62.5, 0,    0,    3.75, -7.5,  3.75],
        [0,    0,    0,   62.5, -62.5, 0,    0,    0,    3.75]
    ])
    Bh = np.array([0, 0,  0,  0,  0.005,  0,  0,  0,  0])
    
    Ch = np.array([
        [1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0]
    ])
    
    yh = np.dot(Ch, xh)
    G = np.array([
        [10.5008,  0.0472],
        [ 4.0624,  0.0100],
        [ 1.2245,  0.0004],
        [ 0.3222, -0.0007],
        [118.1098,  1.1441],
        [60.1867,  0.5240],
        [16.7939,  0.3003],
        [-0.0227,  0.2370],
        [-4.2587,  0.2213]
    ])
    
    xhp = np.dot(Ah, xh) + Bh * uh + np.dot(G, (dy - yh))
    
    Xp = np.concatenate((xp, xhp))
    
    return Xp

# Initial conditions and time span
x0 = np.array([0, 20, 20, 20, 20, 0, 0, 0, 0, 0,
               0, 0, 0, 0, 0, 0, 0, 0, 0])
tspan = np.linspace(0, 20, 100)  # 100 points from 0 to 20 seconds

# Solve the ODE
sol = odeint(train_model1, x0, tspan)

# Extract results for plotting
x = sol[:, :10]
xh = sol[:, 10:19]

# Plotting
plt.figure(figsize=(10, 8))

plt.subplot(211)
plt.plot(tspan, x[:, 1] - 20, 'k', label='Real x_2')
plt.plot(tspan, xh[:, 0], 'k-.', label='Est x_2')
plt.grid(True)
plt.xlabel('Time (sec)')
plt.ylabel('State variables')
plt.legend()

plt.subplot(212)
plt.plot(tspan, x[:, 5], 'k', label='Real v_1')
plt.plot(tspan, xh[:, 4], 'k-.', label='Est v_1')
plt.grid(True)
plt.xlabel('Time (sec)')
plt.ylabel('State variables')
plt.legend()

plt.tight_layout()
plt.show()
