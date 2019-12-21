function [yb,k] = regression(x,Y)
x=x';
Y=Y';
X=[ones(length(x), 1) x];
[b, bint, r, rint, stats]=regress(Y,X);
Z=b(1)+b(2)*(140:165);
yb=b(1);
k=b(2);