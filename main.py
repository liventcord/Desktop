import sys
import json
import os
from PyQt5 import QtWidgets, QtWebEngineWidgets
from PyQt5.QtCore import QUrl

class BrowserWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.browser = QtWebEngineWidgets.QWebEngineView()
        self.setCentralWidget(self.browser)
        self.setWindowTitle("LiventCord")
        self.setGeometry(100, 100, 1200, 800)
        initial_url = "http://localhost:5005/app"
        self.load_page(initial_url)

    def load_page(self, url):
        self.browser.setUrl(QUrl(url))

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = BrowserWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
