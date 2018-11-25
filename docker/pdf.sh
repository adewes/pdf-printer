#!/bin/bash
xvfb-run python3 /printer.py /media /templates \
                index.html /context.json /output/index.pdf
chown $TARGET_UID /output/index.pdf
chgrp $TARGET_UID /output/index.pdf
