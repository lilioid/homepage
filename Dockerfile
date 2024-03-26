FROM docker.io/debian:bookworm-slim

# setup base image
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update &&\
    apt-get upgrade -y &&\
    apt-get install -y --no-install-recommends python3 python-is-python3 pipenv
RUN useradd -m -d /usr/local/src/homepage/ -s /bin/bash homepage
WORKDIR /usr/local/src/homepage

# install django server
ADD Pipfile Pipfile.lock ./
RUN pipenv install --system --deploy
ADD LICENSE README.md ./
ADD src/ ./src/

# finalize image
RUN chown -R homepage:homepage /usr/local/src/homepage &&\
    chmod -R u=rX,g=rX,o= /usr/local/src/homepage
USER homepage
EXPOSE 8000/tcp
ENV PYTHONPATH=/usr/local/src/homepage/src/
CMD ["uvicorn", "homepage.main:app", "--host=0.0.0.0", "--port=8000", "--proxy-headers"]
