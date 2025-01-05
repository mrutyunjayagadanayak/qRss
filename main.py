import sys
import feedparser
from PySide6.QtWidgets import QApplication, QMainWindow , QMessageBox
from PySide6.QtCore import QFile
from ui.mainwindow import Ui_MainWindow
from PySide6.QtCore import QCoreApplication
from helpers import url_validator


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        #Setup menu items
        self.ui.action_quit.triggered.connect(QCoreApplication.quit)
        self.ui.action_about.triggered.connect(self.on_about_clicked)

        self.ui.add_button.clicked.connect(self.on_addbutton_clicked)
        self.ui.remove_button.clicked.connect(self.on_removebutton_clicked)


    def on_addbutton_clicked(self):
        url = self.ui.feed_line_edit.text()
        if url_validator(url):
            feed = feedparser.parse(url)
            print(feed['feed']['title'])
        else:
            QMessageBox().warning(self,"Invalid FEED","Entered feed URL is incorrect, Please enter a valid URL")


    def on_removebutton_clicked(self):
        print("Remove button clicked")

    def on_about_clicked(self):
        msgbox = QMessageBox()
        msgbox.setText("This is a free RSS reader made using pyside6 and python3")
        msgbox.exec()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window =MainWindow()
    window.show()

    sys.exit(app.exec())


