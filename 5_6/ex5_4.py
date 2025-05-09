import numpy as np
import scipy.signal as signal

# Define numerator and denominator arrays for transfer functions
num = [[1, 2], [-1, 1]]
den = [[1, 1], [1, 2], [1, 1], [1, 3]]

# Create transfer function sys
sys = signal.TransferFunction(num, den)

# Display sys as a transfer function
print("Transfer function (sys):")
print(sys)

# Convert sys to state-space form and compute minimal realization
sys2 = signal.minreal(signal.ss(sys))

print("\nMinimal realization (sys2):")
print(sys2)

# Define symbolic variable 's'
s = signal.TransferFunction([1, 0], [1])

# Define and simplify symbolic system mysys
mysys = [[1/(s + 1), 2/(s + 2)],
         [-1/(s + 1), 1/(s + 3)]]
myss = signal.minreal(signal.ss(mysys))

print("\nSymbolic system (mysys):")
print(mysys)
print("\nMinimal realization (myss):")
print(myss)

# Clear command window (not necessary in Python)

# Define symbolic variable 's'
s = signal.TransferFunction([1, 0], [1])

# Define transfer functions G11, G12, G21, G22
G11 = 1 / (s + 1)
G12 = 2 / (s + 2)
G21 = -1 / (s + 1)
G22 = 1 / (s + 3)

# Define interconnection strings
systemnames = 'G11 G12 G21 G22'
inputvar = '[u{2}]'
input_to_G11 = '[u(1)]'
input_to_G12 = '[u(2)]'
input_to_G21 = '[u(1)]'
input_to_G22 = '[u(2)]'
outputvar = '[G11+G12; G21+G22]'

# Interconnect systems
sysic = signal.InterconnectedSystem([G11, G12, G21, G22],
                                    connections=[input_to_G11, input_to_G12,
                                                 input_to_G21, input_to_G22],
                                    inplist=inputvar,
                                    outlist=outputvar)

# Display interconnected system
print("\nInterconnected system (sysic):")
print(sysic)

# Set input and output names
sysic.InputName = ['u1', 'u2']
sysic.OutputName = ['y1', 'y2']

# Convert interconnected system to state-space and compute minimal realization
G = signal.minreal(signal.ss(sysic))

print("\nMinimal realization of interconnected system (G):")
print(G)
