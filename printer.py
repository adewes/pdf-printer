from PyQt4.QtGui import QApplication, QPrinter
from PyQt4.QtCore import QUrl
from PyQt4.QtWebKit import QWebView
import os

from jinja2 import Environment, FileSystemLoader

jinja_env = Environment(loader=FileSystemLoader('templates'))#add your loaders here if necessary

def generate_pdf(template, filename, media_path=None, template_context=None):
    global app

    if template_context is None:
        template_context = {}
    template_context['media_path'] = media_path
    #put your templates in the pdf subdirectory
    template_path = '{0}.html'.format(template)
    template = jinja_env.get_template(template_path)
    html = template.render(**template_context)
    app = QApplication.instance()
    if app is None:
        app = QApplication(['--platform','minimal'])
    web = QWebView()
    url = QUrl.fromLocalFile(media_path)
    web.setHtml(html,baseUrl = url)
    #we need this call to correctly render images...
    app.processEvents()
    printer = QPrinter()
    printer.setPageSize(QPrinter.A4)
    printer.setOutputFormat(QPrinter.PdfFormat)
    printer.setOutputFileName(filename)
    web.print_(printer)

if __name__ == '__main__':
    generate_pdf('example','test.pdf',os.path.abspath('media'),template_context={})
