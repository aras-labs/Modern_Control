%
%   Simulation of closed-loop Inverted Pendulum
%   Copyright Hamid D. Taghirad 2013
%
clear all
clf, echo on
tspan=[0 4];
x0=[0; 0; 0.26; 0];

[t,x] = ode45(@inverted_pendulum_k1,tspan, x0, ...
    odeset('OutputFcn','odeplot','MaxStep',1e-2)); 

plot(t,x(:,1),'k',t,x(:,3)*180/pi,'-.k'),grid
xlabel('Time (sec)')
ylabel('State Variables')
legend('x (m)', '\theta (degrees)')
set(findall(figure(1),'type','line'),'linewidth',2)
