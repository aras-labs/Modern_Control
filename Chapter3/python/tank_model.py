import numpy as np

def tank_model(t, x):
    """
    Model of the tank.

    Parameters:
    t : float
        Time variable.
    x : float
        State variable representing the tank level.

    Returns:
    xp : float
        Derivative of the tank level with respect to time.
    """
    # Parameters
    A = 1.0  # Cross-sectional area of the tank
    C = 2.0  # Coefficient related to the valve and tank properties
    F_in = 0.0  # No disturbance input
    u = 0.1  # Constant opening for valve

    # Tank model differential equation
    xp = 1/A * (F_in - C * u * np.sqrt(x))

    return xp
########################################
def tank_model(x, t):
    # Parameters
    k1 = 0.1
    k2 = 0.2
    
    # System of differential equations
    dxdt = -k1*x + k2
    
    return dxdt