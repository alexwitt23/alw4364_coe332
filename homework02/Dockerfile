FROM centos:7.7.1908

RUN yum update -y && \
    yum install -y python3 && \
    rm -rf /var/cache/yum

WORKDIR /build

# Workaround to allow special characters in `setup.py`s
ENV LC_CTYPE=en_US.UTF-8
ENV LANG=en_US.UTF-8

# Copy in all necessary files from repository.
ADD homework02/read_animals.py /build
ADD homework02/generate_animals.py /build

# Upgrade pip and install packages
RUN python3 -m pip install --upgrade --user pip petname==2.2

# Set read and execute permissions on the files
RUN chmod +rx generate_animals.py && \
    chmod +rx read_animals.py

# Add the code to our environment path so the scripts can be
# invoked by simply calling their names.
ENV PATH "/build:$PATH"

WORKDIR /home
