from qtpdf import generate_pdf

import json
import sys
import os

if __name__ == '__main__':

    if len(sys.argv) < 6:
        sys.stderr.write("Usage: {} [media dir] [template dir] [template path] "
                         "[context-json] [output filename]\n"
                         .format(sys.argv[0]))
        exit(-1)
    media_dir = os.path.abspath(sys.argv[1])
    template_dir = os.path.abspath(sys.argv[2])
    template_path = sys.argv[3]
    context_json = sys.argv[4]
    output_filename = sys.argv[5]

    with open(context_json, 'rb') as input_file:
        context = json.load(input_file)

    pdf = generate_pdf(template_path, template_dir, media_dir, context)
    with open(output_filename, 'wb') as output_file:
        output_file.write(pdf)
