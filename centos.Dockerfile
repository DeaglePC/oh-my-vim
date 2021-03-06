FROM centos:centos8

ADD . /root
COPY .ycm_cpp_conf.py /tmp/

RUN yum -y update && yum -y upgrade \
    && yum install -y sudo python3 vim git

ENV PYTHONIOENCODING=utf-8

CMD ["/bin/bash"]
