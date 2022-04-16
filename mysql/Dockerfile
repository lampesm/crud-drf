FROM mysql:8.0.28-oracle

ENV TZ="Asia/Tehran" 

USER root

COPY ./mysql/init_db.sh /docker-entrypoint-initdb.d/

RUN chmod +x /docker-entrypoint-initdb.d/init_db.sh