import sys
import json
import os
from PyQt5 import QtWidgets, QtWebEngineWidgets
from PyQt5.QtCore import QUrl

class SessionManager:
    def __init__(self, session_file='session.json'):
        self.session_file = session_file
        self.session_data = {}
        self.load_session()

    def load_session(self):
        if os.path.exists(self.session_file):
            with open(self.session_file, 'r') as f:
                self.session_data = json.load(f)

    def save_session(self):
        with open(self.session_file, 'w') as f:
            json.dump(self.session_data, f)

    def get_session_data(self):
        return self.session_data

    def set_session_data(self, key, value):
        self.session_data[key] = value
        self.save_session()

class BrowserWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.session_manager = SessionManager()
        self.browser = QtWebEngineWidgets.QWebEngineView()
        self.setCentralWidget(self.browser)

        self.browser.urlChanged.connect(self.on_url_changed)
        self.browser.loadFinished.connect(self.on_load_finished)

        self.setWindowTitle("LiventCord")
        self.setGeometry(100, 100, 1200, 800)

        initial_url = self.session_manager.get_session_data().get('last_visited_url', 'http://localhost:5005/app')
        self.load_page(initial_url)

    def load_page(self, url):
        self.browser.setUrl(QUrl(url))

    def on_url_changed(self, q):
        print(f"Navigated to: {q.toString()}")
        self.session_manager.set_session_data('last_visited_url', q.toString())

    def on_load_finished(self, success):
        if success:
            print("Page loaded successfully.")

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = BrowserWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
