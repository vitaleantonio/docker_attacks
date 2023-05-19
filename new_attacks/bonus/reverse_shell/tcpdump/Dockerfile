FROM ubuntu:latest

RUN \
  apt-get update && \
  apt install -y gcc libpcap-dev autoconf make python3

COPY . /app/
WORKDIR /app

RUN ./autogen.sh && autoupdate && ./configure && make
RUN make install

ENTRYPOINT ["tcpdump"]

