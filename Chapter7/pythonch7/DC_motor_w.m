%
%   Model of DC Motor for ode
%   Copyright Hamid D. Taghirad 2013
%
function xp=DC_motor_w(t,x)
%   State variable x=[\theta; \omega; i; Tl]
A=[0 1 0 0; 0 0 4.438 -7.396; 0 -12 -24  0; 0 0 0 -1];
B=[0 0; 0 -7.396; 20 0; 0 0];
k =[3.0000    0.8796    0.1529   -1.8190];
theta_d=0;          % Desired angular position
Tl=0.01;            % step disturbance
v1=2.255*Tl-k(1)*(x(1)-theta_d)-k(2)*x(2)-k(3)*x(3);
v2=2.255*Tl-k*x; 
u=[v1;Tl];
xp=A*x+B*u;
end


 