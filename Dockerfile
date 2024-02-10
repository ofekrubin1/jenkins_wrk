FROM ubuntu:latest
ENV VERSION=1.2.0
RUN apt-get update && \
    apt-get install -y python3 vim zip unzip && \
    rm -rf /var/lib/apt/lists/*
COPY zip_job.py /tmp/
CMD ["sh", "-c", "echo 'Operating System:' $(uname -s) $(uname -m) && [ -e /tmp/zip_job.py ] && echo '/tmp/zip_job.py exists' || echo '/tmp/zip_job.py does not exist'"]

