# Import necessary libraries
import numpy as np

# Define the model of the inverted pendulum
def inverted_pendulum(x, t):
    g = 9.8
    l = 1.0
    m = 1.0
    M = 1.0
    
    d1 = M + m * (1 - np.cos(x[1])**2)
    d2 = l * d1
    
    F = 0  # No input
    
    xp = np.zeros(4)
    xp[0] = x[2]
    xp[1] = x[3]
    xp[2] = (F + m * l * x[3]**2 * np.sin(x[1]) - m * g * np.sin(x[1]) * np.cos(x[1])) / d1
    xp[3] = (-F * np.cos(x[1]) - m * l * x[3]**2 * np.sin(x[1]) * np.cos(x[1]) + (M + m) * g * np.sin(x[1])) / d2
    
    return xp
