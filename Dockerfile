FROM ubuntu

COPY ./requirements.txt /flask-app/requirements.txt

WORKDIR /flask-app

RUN apt-get update && apt-get -y upgrade

RUN apt install -y python3.10

RUN apt-get -y install python3-pip

RUN pip3 install -r requirements.txt

COPY . /flask-app

ENTRYPOINT ["python3"]

CMD ["app.py"]