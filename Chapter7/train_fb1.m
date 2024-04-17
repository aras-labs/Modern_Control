%
%   Model of the train
%   Copyright Hamid D. Taghirad 2013
%
function xp=train_fb(t,x)
% x=
% [dx2   dx3 dx4 dx5 dv1    dv2  dv3  dv4   dv5   z];
A=[0      0   0   0   1     -1    0    0     0    0
   0      0   0   0   0      1   -1    0     0    0
   0      0   0   0   0      0    1   -1     0    0
   0      0   0   0   0      0    0    1    -1    0
  -12.5   0   0   0 -0.75  0.75   0    0     0    0
   62.5 -62.5 0   0  3.75  -7.5  3.75  0     0    0
   0  62.5 -62.5  0   0    3.75  -7.5  3.75  0    0
   0   0  62.5 -62.5  0      0   3.75  -7.5  3.75 0   
   0   0   0    62.5  0      0     0   3.75 -3.75 0
   0   0   0      0   0      0     0      0   0  -1/40
   ];
B=[0;  0;  0;  0;  0.005;  0;  0;  0;  0;  0];     % Force input
b1=[0;  0;  0;  0;  0.005;  0;  0;  0;  0;  0];     % Force input
b2=[0;  0;  0;  0;  250;  0;  0;  0;  0;  -1250];   % constant input
vd=25*(1-exp(-t/40));
k=[54.5333, 16.2848, -1.3027, -4.3607, 191.7414, ...
    -40.4841, -34.2067, -29.7070, -27.3437,  52.0886];
dx=[x(2)-20; x(3)-20; x(4)-20; x(5)-20]; 
dv=[x(6)-vd; x(7)-vd; x(8)-vd; x(9)-vd; x(10)-vd];
z=x(6)-vd;
X=[dx;dv;z];
u=k*X;
xp=A*x+b1*u+b2;
end


 