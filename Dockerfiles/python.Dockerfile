FROM python:3.9.6-slim-buster@sha256:fb734fd2a226ab1cbe09beb6ade31f69e943b33d10be3160eaf950335c243d9f

RUN apt update \
  && apt-get install -y --no-install-recommends libaio1 libaio-dev wget unzip procps \
  && python -m pip install cx_Oracle requests --upgrade \
  && pip freeze \
  && apt-get -y autoremove \
  && apt-get clean autoclean \
  && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN set -o errexit -o nounset \
  && echo "Downloading Oracle Instant Client" \
  && wget --no-verbose --output-document=/tmp/client.zip "https://download.oracle.com/otn_software/linux/instantclient/211000/instantclient-basiclite-linux.x64-21.1.0.0.0.zip" \
  \
  && echo "Test checksum" \
  && if [ $(cksum /tmp/client.zip | cut -f 1 -d' ') != 4212154228 ]; then echo 'Failed checksum'; exit 1; fi \
  \
  && echo "Installing Oracle Instant Client" \
  && mkdir /oracle \
  && unzip /tmp/client.zip -d /oracle/ \
  && mv /oracle/instantclient* /oracle/client \
  && rm /tmp/client.zip

ENV LD_LIBRARY_PATH=/oracle/client
ENV TNS_ADMIN=/usr/local/adm/config/tomcat/oracle_wallets/lms

COPY loop.sh /

# Use this shell script to keep container running in background and exit gracefully with Docker kill signal
# Shell script can handle kill signal better than build-in commands like tail and cat
CMD ["/loop.sh"]
