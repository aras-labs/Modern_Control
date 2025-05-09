clear all

% Define the system matrices
A = [0    0   0   0   0    1      0      0   0   0;
     0    0   0   0   0    1     -1      0   0   0;
     0    0   0   0   0    0      1     -1   0   0;
     0    0   0   0   0    0      0      1  -1   0;
     0    0   0   0   0    0      0      0   1  -1;
     0 -12.5  0   0   0  -0.75   0.75    0   0   0;
     0  62.5 -62.5 0  0   3.75  -7.5  3.75   0   0;
     0  0 62.5 -62.5  0    0  3.75  -7.5  3.75   0; 
     0  0  0 62.5 -62.5    0     0  3.75  -7.5  3.75;
     0    0   0   0  62.5  0     0    0   3.75 -3.75];

b1 = [0;  0;  0;  0;  0; 0.005;   0;  0;  0;  0];     
b2 = [0;  0;  0;  0;  0; 250;  0;  0;  0;  -1250];   

C = [1   0   0   0   0   0   0   0   0   0];
D = 0;

u = 750;  
b = b1*u + b2;

% Create the state-space model
train_model = ss(A, b, C, D);  

% Time vector for simulation
t = 0:0.001:7;

% Initial state
x0 = [0; 0; 0; 0; 0; 0; 0; 0; 0; 0];

% Step response
[y, t, x] = step(train_model, t);

% Plotting the step response
figure(1);
plot(t, x(:,2), 'k', t, x(:,5), 'k-.'); grid on;
set(findall(figure(1), 'type', 'line'), 'linewidth', 2);
xlabel('Time (sec)');
ylabel('State variables');
legend('x_2', 'x_5');

% Define the new input signal
u = 0.1 * (sin(5*t) + sin(9*t) + sin(13*t) + sin(17*t) + sin(21*t));

% Simulate the response to the new input signal
[y, t, x] = lsim(train_model, u, t);

% Plotting the lsim response
figure(2);
plot(t, x(:,1), 'k', t, x(:,2), 'k-.'); grid on;
set(findall(figure(2), 'type', 'line'), 'linewidth', 2);
xlabel('Time (sec)');
ylabel('State variables');
legend('x_1', 'x_2');
