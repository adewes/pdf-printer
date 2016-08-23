# Making HTML-based PDFs with Python + Qt

To run this, you need to install the following requirements:

* jinja2
* Qt4 + PyQt4

You can also use Qt5 (see printer_pyqt5), which requires PyQt5 + Pyqt5-webview.

To generate the demo PDF, simply run

    python printer.py
    #or
    python printer_pyqt5.py

## Running this without an X server

The code needs an X server to run in the background. To run it from a headless server, you can
use e.g. xvfb-run:

    xvfb-run python printer.py
