FROM alpine:latest

RUN echo "Installing Nmap" && \
    apk update && \
    apk upgrade && \
    apk add build-base && \
    apk add flex && \
    apk add libcap-dev && \
    apk add openssl-dev && \
    apk add libssh2-dev && \
    apk add bison && \
    apk add curl

WORKDIR /app
COPY . /app/

RUN ./configure && \
    make && \
    make install

ENTRYPOINT ["nmap"]
