FROM python:alpine
EXPOSE 5000
# RUN mkdir /img
# WORKDIR /img
RUN apk update && apk add git
RUN git clone https://github.com/kubernetes-client/python.git
WORKDIR python
RUN pip install kubernetes
# RUN python setup.py install
# RUN pip install kubernetes
RUN pip install asyncio
RUN pip install requests
RUN apk add --update curl
# RUN pip install os
RUN curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
RUN curl -LO "https://dl.k8s.io/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl.sha256"
# RUN sudo install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl
COPY ./server.py ./server.py

CMD ["python3", "./server.py"]