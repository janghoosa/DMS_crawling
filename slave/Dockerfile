FROM python:alpine
EXPOSE 3000
RUN mkdir /mydata
WORKDIR /mydata
RUN pip install beautifulsoup4
RUN pip install flask
COPY ./crawller.py ./crawller.py

CMD ["python", "./crawller.py"]