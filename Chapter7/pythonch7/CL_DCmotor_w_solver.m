%
%   Simulation of closed-loop DC motor
%   Copyright Hamid D. Taghirad 2013
%
clf, echo on
tspan=[0 3];
x0=[0; 0; 0; 0.01];

[t,x] = ode45(@DC_motor_w,tspan, x0, ...
    odeset('OutputFcn','odeplot','MaxStep',1e-2)); 

plot(t,x(:,1)*180/pi,'k'),grid
xlabel('Time (sec)')
ylabel('Angular displacement (degrees)')
%legend('\theta (degrees)')
set(findall(figure(1),'type','line'),'linewidth',2)
