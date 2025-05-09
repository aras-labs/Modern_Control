%
%   Simulation of the train
%   Copyright Hamid D. Taghirad 2013
%
clear all
%   State variable x=[x1 x2 x3 x4 x5 v1 v2 v3 v4 v5];
A=[0    0   0   0   0    1      0      0   0   0
   0    0   0   0   0    1     -1      0   0   0
   0    0   0   0   0    0      1     -1   0   0
   0    0   0   0   0    0      0      1  -1   0
   0    0   0   0   0    0      0      0   1  -1
   0 -12.5  0   0   0  -0.75   0.75    0   0   0
   0  62.5 -62.5 0  0   3.75  -7.5  3.75   0   0
   0  0 62.5 -62.5  0    0  3.75  -7.5  3.75   0 
   0  0  0 62.5 -62.5    0     0  3.75  -7.5  3.75
   0    0   0   0  62.5  0     0    0   3.75 -3.75
   ];
b1=[0;  0;  0;  0;  0.005;  0;  0;  0;  0;  0];     % Force input
b2=[0;  0;  0;  0;  250;  0;  0;  0;  0;  -1250];   % constant input
B=[b1 b2];
C=[1   0   0   0   0   0   0   0   0   0];
D=0;
train_model=ss(A,b1,C,D);  % Note only Second input is used
t=0:0.01:7; N=max(size(t));
%
%   Initial response
%
x0=[20;20;20;20;20;0;0;0;0;0];
[y,t,x]=initial(train_model, x0, t);


plot(t,x(:,1),'k',t,x(:,5),'k-.'), grid
set(findall(figure(1),'type','line'),'linewidth',2)
xlabel('Time (sec)')
ylabel('State variables')
legend('x_1', 'x_5')

%
%    A Simple way to generate input u
%
u=0.1*(sin(5*t)+sin(9*t)+sin(13*t)+sin(17*t)+sin(21*t));
%
%    Simulate the system
%
[y,t,x]=lsim(train_model,u,t); % Changed 'active_suspension' to 'train_model'

%  Plot the result
% ---------------------------------------
figure; % Create a new figure
plot(t,x(:,1),'k',t,x(:,2),'k-.'), grid % Plot x1 and x2
set(findall(figure(2),'type','line'),'linewidth',2) % Increase line width
xlabel('Time (sec)')
ylabel('State variables')
legend('x_1', 'x_2')
