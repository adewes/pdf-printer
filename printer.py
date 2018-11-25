from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QUrl, QTimer
from PyQt5.QtGui import QPageLayout
from PyQt5.QtPrintSupport import QPrinter
from PyQt5.QtWebEngineWidgets import QWebEngineView
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
    web = QWebEngineView()
    url = QUrl.fromLocalFile(media_path)
    web.setHtml(html,baseUrl=url)
    #we need this call to correctly render images...
    layout = QPageLayout()
    def callback(b):
        with open(filename, 'wb') as output_file:
            output_file.write(b)
        app.quit()
    def printPage():
        web.page().printToPdf(callback)
    web.loadFinished.connect(printPage)
    app.exec_()

if __name__ == '__main__':
    context = {
        'user' : {
            'name' : 'Andreas'
        }
    }
    for i in range(3):
        context['user']['name'] = 'Andreas {}'.format(i)
        generate_pdf('example','test-{}.pdf'.format(i),os.path.abspath('media'),template_context=context)
