FROM python:3.6
MAINTAINER Tarun Kumar Bhati

RUN mkdir /market
WORKDIR /market
ADD . /market/

RUN pip install -r requirements.txt

ENTRYPOINT ["/bin/bash", "-c", "/market/run_server.sh"]



