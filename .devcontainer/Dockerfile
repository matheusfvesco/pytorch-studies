FROM mcr.microsoft.com/devcontainers/python:3.10-bookworm
# updates openssh-client, to avoid problems with ssh key forwarding
RUN apt-get update && apt-get install -y openssh-client
# [Optional] If your pip requirements rarely change, uncomment this section to add them to the image.
COPY requirements.txt /tmp/pip-tmp/
RUN pip3 --disable-pip-version-check --no-cache-dir install -r /tmp/pip-tmp/requirements.txt \
    && rm -rf /tmp/pip-tmp