FROM ubuntu:20.04

ARG VERSION=""
ENV LIBRARY_VERSION=$VERSION

RUN apt-get update \
 && apt-get install --no-install-recommends -y \
 jpegoptim optipng zip

COPY ./opt-script.sh script.sh

ENTRYPOINT ["sh", "script.sh"]
