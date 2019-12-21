# python调用octave
### 介绍
用octave代替matlab，基于oct2py，实现python执行m文件，可以在python脚本中直接调用m文件中函数并取得返回值，其中形参和返回值的类型都会进行自动转化，无需手动调整；形参支持python基础数据类型以及numpy数据类型。只要在octave中配置相应的工具库，在python中也能够进行使用，例如regression等。

octave语法与matlab高度一致，也可以在win和macos运行，并且开源免费。
### 运行环境
os: Ubuntu 18.04

python: python 3.6.8

octave: GNU Octave, version 4.2.2
### 项目目录
```
.
├── document
│   └── py_call_octave.md
├── static_file
│   ├── add.m
│   ├── call.m
│   ├── call_regression.m
│   ├── min_max.m
│   └── regression.m
├── timeline
│   └── use_octave.py
```
### m文件
min_max.m
```matlab
function [a,b] = min_max(m,n)
    temp = m+n;
    a = max(max(temp));
    b = min(min(temp));
```
call.m
```matlab
M1 = rand(4,4);
M2 = rand(4,4);
[a,b] = min_max(M1,M2)
```
regression.m
```matlab
function [yb,k] = regression(x,Y)
  x=x';
  Y=Y';
  X=[ones(length(x),1) x];
  [b,bint,r,rint,stats]=regress(Y,X);
  Z=b(1)+b(2)*(140:165);
  yb=b(1);
  k=b(2);
```
call_regression.m
```matlab
x = [143 145 146 147 149 150 153 154 155 156 157 158 159 160 162 164];
Y = [88 85 88 91 92 93 93 95 96 98 97 96 98 99 100 102];
[yb,k] = regression(x,Y)
```

### python脚本调用m文件
注意函数有多个返回值的时候要添加关键字参数```nout```

use_octave.py
```python
from oct2py import octave

# 添加文件路径
octave.addpath('../static_file')
# 调用octave函数，多个返回值需要添加nout参数
print('通过函数名调用m文件中的函数')
a, b = octave.min_max([[1, 2], [3, 4]], [[1, 2], [3, 4]], nout=2)
print(f'a={a}, b={b}')
print('直接执行脚本')
octave.eval('call')
print('-------------------------------')
print('regression工具包')
octave.eval('pkg load statistics')
x = [143, 145, 146, 147, 149, 150, 153, 154, 155, 156, 157, 158, 159, 160, 162, 164]
Y = [88, 85, 88, 91, 92, 93, 93, 95, 96, 98, 97, 96, 98, 99, 100, 102]
yb, k = octave.regression(x, Y, nout=2)
print(f'yb={yb}, k={k}')
print('执行脚本call_regression')
octave.eval('call_regression')
octave.close()
```
执行结果
```
通过函数名调用m文件中的函数
a=8.0, b=2.0
直接执行脚本
a =  1.8594
b =  0.18514
-------------------------------
regression工具包
yb=-16.07298072980751, k=0.719352193521936
执行脚本call_regression
yb = -16.073
k =  0.71935
```

>https://oct2py.readthedocs.io/en/latest/index.html