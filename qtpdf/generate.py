from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QPageLayout, QPageSize 
from PyQt5.QtPrintSupport import QPrinter
from PyQt5.QtWebEngineWidgets import QWebEngineView
from jinja2 import Environment, FileSystemLoader

def generate_pdf(
        template_path,
        template_dir,
        media_dir,
        template_context,
        page_size="A4",
        page_orientation="Portrait"):

    #we use an array to pass the result asynchronously
    ob = []

    jinja_env = Environment(loader=FileSystemLoader(template_dir))

    template_context['media_dir'] = media_dir
    template = jinja_env.get_template(template_path)
    html = template.render(**template_context)
    app = QApplication.instance()
    if app is None:
        app = QApplication(['--platform','minimal'])
    web = QWebEngineView()
    url = QUrl.fromLocalFile(media_dir)
    web.setHtml(html,baseUrl=url)
    layout = QPageLayout()

    # you can change the page size / layout here
    layout.setPageSize(QPageSize(getattr(QPageSize, page_size)))
    layout.setOrientation(getattr(QPageLayout.Orientation, page_orientation))

    def callback(b, ob=ob):
        ob.append(b)
        app.quit()

    def printPage():
        web.page().printToPdf(callback, layout)

    web.loadFinished.connect(printPage)
    app.exec_()
    return ob[0]
