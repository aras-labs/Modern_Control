%
%   Model of the train
%   Copyright Hamid D. Taghirad 2013
%
function xp=train_model1(t,x)
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
b1=[0;  0;  0;  0;  0.005;  0;  0;  0;  0;  0];      % Force input
b2=[0;  0;  0;  0;    250;  0;  0;  0;  0; -1250];   % constant input
u=750;  % Constant input
xp=A*x+b1*u+b2;
end


 