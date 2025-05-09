# Import necessary libraries
import numpy as np

# Define the model of the tank
def tank_model(x, t):
    A = 1.0
    C = 2.0
    F_in = 0.0  # No disturbance input
    u = 0.1     # Constant opening for valve
    
    x = np.maximum(x, 0)  # Ensure tank level is non-negative
    
    xp = (F_in - C * u * np.sqrt(x)) / A
    
    return xp