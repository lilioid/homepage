FROM docker.io/debian:bookworm as final

# setup process supervisor
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update &&\
    apt-get install -y --no-install-recommends python3 python-is-python3 pipenv nginx gunicorn xz-utils supervisor
COPY docker/supervisord.conf /etc/supervisor/supervisord.conf
COPY docker/start_django.sh docker/start_nginx.sh /usr/local/bin/
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/supervisord.conf"]

# install django server
WORKDIR /usr/local/src/homepage/
ADD Pipfile Pipfile.lock ./
RUN pipenv install --system --deploy
ADD LICENSE README.md ./
ADD src/ ./src/

# configure nginx
ADD docker/nginx.conf /etc/nginx/sites-enabled/default

# add some image metadata and config
EXPOSE 8000/tcp
ENV APP_MODE=prod
