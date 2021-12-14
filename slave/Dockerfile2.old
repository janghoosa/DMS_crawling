FROM centos:centos7

ENV container docker

RUN su
RUN (cd /lib/systemd/system/sysinit.target.wants/; for i in *; do [ $i == systemd-tmpfiles-setup.service ] || rm -f $i; done); \
rm -f /lib/systemd/system/multi-user.target.wants/*;\
rm -f /etc/systemd/system/*.wants/*;\
rm -f /lib/systemd/system/local-fs.target.wants/*; \
rm -f /lib/systemd/system/sockets.target.wants/*udev*; \
rm -f /lib/systemd/system/sockets.target.wants/*initctl*; \
rm -f /lib/systemd/system/basic.target.wants/*;\
rm -f /lib/systemd/system/anaconda.target.wants/*;
RUN yum -y install epel-release
RUN yum -y install python3
RUN yum -y install python-pip
RUN yum -y install nginx
RUN easy_install-3.6 pip
RUN pip install beautifulsoup4


EXPOSE 80
COPY ./crawller.py ./home/crawller.py
WORKDIR /home

CMD ["nginx", "-g", "daemon off;"]