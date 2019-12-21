# octave 对于matlab工具箱以及第三方工具箱的支持
python调用octave的方式与matlab engine类似。相较而言最大的优势在于matlab engine调用函数的时候形参以及返回值必须要转化成matlab对象，而octave不用。
### octave安装工具箱
在octave环境中安装了相应的工具箱后，python中即可使用。
>https://octave.sourceforge.io/

安装工具箱需要先进入ocatave命令行

Octave Forge自带了许多工具箱，可以通过如下方式安装
```
pkg install -forge package_name
```

此外，第三方工具箱有多种安装方式（本地or网络）
```
pkg install image-1.0.0.tar.gz
pkg install 'http://somewebsite.org/image-1.0.0.tar.gz'
```

使用工具箱
```
pkg load package_name
```
octave同样支持卸载工具箱以及将本地文件打包为工具箱
### 使用matlab第三方工具箱
>https://octave.org/doc/interpreter/Installing-and-Removing-Packages.html

matlab安装文件.mltbx不能直接在octave上安装，但若是能够获得第三方工具库的源代码m文件，则octave同样可以执行，并生成自己的工具箱安装文件。

具体过程：新建一个文件夹，在文件夹中新建COPYING，DESCRIPTION文件以及inst文件夹，将所有m文件放在inst文件夹中，再将整个文件夹打包，使用```pkg build builddir image-1.0.0.tar.gz …```生成安装包。再使用```pkg install image-1.0.0.tar.gz```安装。