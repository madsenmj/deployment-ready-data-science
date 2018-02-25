FROM nvidia/cuda:8.0-cudnn5-devel

RUN apt-get update --fix-missing && apt-get install -y wget bzip2 ca-certificates \
    curl build-essential libpng12-dev libffi-dev \
    libglib2.0-0 libxext6 libsm6 libxrender1 \
    git mercurial subversion && \
    apt-get clean && \
    rm -rf /var/tmp /tmp /var/lib/apt/lists/*

RUN curl -sSL -o installer.sh https://repo.continuum.io/archive/Anaconda3-5.1.0-Linux-x86_64.sh && \
    bash /installer.sh -b -f && \
    rm /installer.sh

ENV PATH "$PATH:/root/anaconda3/bin"

EXPOSE 8888 6006
VOLUME /code
WORKDIR "/code"

CMD [""]



