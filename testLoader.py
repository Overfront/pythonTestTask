import sys
from PyQt5.QtCore import pyqtSlot, QObject
from PyQt5.QtWebKitWidgets import QWebView
from PyQt5.QtWidgets import QApplication


class Foo(QObject):
    @pyqtSlot(int)
    def file_info(self, value):
        print('File size: {0} b'. format(value))


class MyApp(QWebView):
    def __init__(self):
        self.view = QWebView.__init__(self)
        self.setWindowTitle('File loading...')
        self.foo = Foo(self)
        self.page().mainFrame().addToJavaScriptWindowObject("foo", self.foo)

    def start(self, htmlPage):
        try:
            with open(htmlPage) as page:
                self.setHtml(page.read())
        except EnvironmentError:  # parent of IOError, OSError *and* WindowsError where available
            print('Please, put the "page.html" file in this directory and try again!')
            exit()


# Create an application
app = QApplication(sys.argv)

# Create and fill a QWebView
view = MyApp()
view.start("page.html")
# Show the window and run the app
view.show()

app.exec_()
