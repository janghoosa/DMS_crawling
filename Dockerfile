FROM python:alpine
EXPOSE 5000
RUN mkdir /img
WORKDIR /img
RUN pip install requests
COPY ./server.py ./server.py

CMD ["python3", "./server.py"]