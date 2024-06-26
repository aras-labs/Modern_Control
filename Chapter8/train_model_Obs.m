%
%   Model of the train
%   Copyright Hamid D. Taghirad 2013
%
function Xp=train_model1(t,X),
global Par
%   Model of The Real System
%   State variable x=[x1 x2 x3 x4 x5 v1 v2 v3 v4 v5];
x=X(1:10);
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
b1=[0; 0;  0;  0;  0;  0.005;  0;  0;  0;  0];      % Force input
b2=[0; 0;  0;  0;  0;    250;  0;  0;  0; -1250];   % constant input
if t < 10,
    u=Par.F;       % Constant Force
    uh=0.5*u;
else 
    u=0;
    uh=u;
end
xp=A*x+b1*u+b2;
C=[0 1 0 0 0 0 0 0 0 0;
   0 0 0 0 0 1 0 0 0 0];
y=C*x; dy=[y(1)-20;y(2)]
%   Model of The observer
xh=X(11:19);
Ah=[0     0   0   0   1     -1    0    0     0
   0      0   0   0   0      1   -1    0     0
   0      0   0   0   0      0    1   -1     0
   0      0   0   0   0      0    0    1    -1
  -12.5   0   0   0 -0.75  0.75   0    0     0
   62.5 -62.5 0   0  3.75  -7.5  3.75  0     0
   0  62.5 -62.5  0   0    3.75  -7.5  3.75  0
   0   0  62.5 -62.5  0      0   3.75  -7.5  3.75    
   0   0   0    62.5  0      0     0   3.75 -3.75 
   ];
Bh=[0; 0;  0;  0;  0.005;  0;  0;  0;  0];
Ch=[1 0 0 0 0 0 0 0 0;
    0 0 0 0 1 0 0 0 0];
yh=Ch*xh;
G =[
   10.5008    0.0472
    4.0624    0.0100
    1.2245    0.0004
    0.3222   -0.0007
  118.1098    1.1441
   60.1867    0.5240
   16.7939    0.3003
   -0.0227    0.2370
   -4.2587    0.2213
    ];
xhp=Ah*xh+Bh*uh+G*(dy-yh);
%   Augment the real and estimated states
Xp=[xp;xhp];
end


 