FROM python:alpine
EXPOSE 5000
RUN mkdir /img
WORKDIR /img
RUN pip install requests
RUN pip install flask
COPY ./server.py ./server.py

CMD ["python", "./server.py"]