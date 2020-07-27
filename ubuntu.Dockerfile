FROM ubuntu:20.04

ADD ubuntu.sources.list /etc/apt/sources.list
ADD . /root
ADD ".ycm_c-c++_conf.py" /tmp

RUN apt-get -y update && apt-get -y upgrade\
    && apt-get install -y  sudo python3 vim git

ENV PYTHONIOENCODING=utf-8

CMD ["/bin/bash"]
