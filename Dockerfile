FROM python:3.5
MAINTAINER chck

RUN \
  apt-get update && \
  apt-get install -y libxmu-dev libxi-dev && \
  apt-get install -y freeglut3-dev libglew1.5-dev

RUN \
  apt-get install -y \
    python-numpy python-dev cmake zlib1g-dev \
    libjpeg-dev xvfb libav-tools xorg-dev \
    python-opengl libboost-all-dev libsdl2-dev swig

RUN \
  mkdir -p /work

WORKDIR \
  /work

ADD \
  requirements.txt /work

RUN \
  pip install -r requirements.txt && \
  pip install 'gym[atari]'

