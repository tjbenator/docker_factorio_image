FROM ubuntu:16.04
MAINTAINER tjbenator <tjbenator@gmail.com>

WORKDIR /opt

COPY start.py factorio/start.py

VOLUME /opt/factorio/saves /opt/factorio/mods

EXPOSE 34197/udp
EXPOSE 27015/tcp


ENV VERSION=0.14.22 \
    FACTORIO_SHA1=c43fa0d750e8347ec466ce165053db3cd3dc2fe0

RUN apt-get update -y && \
    apt-get install curl python -y && \
    curl -sSL https://www.factorio.com/get-download/$VERSION/headless/linux64 -o /tmp/factorio_headless_x64_$VERSION.tar.gz && \
    echo "$FACTORIO_SHA1  /tmp/factorio_headless_x64_$VERSION.tar.gz" | sha1sum -c && \
    tar xzf /tmp/factorio_headless_x64_$VERSION.tar.gz && \
    rm /tmp/factorio_headless_x64_$VERSION.tar.gz

WORKDIR /opt/factorio

CMD ["/usr/bin/python", "/opt/factorio/start.py"]
