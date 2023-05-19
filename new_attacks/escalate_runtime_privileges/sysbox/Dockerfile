FROM ubuntu:20.04

RUN apt-get update && \
    apt-get install -y build-essential curl

RUN curl -OL https://golang.org/dl/go1.20.3.linux-amd64.tar.gz
RUN tar -C /usr/local -xvf go1.20.3.linux-amd64.tar.gz

ENV PATH=$PATH:/usr/local/go/bin
RUN echo $PATH > ~/.profile

COPY . /home/app
WORKDIR /home/app

RUN go build .
RUN go install .

ENTRYPOINT ["./sysbox"]
