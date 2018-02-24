FROM ubuntu:16.04

MAINTAINER Martin Madsen <madsen.mj@gmail.com> 

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
ADD startup /startup

EXPOSE 8888 6006
VOLUME /code
WORKDIR "/code"

#CMD ["jupyter", "notebook", "--port=8888", "--no-browser", "--ip=0.0.0.0"]
CMD ["/bin/bash"]

ADD environment.yml /environment.yml
RUN conda env create -f /environment.yml

ENV CONDA_ENV tensorflow

# Run app.py when the container launches
# CMD ["python", "app.py"]