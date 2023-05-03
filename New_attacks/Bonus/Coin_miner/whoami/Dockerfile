FROM alpine:latest as builder

RUN apk --no-cache --no-progress add git ca-certificates tzdata make \
    && update-ca-certificates \
    && rm -rf /var/cache/apk/*

RUN apk add --update --no-cache go vim git make musl-dev curl
ENV GOPATH=/root/go
ENV PATH=${GOPATH}/bin:/usr/local/go/bin:$PATH
ENV GOBIN=$GOROOT/bin
RUN mkdir -p ${GOPATH}/src ${GOPATH}/bin

RUN apk update && apk upgrade --available
RUN apk add --update python3 py3-pip
RUN pip install requests

ENV PATH=$PATH:/usr/bin/python
RUN echo $PATH > ~/.profile

ENV PATH=$PATH:/usr/bin/go
RUN echo $PATH > ~/.profile

WORKDIR /go/whoami

# Download go modules
COPY go.mod .
COPY go.sum .
RUN GO111MODULE=on GOPROXY=https://proxy.golang.org go mod download

COPY . .

RUN make build

ENTRYPOINT ["./whoami"]
EXPOSE 80
