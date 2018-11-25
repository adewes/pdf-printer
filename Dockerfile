FROM ubuntu:18.04
RUN apt-get update
RUN apt-get install -y \
    libxcomposite1 \
    libxcursor1 \
    libxi6 \
    libfontconfig \
    libxrandr2 \
    libasound2 \
    libegl1 \
    xvfb \
    python3 \
    python3-pip \
    libnss3 \
    libxtst6 \
    bash
COPY requirements.txt /requirements.txt
RUN pip3 install -r /requirements.txt
COPY printer.py /printer.py
COPY qtpdf /qtpdf
COPY docker/pdf.sh /pdf.sh
WORKDIR /
RUN mkdir /tmp/runtime-root
ENV XDG_RUNTIME_DIR=/tmp/runtime-root
ENV QTWEBENGINE_CHROMIUM_FLAGS="--disable-logging --no-sandbox --disable-gpu --single-process"
ENTRYPOINT /pdf.sh
