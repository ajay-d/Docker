FROM ubuntu:16.04
MAINTAINER ajay@deonarine.com

RUN apt-get upgrade -y && apt-get dist-upgrade

RUN apt-get update && apt-get install -y \
    build-essential \
    apt-transport-https \
	r-base \
&& rm -rf /var/lib/apt/lists/*

#Add new cran repo
RUN echo 'deb https://cloud.r-project.org/bin/linux/ubuntu xenial/' >> /etc/apt/sources.list

##And Key
RUN gpg --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys E084DAB9
RUN gpg -a --export E084DAB9 | apt-key add -

RUN apt-get update && apt-get upgrade -y \
&& rm -rf /var/lib/apt/lists/*

WORKDIR /home/work
