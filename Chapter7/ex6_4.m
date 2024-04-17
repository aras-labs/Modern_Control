%
%   Example 6-4 of Modern Book
%   Copyright Hamid D. Taghirad 2014
%
clear all
A=[0 1 0 0; 0 0 -9.8 0; 0 0 0 1; 0 0 19.6 0];
b=[0 ; 1; 0; -1];
C=ctrb(A,b);
a=[0 -19.6 0 0];
alpha=[12.86  63.065  149.38  157.0];
Psi=[1 a(1) a(2) a(3);
     0  1   a(1) a(2);
     0  0    1   a(1)
     0  0    0    1];
k=(alpha-a)*inv(C*Psi)