%
%   Model of DC Motor for ode
%   Copyright Hamid D. Taghirad 2013
%
function xp=DC_motor(t,x)
%   State variable x=[\theta; \omega; i]
A=[0 1 0; 0 0 4.438; 0 -12 -24];
B=[0 0; 0 -7.396; 20 0];
theta_d=0;          % Desired angular position
Tl=0.01;            % step disturbance
v=2.255*Tl -3.0*(x(1)-theta_d) -0.879*x(2) -0.1529*x(3);
u=[v;Tl];
xp=A*x+B*u;
end


 