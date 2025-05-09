# import numpy as np
# import matplotlib.pyplot as plt

# # Clear all variables (not usually necessary in Python)
# # globals().clear()

# # Clear the current figure
# plt.clf()

# # Define the time span
# tspan = [0, 3]

# # Define the initial conditions
# x0 = np.array([0, 0, 0])

# # If you want to mimic echoing of commands, use print statements (optional)
# print("tspan =", tspan)
# print("x0 =", x0)


# from scipy.integrate import solve_ivp
# import numpy as np
# import matplotlib.pyplot as plt

# # Define the DC_motor function (placeholder function; needs to be defined)
# def DC_motor(t, x):
#     # Placeholder for the differential equations
#     # Replace this with the actual equations
#     dxdt = [0, 0, 0]
#     return dxdt

# # Define the time span and initial conditions
# tspan = [0, 3]
# x0 = np.array([0, 0, 0])

# # Define options for the solver
# options = {
#     'max_step': 1e-2
# }

# # Solve the ODE
# solution = solve_ivp(DC_motor, tspan, x0, **options)

# # Extract the results
# t = solution.t
# x = solution.y.T

# # Plotting function (to mimic odeplot)
# def odeplot(t, x):
#     plt.plot(t, x)
#     plt.xlabel('Time')
#     plt.ylabel('State Variables')
#     plt.show()

# # Call the plotting function
# odeplot(t, x)


# import numpy as np
# import matplotlib.pyplot as plt

# # Assume t and x are already defined from the previous solve_ivp result
# # Example values for demonstration:
# t = np.linspace(0, 3, 100)
# x = np.zeros((100, 3))  # Replace this with the actual solution data
# x[:, 0] = np.sin(t)  # Example data for plotting

# # Convert angular displacement from radians to degrees
# angular_displacement = x[:, 0] * 180 / np.pi

# # Plot the data
# plt.plot(t, angular_displacement, 'k')
# plt.grid(True)
# plt.xlabel('Time (sec)')
# plt.ylabel('Angular displacement θ (degrees)')

# # Uncomment the legend line if you want to include a legend
# # plt.legend(['θ (degrees)'])

# # Set the line width for all lines in the figure
# lines = plt.gca().get_lines()
# for line in lines:
#     line.set_linewidth(2)

# # Display the plot
# plt.show()
#############################

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Define the DC_motor function (replace this with your actual function)
def DC_motor(t, x):
    # Example placeholder for the differential equations
    # Ensure this matches the MATLAB function exactly
    dxdt = [x[1], -0.1 * x[0], 0.1]  # Adjust as per your actual equations
    return dxdt

# Define the time span and initial conditions
tspan = [0, 3]
x0 = [0, 0, 0]

# Define options for the solver
options = {'max_step': 1e-2}

# Solve the ODE
solution = solve_ivp(DC_motor, tspan, x0, method='RK45', max_step=options['max_step'])

# Extract the results
t = solution.t
x = solution.y.T

# Plot the data
plt.figure()
plt.plot(t, x[:, 0] * 180 / np.pi, 'k')
plt.grid(True)
plt.xlabel('Time (sec)')
plt.ylabel('Angular displacement θ (degrees)')

# Uncomment the legend line if you want to include a legend
# plt.legend(['θ (degrees)'])

# Set the line width for all lines in the figure
lines = plt.gca().get_lines()
for line in lines:
    line.set_linewidth(2)

# Display the plot
plt.show()

