FROM ubuntu:latest

RUN apt-get update
RUN apt-get install python3 python3-pip -y

RUN pip3 install flask flask_sqlalchemy flask-bootstrap

WORKDIR /workspace

CMD ["python3", "run.py"]
