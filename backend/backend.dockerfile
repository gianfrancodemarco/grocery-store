# This is no longer maintend
# Update using https://github.com/pyb4430/full-stack-fastapi-postgresql
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

# Install ORACLE client
ENV LD_LIBRARY_PATH=/opt/oracle/instantclient_21_4

RUN apt-get update && \
    apt-get install -y libpq-dev zlib1g-dev build-essential shared-mime-info libaio1 libaio-dev unzip wget --no-install-recommends && \
    wget https://download.oracle.com/otn_software/linux/instantclient/214000/instantclient-sdk-linux.x64-21.4.0.0.0dbru.zip && \
    wget https://download.oracle.com/otn_software/linux/instantclient/214000/instantclient-sqlplus-linux.x64-21.4.0.0.0dbru.zip && \
    wget https://download.oracle.com/otn_software/linux/instantclient/214000/instantclient-basic-linux.x64-21.4.0.0.0dbru.zip && \
    mkdir -p /opt/oracle && \
    cp instantclient-* /opt/oracle/ && \
    cd /opt/oracle/ && \
    unzip instantclient-basic-linux.x64-21.4.0.0.0dbru.zip && \
    unzip instantclient-sdk-linux.x64-21.4.0.0.0dbru.zip && \
    unzip instantclient-sqlplus-linux.x64-21.4.0.0.0dbru.zip && \
    rm -rf /var/lib/apt/lists/* instantclient-basic-linux.x64-21.4.0.0.0dbru.zip instantclient-sdk-linux.x64-21.4.0.0.0dbru.zip instantclient-sqlplus-linux.x64-21.4.0.0.0dbru.zip && \
    apt -y clean && \
    apt -y remove wget unzip && \
    apt -y autoremove && \
    rm -rf /var/cache/apt

WORKDIR /app/
ADD ./app /app

RUN pip install -r requirements.txt

ENV PYTHONPATH=/app