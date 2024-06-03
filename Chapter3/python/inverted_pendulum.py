
def inverted_pendulum(x, t):
    # Parameters
    g = 9.8
    l = 1
    m = 1
    M = 1
    
    # Compute intermediate terms
    d1 = M + m * (1 - np.cos(x[1])**2)
    d2 = l * d1
    
    # Input force
    F = 0  # No input
    
    # Compute time derivatives of state variables
    xp = np.array([
        x[2],  # x'
        x[3],  # theta'
        (F + m * l * x[3]**2 * np.sin(x[1]) - m * g * np.sin(x[1]) * np.cos(x[1])) / d1,  # v'
        (-F * np.cos(x[1]) - m * l * x[3]**2 * np.sin(x[1]) * np.cos(x[1]) +
         (M + m) * g * np.sin(x[1])) / d2  # omega'
    ])
    
    return xp