FROM docker.io/debian:bookworm-slim

# setup base image
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update &&\
    apt-get upgrade -y &&\
    apt-get install -y --no-install-recommends python3 python3-pip python-is-python3
RUN useradd -m -d /usr/local/src/homepage/ -s /bin/bash homepage
WORKDIR /usr/local/src/homepage

# install django server
ADD pyproject.toml LICENSE README.md ./
ADD src/ ./src/
RUN pip install --break-system-packages --editable .
ADD LICENSE README.md ./
ADD src/ ./src/

# finalize image
RUN chown -R homepage:homepage /usr/local/src/homepage &&\
    chmod -R u=rX,g=rX,o= /usr/local/src/homepage
USER homepage
EXPOSE 8000/tcp
CMD ["hypercorn", "homepage.main:app", "--bind=0.0.0.0:8000"]
