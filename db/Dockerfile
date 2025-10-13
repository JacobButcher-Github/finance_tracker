FROM postgres:latest

WORKDIR /
COPY db/init_db.sh /docker-entrypoint-initdb.d/10-init_job_db.sh
COPY db/finances.sql /docker-entrypoint-initdb.d/

RUN sed -i '1s;^;\\set ON_ERROR_STOP off\n;' /docker-entrypoint-initdb.d/books.sql.init

WORKDIR /docker-entrypoint-initdb.d
RUN chown -R postgres:postgres /docker-entrypoint-initdb.d && \
  chmod -R 755 /docker-entrypoint-initdb.d
