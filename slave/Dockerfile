FROM centos:7

RUN su
RUN yum -y install epel-release
RUN yum -y install python3
RUN yum -y install python-pip
RUN yum -y install nginx
RUN easy_install-3.6 pip
RUN pip install beautifulsoup4
COPY ./crawller.py ./home/crawller.py

WORKDIR /home