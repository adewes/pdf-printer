# Making HTML-based PDFs with Python + Qt

To run this, you need to install the following requirements:

* Python 3
* jinja2
* Qt5 + PyQt5

To install the dependencies you can (often) simply use pip:

    pip3 install -r requirements.txt

To generate the demo PDF, simply run

    python printer.py

This should generate three PDFs named `test-0.pdf`, `test-1.pdf` and `test-2.pdf`, showing that
the printer and event loop works when processing multiple documents.

## System Requirements

PyQt5 requires several X window libraries that are not automatically installed
when installing it through pip. If you don't have a working X setup (e.g. because you run this on a server) you can install the requirements along with xvfb using

    sudo apt-get install \
        libxcomposite1 \
        libxcursor1 \
        libxi6 \
        libfontconfig \
        libxrandr2 \
        libasound2 \
        libegl1 \
        xvfb \
        libnss3 \
        libxtst6

You can then run the printer using XVFB:

    xvfb-run python printer.py

## Docker Image

This repository includes a `Dockerfile` that allows you to build a Docker image
that can run the PDF printer (for better isolation / security). To build the
image locally, run

    docker build . --tag pdf-printer:latest

You can then run the PDF creator using the following command:

    docker run pdf-printer:latest -v media:/media -v templates:/templates -v output:/output

## License

The code in this repository is in the public domain, you can use it without any kind of attribution,
in any way you please and at your own risk.
