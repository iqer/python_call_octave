# -*- coding: utf-8 -*-
import sys

from oct2py import octave

octave.addpath(r'../static_file/min_max.m')
# octave.addpath('../static_file')
# octave.temp_dir = '../static_file'
# octave.addpath(u'/home/cqh/Documents/PythonCallOctave/static_file')

print('Demo1\nCall the function in .m file by using the name of function')

# octave can use python built-in data-structure as arguments but matlab can't
# octave object can call function in the file in path
# by the way,when calling function by dot operator, 'nout' tell python the number n of output arguments
a, b = octave.min_max([[1, 2], [3, 4]], [[1, 2], [3, 4]], nout=2)

PY2 = sys.version_info[0] == 2
if PY2:
    print ('a={}, b={}'.format(a, b))
else:
    eval("print(f'a={a}, b={b}')")
# print('\n-------------------------------\n')
print('\nDemo2.\nDirect Eval octave method by file name\n')

octave.eval('call')
# print('\n-------------------------------\n')
print('\nDemo2.\nDirect Call octave method by its file name\n')

print('\nDemo3.\nEval octave regression工具包')
# pkg is the package manager of octave like apt in ubuntu
octave.eval('pkg load statistics')
x = [143, 145, 146, 147, 149, 150, 153, 154, 155, 156, 157, 158, 159, 160, 162, 164]
Y = [88, 85, 88, 91, 92, 93, 93, 95, 96, 98, 97, 96, 98, 99, 100, 102]
yb, k = octave.regression(x, Y, nout=2)
if PY2:
    print ('yb={}, k={}'.format(yb, k))
else:
    eval("print(f'yb={yb}, k={k}')")

print('执行脚本call_regression')
octave.eval('call_regression')
octave.close()
