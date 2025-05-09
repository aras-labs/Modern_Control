import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Define the function train_model1 representing the system of differential equations
def train_model1(t, x):
    # Define the parameters and constants used in the system
    A = np.array([[0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])
    
    B = np.array([[0], [0], [0], [0], [0], [0], [0], [0], [0], [0]])

    # Define the differential equations (modify based on your actual equations)
    dxdt = A @ x + B.flatten()  # Ensure B is flattened to match the shape of x

    return dxdt

# Define the time span and initial conditions
t_span = [0, 10]
x0 = np.array([0, 20, 20, 20, 20, 0, 0, 0, 0, 0])

# Integrate the differential equations using solve_ivp
sol = solve_ivp(train_model1, t_span, x0, method='RK45', dense_output=True)

# Extract the solution time points and state variables
t = sol.t
x = sol.y

# Plotting the results
plt.figure(figsize=(10, 6))
plt.plot(t, x[1, :], 'k', label='x_2')
plt.plot(t, x[4, :], 'k-.', label='x_5')
plt.grid(True)
plt.xlabel('Time (sec)')
plt.ylabel('State variables')
plt.legend()
plt.show()
