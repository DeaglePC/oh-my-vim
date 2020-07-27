FROM centos:centos8

ADD . /root
ADD ".ycm_c-c++_conf.py" /tmp

RUN yum -y update && yum -y upgrade \
    && yum install -y sudo python3 vim git

ENV PYTHONIOENCODING=utf-8

CMD ["/bin/bash"]
