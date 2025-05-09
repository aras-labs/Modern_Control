%
%   Model of Inverted Pendulum
%   Copyright Hamid D. Taghirad 2014
%
function xp=inverted_pendulum_k2(t,x);
%   State variable x=[x; v; \theta; \omega]
g=9.8,l=1,m=1;M=1;
d1=M+m*(1-cos(x(3))^2);
d2=l*d1;
k =[-40.0000  -37.3693 -190.6669  -54.7283];

F=-k*x;   % State feedback

xp=[
    x(2);
    (F+m*l*x(4)^2*sin(x(3))-m*g*sin(x(3))*cos(x(3)))/d1;
    x(4);
    (-F*cos(x(3))-m*l*x(4)^2*sin(x(3))*cos(x(3))+...
        (M+m)*g*sin(x(3)))/d2;
    ];
end


 