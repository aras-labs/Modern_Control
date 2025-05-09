import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

def tank_model(t, x):
    # State variable x = [l]: Tank level
    A = 1.0
    C = 2.0
    F_in = 0  # No disturbance input
    u = 0.1  # Constant opening for valve

    xp = 1 / A * (F_in - C * u * np.sqrt(x[0]))
    return [xp]

# Initial condition: tank level
x0 = [100.0]  # Initial level of the tank

# Time span for the simulation
t_span = (0, 100)
t_eval = np.linspace(*t_span, 1000)  # Generate 1000 time points within the span

# Solve the differential equation
sol = solve_ivp(tank_model, t_span, x0, t_eval=t_eval, max_step=0.1)

# Plotting the results
plt.figure(figsize=(10, 6))
plt.plot(sol.t, sol.y[0], 'k')
plt.grid(True)
plt.xlabel('Time (sec)')
plt.ylabel('Tank Level (m)')
plt.title('Simulation of Tank Level')
plt.show()
