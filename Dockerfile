FROM ubuntu:18.04
RUN apt-get update
RUN apt-get install -y gnupg2
RUN apt-get install -y wget
RUN echo deb http://apt.postgresql.org/pub/repos/apt/ bionic-pgdg main >> /etc/apt/sources.list.d/pgdg.list
RUN wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add -
RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install -y python3 python3-pip
RUN apt-get install -y postgresql-client-11

ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD . /code/

RUN pip3 install -r requirements.txt
