FROM ubuntu:latest

RUN \
  apt-get update && \
  apt install -y libncursesw5-dev autotools-dev autoconf automake build-essential

WORKDIR /app
COPY . /app/

RUN ./autogen.sh && ./configure && make
RUN make install

ENTRYPOINT ["htop"]
