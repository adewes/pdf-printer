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

    xvfb-run python printer.py [...]

For an example, checkout out the `python-example` target of the Makefile:

    make python-example

This will generate a PDF using the content in the `example` directory.

## Docker Image

This repository includes a `Dockerfile` that allows you to build a Docker image
that can run the PDF printer (for better isolation / security). To build the
image locally, run

    make docker-image

You can then run the PDF creator on the example data using the following command:

    make docker-example

Have a look at the Makefile to see how to process different files. Basically,
the container expects templates to be mounted under `/templates`, media under
`/media`, the context given as a JSON file located at `/context.json` and
a writeable output directory mounted at `/output`. It will look for an
`index.html` file in the template directory and write its output to `/output/index.pdf`.
The UID/GID of the output file will be set to the values specified using the
`TARGET_UID` environment variable.

## License

The code in this repository is in the public domain, you can use it without any kind of attribution,
in any way you please and at your own risk.
