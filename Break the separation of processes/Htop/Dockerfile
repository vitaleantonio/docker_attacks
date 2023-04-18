FROM alpine:latest

RUN \
  adduser -h /app -s /sbin/nologin -D app && \
  apk add --update --no-cache htop && \
  rm -f /tmp/* /etc/apk/cache/*

USER app

WORKDIR /app
COPY . /app/

#   apk add --no-cache --upgrade bash && \
# RUN chmod +x /app/myhtop

ENTRYPOINT ["sh", "myhtop.sh"]
