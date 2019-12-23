## Method to use 
OS:Ubuntu 18.04
/PythonCallOctave/bin/run.sh

## Q&A
```
1.Q:
octave:1> pkg install io-2.4.13.tar.gz
pkg: please install the Debian package "liboctave-dev" to get the mkoctfile command
error: called from
    __gripe_missing_component__ at line 53 column 3
    configure_make at line 40 column 7
    install at line 194 column 7
    pkg at line 394 column 9

A:sudo apt install liboctave-dev -y 
```