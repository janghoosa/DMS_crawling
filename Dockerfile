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
COPY ./server.py ./server.py

CMD ["python3", "./server.py"]