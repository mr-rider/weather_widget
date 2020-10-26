import sys
import datetime
from weather_request import get_current_weather

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QStatusBar
from PyQt5.QtWidgets import QToolBar
from PyQt5 import QtCore


class Window(QMainWindow):
    """Main Window."""

    def __init__(self, parent = None):
        super().__init__(parent)
        self.setWindowTitle('Weather')
        self.setGeometry(100, 100, 280, 80)
        self.update_weather()
        #self.setCentralWidget(QLabel(f'<h1>Weather Update С</h1>'))
        self.create_menu()
        self.create_toolbar()
        self.create_status_bar()

    def create_menu(self):
        self.menu = self.menuBar().addMenu("&Menu")
        self.menu.addAction('&Exit', self.close)

    def create_toolbar(self):
        tools = QToolBar()
        self.addToolBar(tools)
        tools.addAction('Exit', self.close)

    def create_status_bar(self):
        status = QStatusBar()
        status.showMessage("I'm the Status Bar")
        self.setStatusBar(status)

    def update_weather(self):
        current_temperature = get_current_weather()['current']['temperature']
        self.setCentralWidget(QLabel(f'<h1> In Irkutsk {current_temperature} C </h1>'))
        print(current_temperature)





if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Window()
    win.show()

    #updating of weather every 600000 milecseconds
    timer = QtCore.QTimer()
    timer.timeout.connect(win.update_weather)
    timer.start(600000)

    sys.exit(app.exec())




