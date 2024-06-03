import control as ctrl

# Define numerator and denominator matrices
num = [[[1], [2]], [[-1], [1]]]
den = [[[1, 1], [1, 2]], [[1, 1], [1, 3]]]

# Create transfer function system
sys = ctrl.TransferFunction(num, den)
print('sys =')
print(sys)

# Convert to state-space representation and minimal realization
sys2 = ctrl.minreal(ctrl.ss(sys))
print('\nsys2 =')
print(sys2)

# Define s in the Laplace domain
s = ctrl.TransferFunction([1, 0], [1])

# Define the system matrix
mysys = ctrl.TransferFunction([[1/(s + 1), 2/(s + 2)], [-1/(s + 1), 1/(s + 3)]])
print('\nmysys =')
print(mysys)

# Convert to state-space representation and minimal realization
myss = ctrl.minreal(ctrl.ss(mysys))
print('\nmyss =')
print(myss)

# Define the zpk system
s = ctrl.TransferFunction([1, 0], [1])

# Define transfer functions
G11 = 1/(s + 1)
G12 = 2/(s + 2)
G21 = -1/(s + 1)
G22 = 1/(s + 3)

# Define interconnection structure
systemnames = ['G11', 'G12', 'G21', 'G22']
inputvar = '[u[2]]'
input_to_G11 = '[u[1]]'
input_to_G12 = '[u[2]]'
input_to_G21 = '[u[1]]'
input_to_G22 = '[u[2]]'
outputvar = '[G11+G12; G21+G22]'

# Interconnection
sysic = ctrl.InterconnectedSystem(
    (G11, G12, G21, G22), inputvar, input_to_G11, input_to_G12, input_to_G21, input_to_G22, outputvar
)

# Set input and output names
sysic.InputName = ['u1', 'u2']
sysic.OutputName = ['y1', 'y2']

# Convert to state-space representation and minimal realization
G = ctrl.minreal(ctrl.ss(sysic))
print('\nans =')
print(G)
