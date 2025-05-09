import numpy as np

def robot_model(t, x):
    # Parameters
    g = 9.81
    l1 = 1
    l2 = 0.5
    m1 = 2
    m2 = 1
    I1 = 1e-2
    I2 = 5e-3
    D = 2
    
    # Mass matrix M
    M = np.array([[m1*(l1/2)**2 + m2*(l1**2 + (l2/2)**2) + m2*l1*l2*np.cos(x[1]) + I1 + I2,
                   m2*(l2/2)**2 + 0.5*m2*l1*l2*np.cos(x[1]) + I2],
                  [m2*(l2/2)**2 + 0.5*m2*l1*l2*np.cos(x[1]) + I2,
                   m2*(l2/2)**2 + I2]])
    
    # Coriolis and centrifugal force vector V
    V = np.array([-m2*l1*l2*np.sin(x[1])*x[2]*x[3] - 0.5*m2*l1*l2*np.sin(x[1])*x[3]**2,
                  -0.5*m2*l1*l2*np.sin(x[1])*x[2]*x[3]])
    
    # Gravitational force vector G
    G = np.array([(m1*l1/2 + m2*l1)*g*np.cos(x[0]) + m2*g*l2/2*np.cos(x[0] + x[1]),
                  m2*g*l2/2*np.cos(x[0] + x[1])])
    
    # Input vector Q
    Q = np.array([0, 0])  # No input
    Q -= D * np.array([x[2], x[3]])
    
    # Compute acceleration
    xy = np.linalg.pinv(M).dot(Q - V - G)
    
    # Return time derivatives of state variables
    return np.array([x[2], x[3], xy[0], xy[1]])
