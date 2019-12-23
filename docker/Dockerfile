FROM ubuntu

RUN cp /etc/apt/sources.list /etc/apt/sources.list.bak && \
echo 'deb http://mirrors.aliyun.com/ubuntu/ bionic main restricted universe multiverse'> /etc/apt/sources.list && \
echo 'deb http://mirrors.aliyun.com/ubuntu/ bionic-security main restricted universe multiverse'>> /etc/apt/sources.list && \
echo 'deb http://mirrors.aliyun.com/ubuntu/ bionic-updates main restricted universe multiverse'>> /etc/apt/sources.list && \
echo 'deb http://mirrors.aliyun.com/ubuntu/ bionic-proposed main restricted universe multiverse'>> /etc/apt/sources.list && \
echo 'deb http://mirrors.aliyun.com/ubuntu/ bionic-backports main restricted universe multiverse'>> /etc/apt/sources.list && \
echo 'deb-src http://mirrors.aliyun.com/ubuntu/ bionic main restricted universe multiverse'>> /etc/apt/sources.list && \
echo 'deb-src http://mirrors.aliyun.com/ubuntu/ bionic-security main restricted universe multiverse'>> /etc/apt/sources.list && \
echo 'deb-src http://mirrors.aliyun.com/ubuntu/ bionic-updates main restricted universe multiverse'>> /etc/apt/sources.list && \
echo 'deb-src http://mirrors.aliyun.com/ubuntu/ bionic-proposed main restricted universe multiverse'>> /etc/apt/sources.list && \
echo 'deb-src http://mirrors.aliyun.com/ubuntu/ bionic-backports main restricted universe multiverse'>> /etc/apt/sources.list

RUN apt-get update && \
apt-get upgrade -y

RUN apt-get install -y python3 && \
wget && \
python3-distutils

RUN wget -O /tmp/get-pip.py https://bootstrap.pypa.io/get-pip.py

RUN python3 /tmp/get-pip.py

RUN pip install --upgrade pip

RUN apt install -y octave

RUN pip install oct2py

COPY py_to_octave.tar.gz /

RUN tar xzf py_to_octave.tar.gz && \
mkdir -p /datayes/mercury && \
mv py_to_octave /datayes/mercury/py_to_octave && \
rm -f py_to_octave.tar.gz

# fix dependency for octave-engine
RUN cd /datayes/mercury/py_to_octave/pkg && \
octave && \
pkg install io-2.4.13.tar.gz && \
pkg install statistics-1.4.1.tar.gz && \
quit

ENTRYPOINT cd /datayes/mercury/py_to_octave/bin && bash run_with_docker.sh