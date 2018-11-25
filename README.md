# Making HTML-based PDFs with Python + Qt

This repository contains code for generating PDFs from Jinja2 templates using
PyQT5's web rendering engine. It is very handy e.g. for generating PDF invoices
or other documents using templated HTML. It comes with a Docker image that makes
running it easy on servers without an X windows system.

## Installation

To run the code, you need to install the following requirements:

* Python 3
* Jinja2
* Qt5 + PyQt5
* A minimal X Windows system, or XVFB with required X libraries

All instructions below assume you run a Debian/Ubuntu based system (there's a
dockerized version of the system that you can use as well, please look below).

To install the required X window libraries:

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

To install the Python dependencies:

    pip3 install -r requirements.txt

## Usage

To generate a demo PDF using the `printer.py` script, simply run

    make python-example

You can also run the printer using XVFB:

    make python-example-xvfb

This will generate a PDF using the content in the `example` directory, storing
the output to `example/output/index.pdf`.

## Docker Image

This repository includes a `Dockerfile` that allows you to build a Docker image
that can run the PDF printer (for better isolation / security). To build the
image locally, run

    make docker-image

You can then run the PDF creator on the example data using the following command:

    make docker-example

Have a look at the Makefile to see how to run the container. Basically,
it expects templates to be mounted under `/templates`, media under
`/media`, the context given as a JSON file located at `/context.json` and
a writeable output directory mounted at `/output`. It will then look for an
`index.html` file in the template directory and write PDF output to
`/output/index.pdf`. The UID/GID of the output file will be set to the values
specified using the `TARGET_UID` environment variable.

## License

The code in this repository is in the public domain, you can use it without any
kind of attribution, in any way you please and at your own risk.