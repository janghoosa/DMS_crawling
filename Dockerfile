FROM python:alpine
EXPOSE 5000
RUN mkdir /img
WORKDIR /img
RUN git clone --recursive https://github.com/kubernetes-client/python.git && cd python && python setup.py install
RUN pip install kubernetes
RUN pip install asyncio
RUN pip install requests
COPY ./server.py ./server.py

CMD ["python3", "./server.py"]