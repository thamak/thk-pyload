FROM resin/rpi-raspbian

RUN adduser --system pyload

run echo "deb http://mirrordirector.raspbian.org/raspbian/ jessie main contrib non-free rpi" >> /etc/apt/sources.list
RUN echo "deb-src http://archive.raspbian.org/raspbian/ jessie main contrib non-free rpi" >> /etc/apt/sources.list

RUN apt-get update \
  && apt-get upgrade --force-yes --yes \
  && apt-get install -y git \
    nano \
    liblept4 \
    python \
    python-pycurl \
    python-crypto \
    tesseract-ocr \
    python-beaker \
    python-imaging \
    python-openssl \
    libmozjs-24-bin \
    gocr \
    python-django \
    zip \
    unzip \
  && apt-get -y build-dep rar unrar-nonfree \
  && apt-get source -b unrar-nonfree \
  && dpkg -i unrar_*_armhf.deb \
  && rm -rf unrar-* \

RUN ln -s /usr/bin/js24 /usr/bin/js

RUN git clone -b stable https://github.com/pyload/pyload.git /opt/pyload \
  && echo "/opt/pyload/pyload-config" > /opt/pyload/module/config/configdir \
  && chmod +x /run.sh

ADD pyload-config/ /tmp/pyload-config

EXPOSE 8000 7227
VOLUME ["/opt/pyload/pyload-config", "/opt/pyload/Downloads"]

CMD ["/run.sh"]