import numpy as np
import control as ctrl
import matplotlib.pyplot as plt

A = np.array([[0, 1, 0],
              [0, 0, 4.438],
              [0, -12, -24]])

b1 = np.array([[0],
               [0],
               [20]])

b2 = np.array([[0],
               [-7.396],
               [0]])

B = np.hstack((b1, b2))

C = np.array([[1, 0, 0],
              [0, 1, 0]])

# D = np.array([[0, 0, 0],
            #   [0, 0, 0]])
D = np.zeros((2, 1))
# Create state-space system
DC_motor = ctrl.ss(A, b1, C, D)

# Simulation
t = np.arange(0, 4, 0.01)
t, yout = ctrl.step_response(DC_motor, T=t)


# t = np.arange(0, 4, 0.01)  # Create the time array
# N = np.size(t)  # Get the number of elements in the array t
# # Or equivalently
# N = len(t)  # Get the number of elements in the array t



# Assuming t is already defined
N = len(t)
u = np.zeros((2, N))  # Assuming u has 2 rows (inputs) and N columns (time points)

for i in range(N):
    if t[i] < 2:
        u[:, i] = 3  # Set all elements in column i to 3
    else:
        u[:, i] = -3  # Set all elements in column i to -3





# Generate a square wave signal
# t = np.arange(0, 4, 0.01)  # Time vector from 0 to 4 with 0.01 step
u = -6 * np.sign(np.sin(2 * np.pi * 0.25 * t)) + 3  # Square wave with period 4 seconds, scaled and offset

# Simulate the response of the system
# _, y, _ = ctrl.forced_response(DC_motor, T=t, U=u)
# y contains the system's output, t contains the time vector, and x contains the states of the system
response = ctrl.forced_response(DC_motor, T=t, U=u)

# Inspect the response
print(response)


# print("Time array:")
# print(t)
# print("\nOutput array:")
# print(yout)



# plt.plot(t, response.states[2], 'k', label=r'$\theta$')
# plt.plot(t, response.states[1], 'k-.', label=r'$\omega$')
# plt.plot(t, response.states[0], 'k:', label='i')
# plt.xlabel('Time (sec)')
# plt.ylabel('State variables')
# plt.grid(True)
# plt.legend()
# plt.show()

plt.plot(t, -response.states[2], 'k', label='i')
plt.plot(t, -response.states[1], 'k-.', label=r'$\omega$')
plt.plot(t, -response.states[0], 'k:', label=r'$\theta$')
plt.xlabel('Time (sec)')
plt.ylabel('State variables')
plt.grid(True)
plt.legend()
plt.show()
#############################################
# no need to use the DCmotor_transfun function


